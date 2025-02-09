from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class FloorPlan(Intangible):
    floorSize: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    numberOfRooms: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    numberOfRooms: Optional[Union[float, List[float]]] = None
    petsAllowed: Optional[Union[str, List[str]]] = None
    petsAllowed: Optional[Union[bool, List[bool]]] = None
    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    layoutImage: Optional[Union["ImageObject", List["ImageObject"]]] = None
    layoutImage: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    numberOfPartialBathrooms: Optional[Union[float, List[float]]] = None
    numberOfAvailableAccommodationUnits: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    numberOfBathroomsTotal: Optional[Union[int, List[int]]] = None
    numberOfAccommodationUnits: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    numberOfFullBathrooms: Optional[Union[float, List[float]]] = None
    numberOfBedrooms: Optional[Union[float, List[float]]] = None
    numberOfBedrooms: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    isPlanForApartment: Optional[Union["Accommodation", List["Accommodation"]]] = None
