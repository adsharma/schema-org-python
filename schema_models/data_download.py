from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.defined_term import DefinedTerm
from schema_models.measurement_method_enum import MeasurementMethodEnum
from schema_models.media_object import MediaObject


class DataDownload(MediaObject):
    """
    All or part of a [[Dataset]] in downloadable form.
    """

    measurementMethod: Optional[
        Union[
            HttpUrl,
            List[HttpUrl],
            DefinedTerm,
            List[DefinedTerm],
            MeasurementMethodEnum,
            List[MeasurementMethodEnum],
            str,
            List[str],
        ]
    ] = None
    measurementTechnique: Optional[
        Union[
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
            DefinedTerm,
            List[DefinedTerm],
            MeasurementMethodEnum,
            List[MeasurementMethodEnum],
        ]
    ] = None
