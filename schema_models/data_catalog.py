from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.dataset import Dataset
from schema_models.defined_term import DefinedTerm
from schema_models.text import Text
from schema_models.url import URL


class DataCatalog(CreativeWork):
    measurementMethod: Optional[Union[URL, List[URL]]] = None
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementMethod: Optional[
        Union["MeasurementMethodEnum", List["MeasurementMethodEnum"]]
    ] = None
    measurementMethod: Optional[Union[Text, List[Text]]] = None
    dataset: Optional[Union[Dataset, List[Dataset]]] = None
    measurementTechnique: Optional[Union[Text, List[Text]]] = None
    measurementTechnique: Optional[Union[URL, List[URL]]] = None
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementTechnique: Optional[
        Union["MeasurementMethodEnum", List["MeasurementMethodEnum"]]
    ] = None
