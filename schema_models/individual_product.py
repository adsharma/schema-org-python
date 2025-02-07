from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.product import Product
from schema_models.text import Text


class IndividualProduct(Product):
    serialNumber: Optional[Union[Text, List[Text]]] = None
