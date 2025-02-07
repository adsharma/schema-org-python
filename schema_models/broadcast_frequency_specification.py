from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.number import Number
from schema_models.text import Text


class BroadcastFrequencySpecification(Intangible):
    broadcastSubChannel: Optional[Union[Text, List[Text]]] = None
    broadcastFrequencyValue: Optional[Union[Number, List[Number]]] = None
    broadcastFrequencyValue: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    broadcastSignalModulation: Optional[
        Union["QualitativeValue", List["QualitativeValue"]]
    ] = None
    broadcastSignalModulation: Optional[Union[Text, List[Text]]] = None
