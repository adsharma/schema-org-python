from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_term import DefinedTerm
from schema_models.media_object import MediaObject


@dataclass
class DataDownload(MediaObject):
    """
    All or part of a [[Dataset]] in downloadable form.
    """

    measurementMethod: Optional[
        Union[
            DefinedTerm,
            List[DefinedTerm],
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
            DefinedTerm,
            List[DefinedTerm],
            "MeasurementMethodEnum",
            List["MeasurementMethodEnum"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
