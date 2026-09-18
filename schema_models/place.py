from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event
from schema_models.thing import Thing


@dataclass
class Place(Thing):
    """
    Entities that have a somewhat fixed, physical extension.
    """

    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    address: Optional[Union["PostalAddress", List["PostalAddress"], str, List[str]]] = (
        None
    )
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    branchCode: Optional[Union[str, List[str]]] = None
    containedIn: Optional[Union["Place", List["Place"]]] = None
    containedInPlace: Optional[Union["Place", List["Place"]]] = None
    containsPlace: Optional[Union["Place", List["Place"]]] = None
    event: Optional[Union[Event, List[Event]]] = None
    events: Optional[Union[Event, List[Event]]] = None
    faxNumber: Optional[Union[str, List[str]]] = None
    geo: Optional[
        Union["GeoCoordinates", List["GeoCoordinates"], "GeoShape", List["GeoShape"]]
    ] = None
    geoContains: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]
    ] = None
    geoCoveredBy: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]
    ] = None
    geoCovers: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]
    ] = None
    geoCrosses: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]
    ] = None
    geoDisjoint: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]
    ] = None
    geoEquals: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]
    ] = None
    geoIntersects: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]
    ] = None
    geoOverlaps: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]
    ] = None
    geoTouches: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]
    ] = None
    geoWithin: Optional[
        Union["GeospatialGeometry", List["GeospatialGeometry"], "Place", List["Place"]]
    ] = None
    globalLocationNumber: Optional[Union[str, List[str]]] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    hasDriveThroughService: Optional[Union[bool, List[bool]]] = None
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    hasMap: Optional[Union["Map", List["Map"], HttpUrl, List[HttpUrl]]] = None
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = None
    isicV4: Optional[Union[str, List[str]]] = None
    keywords: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    latitude: Optional[Union[float, List[float], str, List[str]]] = None
    logo: Optional[
        Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]
    ] = None
    longitude: Optional[Union[float, List[float], str, List[str]]] = None
    map: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    maps: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    maximumAttendeeCapacity: Optional[Union[int, List[int]]] = None
    openingHoursSpecification: Optional[
        Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]
    ] = None
    photo: Optional[
        Union["ImageObject", List["ImageObject"], "Photograph", List["Photograph"]]
    ] = None
    photos: Optional[
        Union["ImageObject", List["ImageObject"], "Photograph", List["Photograph"]]
    ] = None
    publicAccess: Optional[Union[bool, List[bool]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    reviews: Optional[Union["Review", List["Review"]]] = None
    slogan: Optional[Union[str, List[str]]] = None
    smokingAllowed: Optional[Union[bool, List[bool]]] = None
    specialOpeningHoursSpecification: Optional[
        Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]
    ] = None
    telephone: Optional[Union[str, List[str]]] = None
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = None
