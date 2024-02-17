from abc import ABC

from src.abstractclasses import SaveFile, WorkWithApi
from src.jsonsaver import JSONSaver
from src.headhunterapi import HeadHunterAPI

def test_json_saver_issubclass():
    assert issubclass(JSONSaver, SaveFile)
    assert issubclass(SaveFile, ABC)

def test_hhapi_issubclass():
    assert issubclass(HeadHunterAPI, WorkWithApi)
    assert issubclass(WorkWithApi, ABC)
