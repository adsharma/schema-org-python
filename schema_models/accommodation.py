from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.bed_details import BedDetails
from schema_models.floor_plan import FloorPlan
from schema_models.place import Place


class Accommodation(Place):
    """
    An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting room. Many accommodations are for overnight stays, but this is not a mandatory requirement.
    For more specific types of accommodations not defined in schema.org, one can use [[additionalType]] with external vocabularies.
    <br /><br />
    See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    """

    numberOfBathroomsTotal: Optional[Union[int, List[int]]] = None
    accommodationCategory: Optional[Union[str, List[str]]] = None
    floorLevel: Optional[Union[str, List[str]]] = None
    bed: Optional[
        Union["BedType", List["BedType"], BedDetails, List[BedDetails], str, List[str]]
    ] = None
    numberOfBedrooms: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    leaseLength: Optional[
        Union[
            "QuantitativeValue", List["QuantitativeValue"], "Duration", List["Duration"]
        ]
    ] = None
    numberOfFullBathrooms: Optional[Union[float, List[float]]] = None
    floorSize: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    yearBuilt: Optional[Union[float, List[float]]] = None
    numberOfRooms: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], float, List[float]]
    ] = None
    petsAllowed: Optional[Union[str, List[str], bool, List[bool]]] = None
    accommodationFloorPlan: Optional[Union[FloorPlan, List[FloorPlan]]] = None
    amenityFeature: Optional[
        Union["LocationFeatureSpecification", List["LocationFeatureSpecification"]]
    ] = None
    occupancy: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    permittedUsage: Optional[Union[str, List[str]]] = None
    tourBookingPage: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    numberOfPartialBathrooms: Optional[Union[float, List[float]]] = None
