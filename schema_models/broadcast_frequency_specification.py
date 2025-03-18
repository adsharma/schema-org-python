from typing import List, Optional, Union

from schema_models.intangible import Intangible


class BroadcastFrequencySpecification(Intangible):
    """
    The frequency in MHz and the modulation used for a particular BroadcastService.
    """

    broadcastSubChannel: Optional[Union[str, List[str]]] = None
    broadcastFrequencyValue: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    broadcastSignalModulation: Optional[
        Union["QualitativeValue", List["QualitativeValue"], str, List[str]]
    ] = None
