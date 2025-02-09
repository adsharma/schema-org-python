from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.bed_details import BedDetails
from schema_models.floor_plan import FloorPlan
from schema_models.place import Place


class Accommodation(Place):
    numberOfBathroomsTotal: Optional[Union[int, List[int]]] = None
    accommodationCategory: Optional[Union[str, List[str]]] = None
    floorLevel: Optional[Union[str, List[str]]] = None
    bed: Optional[Union["BedType", List["BedType"]]] = None
    bed: Optional[Union[BedDetails, List[BedDetails]]] = None
    bed: Optional[Union[str, List[str]]] = None
    numberOfBedrooms: Optional[Union[float, List[float]]] = None
    numberOfBedrooms: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    leaseLength: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    leaseLength: Optional[Union["Duration", List["Duration"]]] = None
    numberOfFullBathrooms: Optional[Union[float, List[float]]] = None
    floorSize: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    yearBuilt: Optional[Union[float, List[float]]] = None
    numberOfRooms: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    numberOfRooms: Optional[Union[float, List[float]]] = None
    petsAllowed: Optional[Union[str, List[str]]] = None
    petsAllowed: Optional[Union[bool, List[bool]]] = None
    accommodationFloorPlan: Optional[Union[FloorPlan, List[FloorPlan]]] = None
    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    occupancy: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    permittedUsage: Optional[Union[str, List[str]]] = None
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    numberOfPartialBathrooms: Optional[Union[float, List[float]]] = None
