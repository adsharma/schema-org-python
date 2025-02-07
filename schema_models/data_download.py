from typing import List, Optional, Union

from schema_models.defined_term import DefinedTerm
from schema_models.measurement_method_enum import MeasurementMethodEnum
from schema_models.media_object import MediaObject
from schema_models.text import Text
from schema_models.url import URL


class DataDownload(MediaObject):
    measurementMethod: Optional[Union[URL, List[URL]]] = None
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementMethod: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    measurementMethod: Optional[Union[Text, List[Text]]] = None
    measurementTechnique: Optional[Union[Text, List[Text]]] = None
    measurementTechnique: Optional[Union[URL, List[URL]]] = None
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementTechnique: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
