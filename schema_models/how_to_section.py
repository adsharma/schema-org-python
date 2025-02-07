from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.item_list import ItemList
from schema_models.list_item import ListItem
from schema_models.text import Text


class HowToSection(ListItem):
    steps: Optional[Union[ItemList, List[ItemList]]] = None
    steps: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    steps: Optional[Union[Text, List[Text]]] = None
