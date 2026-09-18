from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork


@dataclass
class DataCatalog(CreativeWork):
    """
    A collection of datasets.
    """

    dataset: Optional[Union["Dataset", List["Dataset"]]] = None
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
