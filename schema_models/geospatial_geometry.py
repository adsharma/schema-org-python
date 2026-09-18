from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.place import Place


@dataclass
class GeospatialGeometry(Intangible):
    """
    (Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions from Geo-Spatial best practices.
    """

    geoContains: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]
    ] = None
    geoCoveredBy: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]
    ] = None
    geoCovers: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]
    ] = None
    geoCrosses: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]
    ] = None
    geoDisjoint: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]
    ] = None
    geoEquals: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]
    ] = None
    geoIntersects: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]
    ] = None
    geoOverlaps: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]
    ] = None
    geoTouches: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]
    ] = None
    geoWithin: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], Place, List[Place]]
    ] = None
