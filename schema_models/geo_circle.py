from typing import List, Optional, Union

from schema_models.distance import Distance
from schema_models.geo_coordinates import GeoCoordinates
from schema_models.geo_shape import GeoShape


class GeoCircle(GeoShape):
    geoMidpoint: Optional[Union[GeoCoordinates, List[GeoCoordinates]]] = None
    geoRadius: Optional[Union[Distance, List[Distance]]] = None
    geoRadius: Optional[Union[float, List[float]]] = None
    geoRadius: Optional[Union[str, List[str]]] = None
