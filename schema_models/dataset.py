from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.data_catalog import DataCatalog


@dataclass
class Dataset(CreativeWork):
    """
    A dataset contained in this catalog.
    """

    catalog: Optional[Union[DataCatalog, List[DataCatalog]]] = None
    datasetTimeInterval: Optional[Union[datetime, List[datetime]]] = None
    distribution: Optional[Union["DataDownload", List["DataDownload"]]] = None
    includedDataCatalog: Optional[Union[DataCatalog, List[DataCatalog]]] = None
    includedInDataCatalog: Optional[Union[DataCatalog, List[DataCatalog]]] = None
    issn: Optional[Union[str, List[str]]] = None
    measurementMethod: Optional[
        Union[
            "DefinedTerm",
            List["DefinedTerm"],
            "MeasurementMethodEnum",
            List["MeasurementMethodEnum"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    measurementTechnique: Optional[
        Union[
            "DefinedTerm",
            List["DefinedTerm"],
            "MeasurementMethodEnum",
            List["MeasurementMethodEnum"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    variableMeasured: Optional[
        Union[
            "Property",
            List["Property"],
            "PropertyValue",
            List["PropertyValue"],
            "StatisticalVariable",
            List["StatisticalVariable"],
            str,
            List[str],
        ]
    ] = None
    variablesMeasured: Optional[
        Union["PropertyValue", List["PropertyValue"], str, List[str]]
    ] = None
