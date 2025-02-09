from datetime import datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm
from schema_models.property import Property


class Dataset(CreativeWork):
    measurementMethod: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementMethod: Optional[
        Union["MeasurementMethodEnum", List["MeasurementMethodEnum"]]
    ] = None
    measurementMethod: Optional[Union[str, List[str]]] = None
    issn: Optional[Union[str, List[str]]] = None
    measurementTechnique: Optional[Union[str, List[str]]] = None
    measurementTechnique: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementTechnique: Optional[
        Union["MeasurementMethodEnum", List["MeasurementMethodEnum"]]
    ] = None
    catalog: Optional[Union["DataCatalog", List["DataCatalog"]]] = None
    variablesMeasured: Optional[Union[str, List[str]]] = None
    variablesMeasured: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    variableMeasured: Optional[
        Union["StatisticalVariable", List["StatisticalVariable"]]
    ] = None
    variableMeasured: Optional[Union[Property, List[Property]]] = None
    variableMeasured: Optional[Union[str, List[str]]] = None
    variableMeasured: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    includedDataCatalog: Optional[Union["DataCatalog", List["DataCatalog"]]] = None
    includedInDataCatalog: Optional[Union["DataCatalog", List["DataCatalog"]]] = None
    datasetTimeInterval: Optional[Union[datetime, List[datetime]]] = None
    distribution: Optional[Union["DataDownload", List["DataDownload"]]] = None
