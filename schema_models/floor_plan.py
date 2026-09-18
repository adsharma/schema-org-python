from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


@dataclass
class FloorPlan(Intangible):
    """
    A FloorPlan is an explicit representation of a collection of similar accommodations, allowing the provision of common information (room counts, sizes, layout diagrams) and offers for rental or sale. In typical use, some [[ApartmentComplex]] has an [[accommodationFloorPlan]] which is a [[FloorPlan]].  A FloorPlan is always in the context of a particular place, either a larger [[ApartmentComplex]] or a single [[Apartment]]. The visual/spatial aspects of a floor plan (i.e. room layout, [see wikipedia](https://en.wikipedia.org/wiki/Floor_plan)) can be indicated using [[image]].
    """

    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    floorSize: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    isPlanForApartment: Optional[Union["Accommodation", List["Accommodation"]]] = None
    layoutImage: Optional[
        Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]
    ] = None
    numberOfAccommodationUnits: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    numberOfAvailableAccommodationUnits: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    numberOfBathroomsTotal: Optional[Union[int, List[int]]] = None
    numberOfBedrooms: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    numberOfFullBathrooms: Optional[Union[float, List[float]]] = None
    numberOfPartialBathrooms: Optional[Union[float, List[float]]] = None
    numberOfRooms: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    petsAllowed: Optional[Union[bool, List[bool], str, List[str]]] = None
