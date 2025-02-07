from typing import List, Optional, Union

from schema_models.bed_details import BedDetails
from schema_models.boolean import Boolean
from schema_models.floor_plan import FloorPlan
from schema_models.integer import Integer
from schema_models.number import Number
from schema_models.place import Place
from schema_models.text import Text
from schema_models.url import URL


class Accommodation(Place):
    numberOfBathroomsTotal: Optional[Union[Integer, List[Integer]]] = None
    accommodationCategory: Optional[Union[Text, List[Text]]] = None
    floorLevel: Optional[Union[Text, List[Text]]] = None
    bed: Optional[Union["BedType", List["BedType"]]] = None
    bed: Optional[Union[BedDetails, List[BedDetails]]] = None
    bed: Optional[Union[Text, List[Text]]] = None
    numberOfBedrooms: Optional[Union[Number, List[Number]]] = None
    numberOfBedrooms: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    leaseLength: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    leaseLength: Optional[Union["Duration", List["Duration"]]] = None
    numberOfFullBathrooms: Optional[Union[Number, List[Number]]] = None
    floorSize: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    yearBuilt: Optional[Union[Number, List[Number]]] = None
    numberOfRooms: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    numberOfRooms: Optional[Union[Number, List[Number]]] = None
    petsAllowed: Optional[Union[Text, List[Text]]] = None
    petsAllowed: Optional[Union[Boolean, List[Boolean]]] = None
    accommodationFloorPlan: Optional[Union[FloorPlan, List[FloorPlan]]] = None
    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    occupancy: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    permittedUsage: Optional[Union[Text, List[Text]]] = None
    tourBookingPage: Optional[Union[URL, List[URL]]] = None
    numberOfPartialBathrooms: Optional[Union[Number, List[Number]]] = None
