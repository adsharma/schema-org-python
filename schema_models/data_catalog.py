from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.dataset import Dataset
from schema_models.defined_term import DefinedTerm


class DataCatalog(CreativeWork):
    measurementMethod: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementMethod: Optional[
        Union["MeasurementMethodEnum", List["MeasurementMethodEnum"]]
    ] = None
    measurementMethod: Optional[Union[str, List[str]]] = None
    dataset: Optional[Union[Dataset, List[Dataset]]] = None
    measurementTechnique: Optional[Union[str, List[str]]] = None
    measurementTechnique: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementTechnique: Optional[
        Union["MeasurementMethodEnum", List["MeasurementMethodEnum"]]
    ] = None
