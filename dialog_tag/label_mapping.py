from .config import class_labels

class LabelMapping():
    def __init__(self, label_mapping_path):
        self.__class_names_file = label_mapping_path

    def __load_class_names(self):
        class_names = []
        with open(self.__class_names_file, 'r') as fp:
            lines = fp.readlines()
        for line in lines:
            line = line.rstrip()
            class_names.append(line)
        return class_names

    def helper(self):
        class_names = self.__load_class_names()
        label_map = {}
        for row in class_names:
            act,label = row.strip().split('|')
            label_map[label] = act

        mapping = class_labels["MAPPING"]
        inv_map = {v: k for k, v in mapping.items()}

        sts = {}
        for k,v in inv_map.items():
            sts[v] = label_map[v]

        return inv_map, sts