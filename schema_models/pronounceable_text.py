from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.language import Language
from schema_models.text import Text


class PronounceableText(Text):
    textValue: Optional[Union[Text, List[Text]]] = None
    inLanguage: Optional[Union[Language, List[Language]]] = None
    inLanguage: Optional[Union[Text, List[Text]]] = None
    speechToTextMarkup: Optional[Union[Text, List[Text]]] = None
    phoneticText: Optional[Union[Text, List[Text]]] = None
