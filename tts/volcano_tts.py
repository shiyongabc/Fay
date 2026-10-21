import base64
import json
import uuid
import requests
import time
from utils import util, config_util
from utils import config_util as cfg
import wave
from volcano_tts_http_stream import tts_http_stream


class Speech:
    def __init__(self):
        self.appid = cfg.volcano_tts_appid
        self.access_token = cfg.volcano_tts_access_token
        self.api_key = cfg.volcano_tts_api_key
        self.cluster = cfg.volcano_tts_cluster
        self.__history_data = []

    def connect(self):
        pass

    def __get_history(self, voice_name, style, text):
        for data in self.__history_data:
            if data[0] == voice_name and data[1] == style and data[2] == text:
                return data[3]
        return None    

    def to_sample(self, text, style) :
        if cfg.volcano_tts_voice_type != None and cfg.volcano_tts_voice_type != '':
            voice = cfg.volcano_tts_voice_type
        else:
            voice = config_util.config["attribute"]["voice"] if config_util.config["attribute"]["voice"] is not None and config_util.config["attribute"]["voice"].strip() != "" else "爽快思思/Skye"
        try:
            history = self.__get_history(voice, style, text)
            if history is not None:
                return history
            # https://openspeech.bytedance.com/api/v3/tts/unidirectional
            host = "openspeech.bytedance.com"
            #api_url = f"https://{host}/api/v1/tts"
            #header = {"Authorization": f"Bearer;{self.access_token}"}

            file_url=tts_http_stream(txt=text)
            return file_url
           
        except Exception as e :
                util.log(1, "[x] 语音转换失败！")
                util.log(1, "[x] 原因: " + str(str(e)))
                file_url = None
                return file_url


    def close(self):
       pass


