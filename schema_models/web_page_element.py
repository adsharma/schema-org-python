from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.css_selector_type import CssSelectorType
from schema_models.x_path_type import XPathType


class WebPageElement(CreativeWork):
    cssSelector: Optional[Union[CssSelectorType, List[CssSelectorType]]] = None
    xpath: Optional[Union[XPathType, List[XPathType]]] = None
