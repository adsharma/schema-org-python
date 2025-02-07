from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.distance import Distance
from schema_models.geo_coordinates import GeoCoordinates
from schema_models.geo_shape import GeoShape
from schema_models.number import Number
from schema_models.text import Text


class GeoCircle(GeoShape):
    geoMidpoint: Optional[Union[GeoCoordinates, List[GeoCoordinates]]] = None
    geoRadius: Optional[Union[Distance, List[Distance]]] = None
    geoRadius: Optional[Union[Number, List[Number]]] = None
    geoRadius: Optional[Union[Text, List[Text]]] = None
