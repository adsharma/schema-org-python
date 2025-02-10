from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event
from schema_models.thing import Thing


class Place(Thing):
    """
    Entities that have a somewhat fixed, physical extension.
    """

    geoCrosses: Optional[Union["Place", List["Place"]]] = None
    geoCrosses: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    branchCode: Optional[Union[str, List[str]]] = None
    containedInPlace: Optional[Union["Place", List["Place"]]] = None
    logo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    logo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    geoCovers: Optional[Union["Place", List["Place"]]] = None
    geoCovers: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    keywords: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    keywords: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    keywords: Optional[Union[str, List[str]]] = None
    containsPlace: Optional[Union["Place", List["Place"]]] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    reviews: Optional[Union["Review", List["Review"]]] = None
    map: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    geoEquals: Optional[Union["Place", List["Place"]]] = None
    geoEquals: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    events: Optional[Union[Event, List[Event]]] = None
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    isicV4: Optional[Union[str, List[str]]] = None
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = None
    maps: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    containedIn: Optional[Union["Place", List["Place"]]] = None
    specialOpeningHoursSpecification: Optional[
        Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]
    ] = None
    geo: Optional[Union["GeoCoordinates", List["GeoCoordinates"]]] = None
    geo: Optional[Union["GeoShape", List["GeoShape"]]] = None
    slogan: Optional[Union[str, List[str]]] = None
    hasMap: Optional[Union["Map", List["Map"]]] = None
    hasMap: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    telephone: Optional[Union[str, List[str]]] = None
    photo: Optional[Union["Photograph", List["Photograph"]]] = None
    photo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    faxNumber: Optional[Union[str, List[str]]] = None
    globalLocationNumber: Optional[Union[str, List[str]]] = None
    geoTouches: Optional[Union["Place", List["Place"]]] = None
    geoTouches: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    geoOverlaps: Optional[Union["Place", List["Place"]]] = None
    geoOverlaps: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    maximumAttendeeCapacity: Optional[Union[int, List[int]]] = None
    geoCoveredBy: Optional[Union["Place", List["Place"]]] = None
    geoCoveredBy: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    event: Optional[Union[Event, List[Event]]] = None
    geoDisjoint: Optional[Union["Place", List["Place"]]] = None
    geoDisjoint: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    publicAccess: Optional[Union[bool, List[bool]]] = None
    address: Optional[Union[str, List[str]]] = None
    address: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    longitude: Optional[Union[float, List[float]]] = None
    longitude: Optional[Union[str, List[str]]] = None
    geoContains: Optional[Union["Place", List["Place"]]] = None
    geoContains: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    photos: Optional[Union["Photograph", List["Photograph"]]] = None
    photos: Optional[Union["ImageObject", List["ImageObject"]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    geoWithin: Optional[Union["Place", List["Place"]]] = None
    geoWithin: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    latitude: Optional[Union[str, List[str]]] = None
    latitude: Optional[Union[float, List[float]]] = None
    geoIntersects: Optional[Union["Place", List["Place"]]] = None
    geoIntersects: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    review: Optional[Union["Review", List["Review"]]] = None
    hasDriveThroughService: Optional[Union[bool, List[bool]]] = None
    openingHoursSpecification: Optional[
        Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]
    ] = None
    smokingAllowed: Optional[Union[bool, List[bool]]] = None
