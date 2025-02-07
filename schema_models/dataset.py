from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.data_catalog import DataCatalog
from schema_models.data_download import DataDownload
from schema_models.date_time import DateTime
from schema_models.defined_term import DefinedTerm
from schema_models.measurement_method_enum import MeasurementMethodEnum
from schema_models.property import Property
from schema_models.property_value import PropertyValue
from schema_models.statistical_variable import StatisticalVariable
from schema_models.text import Text
from schema_models.url import URL


class Dataset(CreativeWork):
    measurementMethod: Optional[Union[URL, List[URL]]] = None
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementMethod: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    measurementMethod: Optional[Union[Text, List[Text]]] = None
    issn: Optional[Union[Text, List[Text]]] = None
    measurementTechnique: Optional[Union[Text, List[Text]]] = None
    measurementTechnique: Optional[Union[URL, List[URL]]] = None
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    measurementTechnique: Optional[
        Union[MeasurementMethodEnum, List[MeasurementMethodEnum]]
    ] = None
    catalog: Optional[Union[DataCatalog, List[DataCatalog]]] = None
    variablesMeasured: Optional[Union[Text, List[Text]]] = None
    variablesMeasured: Optional[Union[PropertyValue, List[PropertyValue]]] = None
    variableMeasured: Optional[
        Union[StatisticalVariable, List[StatisticalVariable]]
    ] = None
    variableMeasured: Optional[Union[Property, List[Property]]] = None
    variableMeasured: Optional[Union[Text, List[Text]]] = None
    variableMeasured: Optional[Union[PropertyValue, List[PropertyValue]]] = None
    includedDataCatalog: Optional[Union[DataCatalog, List[DataCatalog]]] = None
    includedInDataCatalog: Optional[Union[DataCatalog, List[DataCatalog]]] = None
    datasetTimeInterval: Optional[Union[DateTime, List[DateTime]]] = None
    distribution: Optional[Union[DataDownload, List[DataDownload]]] = None
