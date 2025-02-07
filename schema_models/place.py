from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.event import Event
from schema_models.integer import Integer
from schema_models.number import Number
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class Place(Thing):
    geoCrosses: Optional[Union["Place", List["Place"]]] = None
    geoCrosses: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    branchCode: Optional[Union[Text, List[Text]]] = None
    containedInPlace: Optional[Union["Place", List["Place"]]] = None
    logo: Optional[Union[URL, List[URL]]] = None
    logo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    geoCovers: Optional[Union["Place", List["Place"]]] = None
    geoCovers: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    keywords: Optional[Union[URL, List[URL]]] = None
    keywords: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    keywords: Optional[Union[Text, List[Text]]] = None
    containsPlace: Optional[Union["Place", List["Place"]]] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    reviews: Optional[Union["Review", List["Review"]]] = None
    map: Optional[Union[URL, List[URL]]] = None
    geoEquals: Optional[Union["Place", List["Place"]]] = None
    geoEquals: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    events: Optional[Union[Event, List[Event]]] = None
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    isicV4: Optional[Union[Text, List[Text]]] = None
    tourBookingPage: Optional[Union[URL, List[URL]]] = None
    isAccessibleForFree: Optional[Union[Boolean, List[Boolean]]] = None
    maps: Optional[Union[URL, List[URL]]] = None
    containedIn: Optional[Union["Place", List["Place"]]] = None
    specialOpeningHoursSpecification: Optional[
        Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]
    ] = None
    geo: Optional[Union["GeoCoordinates", List["GeoCoordinates"]]] = None
    geo: Optional[Union["GeoShape", List["GeoShape"]]] = None
    slogan: Optional[Union[Text, List[Text]]] = None
    hasMap: Optional[Union["Map", List["Map"]]] = None
    hasMap: Optional[Union[URL, List[URL]]] = None
    telephone: Optional[Union[Text, List[Text]]] = None
    photo: Optional[Union["Photograph", List["Photograph"]]] = None
    photo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    faxNumber: Optional[Union[Text, List[Text]]] = None
    globalLocationNumber: Optional[Union[Text, List[Text]]] = None
    geoTouches: Optional[Union["Place", List["Place"]]] = None
    geoTouches: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    geoOverlaps: Optional[Union["Place", List["Place"]]] = None
    geoOverlaps: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    maximumAttendeeCapacity: Optional[Union[Integer, List[Integer]]] = None
    geoCoveredBy: Optional[Union["Place", List["Place"]]] = None
    geoCoveredBy: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    event: Optional[Union[Event, List[Event]]] = None
    geoDisjoint: Optional[Union["Place", List["Place"]]] = None
    geoDisjoint: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    publicAccess: Optional[Union[Boolean, List[Boolean]]] = None
    address: Optional[Union[Text, List[Text]]] = None
    address: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    longitude: Optional[Union[Number, List[Number]]] = None
    longitude: Optional[Union[Text, List[Text]]] = None
    geoContains: Optional[Union["Place", List["Place"]]] = None
    geoContains: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    hasGS1DigitalLink: Optional[Union[URL, List[URL]]] = None
    photos: Optional[Union["Photograph", List["Photograph"]]] = None
    photos: Optional[Union["ImageObject", List["ImageObject"]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    geoWithin: Optional[Union["Place", List["Place"]]] = None
    geoWithin: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = None
    latitude: Optional[Union[Text, List[Text]]] = None
    latitude: Optional[Union[Number, List[Number]]] = None
    geoIntersects: Optional[Union["Place", List["Place"]]] = None
    geoIntersects: Optional[Union["GeospatialGeometry", List["GeospatialGeometry"]]] = (
        None
    )
    review: Optional[Union["Review", List["Review"]]] = None
    hasDriveThroughService: Optional[Union[Boolean, List[Boolean]]] = None
    openingHoursSpecification: Optional[
        Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]
    ] = None
    smokingAllowed: Optional[Union[Boolean, List[Boolean]]] = None
