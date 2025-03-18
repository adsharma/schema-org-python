from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.thing import Thing


class PropertyValueSpecification(Intangible):
    """
    A Property value specification.
    """

    defaultValue: Optional[Union[Thing, List[Thing], str, List[str]]] = None
    stepValue: Optional[Union[float, List[float]]] = None
    multipleValues: Optional[Union[bool, List[bool]]] = None
    valuePattern: Optional[Union[str, List[str]]] = None
    valueMinLength: Optional[Union[float, List[float]]] = None
    valueRequired: Optional[Union[bool, List[bool]]] = None
    maxValue: Optional[Union[float, List[float]]] = None
    valueMaxLength: Optional[Union[float, List[float]]] = None
    readonlyValue: Optional[Union[bool, List[bool]]] = None
    valueName: Optional[Union[str, List[str]]] = None
    minValue: Optional[Union[float, List[float]]] = None
