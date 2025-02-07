from typing import List, Optional, Union

from schema_models.intangible import Intangible
from schema_models.place import Place


class GeospatialGeometry(Intangible):
    geoCrosses: Optional[Union[Place, List[Place]]] = None
    geoCrosses: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    geoCovers: Optional[Union[Place, List[Place]]] = None
    geoCovers: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    geoEquals: Optional[Union[Place, List[Place]]] = None
    geoEquals: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    geoTouches: Optional[Union[Place, List[Place]]] = None
    geoTouches: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    geoOverlaps: Optional[Union[Place, List[Place]]] = None
    geoOverlaps: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    geoCoveredBy: Optional[Union[Place, List[Place]]] = None
    geoCoveredBy: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    geoDisjoint: Optional[Union[Place, List[Place]]] = None
    geoDisjoint: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    geoContains: Optional[Union[Place, List[Place]]] = None
    geoContains: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    geoWithin: Optional[Union[Place, List[Place]]] = None
    geoWithin: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    geoIntersects: Optional[Union[Place, List[Place]]] = None
    geoIntersects: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
