from datetime import datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm
from schema_models.property import Property


class Dataset(CreativeWork):
    """
    A dataset contained in this catalog.
    """

    measurementMethod: Optional[
        Union[
            HttpUrl,
            List[HttpUrl],
            DefinedTerm,
            List[DefinedTerm],
            "MeasurementMethodEnum",
            List["MeasurementMethodEnum"],
            str,
            List[str],
        ]
    ] = None
    issn: Optional[Union[str, List[str]]] = None
    measurementTechnique: Optional[
        Union[
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
            DefinedTerm,
            List[DefinedTerm],
            "MeasurementMethodEnum",
            List["MeasurementMethodEnum"],
        ]
    ] = None
    catalog: Optional[Union["DataCatalog", List["DataCatalog"]]] = None
    variablesMeasured: Optional[
        Union[str, List[str], "PropertyValue", List["PropertyValue"]]
    ] = None
    variableMeasured: Optional[
        Union[
            "StatisticalVariable",
            List["StatisticalVariable"],
            Property,
            List[Property],
            str,
            List[str],
            "PropertyValue",
            List["PropertyValue"],
        ]
    ] = None
    includedDataCatalog: Optional[Union["DataCatalog", List["DataCatalog"]]] = None
    includedInDataCatalog: Optional[Union["DataCatalog", List["DataCatalog"]]] = None
    datasetTimeInterval: Optional[Union[datetime, List[datetime]]] = None
    distribution: Optional[Union["DataDownload", List["DataDownload"]]] = None
