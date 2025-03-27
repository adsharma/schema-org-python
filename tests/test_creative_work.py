# import sys; sys.setrecursionlimit(2000)
from dataclasses import is_dataclass

from pydantic import BaseModel

from schema_models.creative_work import CreativeWork
from schema_models.thing import Thing


def test_creative_work_name():
    c = CreativeWork(awards="test")
    assert isinstance(c, CreativeWork)
    assert isinstance(c, Thing)
    assert is_dataclass(c)
    c_validator = c.validator()
    assert isinstance(c_validator, BaseModel)
