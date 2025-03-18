from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.place import Place


class GeospatialGeometry(Intangible):
    """
    (Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions from Geo-Spatial best practices.
    """

    geoCrosses: Optional[
        Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]
    ] = None
    geoCovers: Optional[
        Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]
    ] = None
    geoEquals: Optional[
        Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]
    ] = None
    geoTouches: Optional[
        Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]
    ] = None
    geoOverlaps: Optional[
        Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]
    ] = None
    geoCoveredBy: Optional[
        Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]
    ] = None
    geoDisjoint: Optional[
        Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]
    ] = None
    geoContains: Optional[
        Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]
    ] = None
    geoWithin: Optional[
        Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]
    ] = None
    geoIntersects: Optional[
        Union[Place, List[Place], "GeospatialGeometry", List["GeospatialGeometry"]]
    ] = None
