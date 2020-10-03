import os
import tensorflow as tf
import operator 
from pathlib import Path

from transformers import AutoTokenizer, TFAutoModelForSequenceClassification, AutoConfig

from .config import model_params, model_location
from .get_weights import Download
from .label_mapping import LabelMapping


class DialogTag:
    def __init__(self, model_name):

        self.__model_name = model_name

        self.__lib_path = f"{str(Path.home())}"+ model_location["MODEL"]
        self.__model_path = os.path.join(self.__lib_path, self.__model_name)
        self.__label_mapping_path = os.path.join(self.__lib_path, self.__model_name) + model_location["label_mapping"]

        # print(self.__lib_path, self.__model_path, self.__label_mapping_path)

        self.__num = len(os.listdir(self.__model_path))
        if(self.__num<3):
            print("Model not found in cache. Downloading...")
            self.__model_file = Download(self.__model_name)
            self.__model_file.download_file()
        else:
            print(f"{self.__model_name} found in cache. Loading model...")

        self.__tokenizer = AutoTokenizer.from_pretrained(self.__model_name, do_lower_case=True)
        self.__config = AutoConfig.from_pretrained(self.__model_path, num_labels=model_params["num_labels"])
        self.__model = TFAutoModelForSequenceClassification.from_pretrained(self.__model_path, config=self.__config)

    def __classhelper(self):
        mapping_object = LabelMapping(self.__label_mapping_path)

        logits_class, class_expanded = mapping_object.helper()

        return logits_class, class_expanded

    def predict_tag(self, sentence):
        predict_input = self.__tokenizer.encode(sentence,
                                 truncation=True,
                                 padding=True,
                                 return_tensors="tf")

        tf_output = self.__model.predict(predict_input)[0]
        tf_prediction = tf.nn.softmax(tf_output, axis=1).numpy()[0]
        index, value = max(enumerate(tf_prediction), key=operator.itemgetter(1))

        # print(value)

        logits_class, class_expanded = self.__classhelper()

        return class_expanded[logits_class[str(index)]]

# test_sentence = "With their homes in ashes, residents share harrowing tales of survival after massive wildfires kill 15"


if __name__=='__main__':
    A  = DialogTag('distilbert-base-uncased')
    # z = A.predict_tag("With their homes in ashes, residents share harrowing tales of survival after massive wildfires kill 15")
    z = A.predict_tag("Stop talking silly!")
    print(z)

