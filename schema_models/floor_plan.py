from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.accommodation import Accommodation
from schema_models.boolean import Boolean
from schema_models.image_object import ImageObject
from schema_models.intangible import Intangible
from schema_models.integer import Integer
from schema_models.location_feature_specification import LocationFeatureSpecification
from schema_models.number import Number
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text
from schema_models.url import URL


class FloorPlan(Intangible):
    floorSize: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfRooms: Optional[Union[Number, List[Number]]] = None
    petsAllowed: Optional[Union[Text, List[Text]]] = None
    petsAllowed: Optional[Union[Boolean, List[Boolean]]] = None
    amenityFeature: Optional[
        Union[LocationFeatureSpecification, List[LocationFeatureSpecification]]
    ] = None
    layoutImage: Optional[Union[ImageObject, List[ImageObject]]] = None
    layoutImage: Optional[Union[URL, List[URL]]] = None
    numberOfPartialBathrooms: Optional[Union[Number, List[Number]]] = None
    numberOfAvailableAccommodationUnits: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    numberOfBathroomsTotal: Optional[Union[Integer, List[Integer]]] = None
    numberOfAccommodationUnits: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    numberOfFullBathrooms: Optional[Union[Number, List[Number]]] = None
    numberOfBedrooms: Optional[Union[Number, List[Number]]] = None
    numberOfBedrooms: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    isPlanForApartment: Optional[Union[Accommodation, List[Accommodation]]] = None
