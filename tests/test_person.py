from dataclasses import is_dataclass

from schema_models.person import Person
from schema_models.place import Place
from schema_models.thing import Thing


def test_person():
    p = Person(name="user1")
    assert isinstance(p, Person)
    assert isinstance(p, Thing)
    assert not isinstance(p, Place)
    assert is_dataclass(p)
    # p_validator = p.validator()
    # assert isinstance(p_validator, BaseModel)
