from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.person import Person


class Book(CreativeWork):
    """
    A book.
    """

    numberOfPages: Optional[Union[int, List[int]]] = None
    illustrator: Optional[Union[Person, List[Person]]] = None
    abridged: Optional[Union[bool, List[bool]]] = None
    bookEdition: Optional[Union[str, List[str]]] = None
    isbn: Optional[Union[str, List[str]]] = None
    bookFormat: Optional[Union["BookFormatType", List["BookFormatType"]]] = None
