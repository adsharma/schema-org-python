from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.thing import Thing


@dataclass
class PropertyValueSpecification(Intangible):
    """
    A Property value specification.
    """

    defaultValue: Optional[Union[str, List[str], Thing, List[Thing]]] = None
    maxValue: Optional[Union[float, List[float]]] = None
    minValue: Optional[Union[float, List[float]]] = None
    multipleValues: Optional[Union[bool, List[bool]]] = None
    readonlyValue: Optional[Union[bool, List[bool]]] = None
    stepValue: Optional[Union[float, List[float]]] = None
    valueMaxLength: Optional[Union[float, List[float]]] = None
    valueMinLength: Optional[Union[float, List[float]]] = None
    valueName: Optional[Union[str, List[str]]] = None
    valuePattern: Optional[Union[str, List[str]]] = None
    valueRequired: Optional[Union[bool, List[bool]]] = None
