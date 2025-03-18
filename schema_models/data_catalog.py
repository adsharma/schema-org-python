from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.dataset import Dataset
from schema_models.defined_term import DefinedTerm


class DataCatalog(CreativeWork):
    """
    A collection of datasets.
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
    dataset: Optional[Union[Dataset, List[Dataset]]] = None
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
