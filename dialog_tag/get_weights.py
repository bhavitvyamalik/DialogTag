import requests
from zipfile import ZipFile
import os
from tqdm import tqdm as tqdm
import logging
from .config import model_download_link, model_location
from pathlib import Path


class Download:
    def __init__(self, model_name):
        self.__model_name = model_name
        self.__url =  model_download_link[self.__model_name]
        
        
        try:
            self.__lib_path = f"{str(Path.home())}"+model_location["MODEL"]
            Path(self.__lib_path).mkdir(parents=True, exist_ok=False)
        except:
            print("Model directory already exists, chill!")

        
        self.__model_zip_path = os.path.join(self.__lib_path, self.__model_name+".zip")
        self.__final_path = os.path.join(self.__lib_path, self.__model_name)

    def download_file(self):
        if os.path.dirname(self.__model_zip_path) != '':
            os.makedirs(os.path.dirname(self.__model_zip_path), exist_ok=True)

        req = requests.get(self.__url, stream=True)
        if req.status_code != 200:
            print("Exception when trying to download {}. Response {}".format(self.__url, req.status_code), file=sys.stderr)
            req.raise_for_status()
            return

        download_filepath = self.__model_zip_path +"_part"
        with open(download_filepath, "wb") as file_binary:
            content_length = req.headers.get('Content-Length')
            total = int(content_length) if content_length is not None else None
            progress = tqdm(unit="B", total=total, unit_scale=True)
            for chunk in req.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    progress.update(len(chunk))
                    file_binary.write(chunk)

        os.rename(download_filepath, self.__model_zip_path)
        progress.close()

        zf = ZipFile(self.__model_zip_path, 'r')
        zf.extractall(path = self.__final_path)
        zf.close()

        os.remove(self.__model_zip_path)