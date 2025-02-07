from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.book_format_type import BookFormatType
from schema_models.boolean import Boolean
from schema_models.creative_work import CreativeWork
from schema_models.integer import Integer
from schema_models.person import Person
from schema_models.text import Text


class Book(CreativeWork):
    numberOfPages: Optional[Union[Integer, List[Integer]]] = None
    illustrator: Optional[Union[Person, List[Person]]] = None
    abridged: Optional[Union[Boolean, List[Boolean]]] = None
    bookEdition: Optional[Union[Text, List[Text]]] = None
    isbn: Optional[Union[Text, List[Text]]] = None
    bookFormat: Optional[Union[BookFormatType, List[BookFormatType]]] = None
