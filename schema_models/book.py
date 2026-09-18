from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.person import Person


@dataclass
class Book(CreativeWork):
    """
    A book.
    """

    abridged: Optional[Union[bool, List[bool]]] = None
    bookEdition: Optional[Union[str, List[str]]] = None
    bookFormat: Optional[Union["BookFormatType", List["BookFormatType"]]] = None
    illustrator: Optional[Union[Person, List[Person]]] = None
    isbn: Optional[Union[str, List[str]]] = None
    numberOfPages: Optional[Union[int, List[int]]] = None
