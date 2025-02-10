from typing import List, Optional, Union

from schema_models.distance import Distance
from schema_models.geo_coordinates import GeoCoordinates
from schema_models.geo_shape import GeoShape


class GeoCircle(GeoShape):
    """
    A GeoCircle is a GeoShape representing a circular geographic area. As it is a GeoShape
              it provides the simple textual property 'circle', but also allows the combination of postalCode alongside geoRadius.
              The center of the circle can be indicated via the 'geoMidpoint' property, or more approximately using 'address', 'postalCode'.

    """

    geoMidpoint: Optional[Union[GeoCoordinates, List[GeoCoordinates]]] = None
    geoRadius: Optional[Union[Distance, List[Distance]]] = None
    geoRadius: Optional[Union[float, List[float]]] = None
    geoRadius: Optional[Union[str, List[str]]] = None
