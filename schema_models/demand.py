from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.administrative_area import AdministrativeArea
from schema_models.aggregate_offer import AggregateOffer
from schema_models.business_entity_type import BusinessEntityType
from schema_models.business_function import BusinessFunction
from schema_models.creative_work import CreativeWork
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.delivery_method import DeliveryMethod
from schema_models.event import Event
from schema_models.geo_shape import GeoShape
from schema_models.intangible import Intangible
from schema_models.item_availability import ItemAvailability
from schema_models.loan_or_credit import LoanOrCredit
from schema_models.menu_item import MenuItem
from schema_models.offer_item_condition import OfferItemCondition
from schema_models.organization import Organization
from schema_models.payment_method import PaymentMethod
from schema_models.person import Person
from schema_models.place import Place
from schema_models.price_specification import PriceSpecification
from schema_models.product import Product
from schema_models.quantitative_value import QuantitativeValue
from schema_models.service import Service
from schema_models.text import Text
from schema_models.time import Time
from schema_models.trip import Trip
from schema_models.type_and_quantity_node import TypeAndQuantityNode
from schema_models.url import URL
from schema_models.warranty_promise import WarrantyPromise


class Demand(Intangible):
    gtin14: Optional[Union[Text, List[Text]]] = None
    gtin12: Optional[Union[Text, List[Text]]] = None
    businessFunction: Optional[Union[BusinessFunction, List[BusinessFunction]]] = None
    eligibleRegion: Optional[Union[GeoShape, List[GeoShape]]] = None
    eligibleRegion: Optional[Union[Text, List[Text]]] = None
    eligibleRegion: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union[Text, List[Text]]] = None
    areaServed: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union[GeoShape, List[GeoShape]]] = None
    areaServed: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    priceSpecification: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = None
    advanceBookingRequirement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    gtin8: Optional[Union[Text, List[Text]]] = None
    availableDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = (
        None
    )
    includesObject: Optional[Union[TypeAndQuantityNode, List[TypeAndQuantityNode]]] = (
        None
    )
    eligibleTransactionVolume: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = None
    deliveryLeadTime: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    eligibleCustomerType: Optional[
        Union[BusinessEntityType, List[BusinessEntityType]]
    ] = None
    seller: Optional[Union[Person, List[Person]]] = None
    seller: Optional[Union[Organization, List[Organization]]] = None
    eligibleDuration: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    itemOffered: Optional[Union[MenuItem, List[MenuItem]]] = None
    itemOffered: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    itemOffered: Optional[Union[Service, List[Service]]] = None
    itemOffered: Optional[Union[Product, List[Product]]] = None
    itemOffered: Optional[Union[Trip, List[Trip]]] = None
    itemOffered: Optional[Union[Event, List[Event]]] = None
    itemOffered: Optional[Union[AggregateOffer, List[AggregateOffer]]] = None
    availability: Optional[Union[ItemAvailability, List[ItemAvailability]]] = None
    validFrom: Optional[Union[DateTime, List[DateTime]]] = None
    validFrom: Optional[Union[Date, List[Date]]] = None
    itemCondition: Optional[Union[OfferItemCondition, List[OfferItemCondition]]] = None
    inventoryLevel: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    validThrough: Optional[Union[DateTime, List[DateTime]]] = None
    validThrough: Optional[Union[Date, List[Date]]] = None
    gtin13: Optional[Union[Text, List[Text]]] = None
    acceptedPaymentMethod: Optional[Union[Text, List[Text]]] = None
    acceptedPaymentMethod: Optional[Union[PaymentMethod, List[PaymentMethod]]] = None
    acceptedPaymentMethod: Optional[Union[LoanOrCredit, List[LoanOrCredit]]] = None
    asin: Optional[Union[Text, List[Text]]] = None
    asin: Optional[Union[URL, List[URL]]] = None
    serialNumber: Optional[Union[Text, List[Text]]] = None
    sku: Optional[Union[Text, List[Text]]] = None
    gtin: Optional[Union[Text, List[Text]]] = None
    gtin: Optional[Union[URL, List[URL]]] = None
    availabilityEnds: Optional[Union[DateTime, List[DateTime]]] = None
    availabilityEnds: Optional[Union[Time, List[Time]]] = None
    availabilityEnds: Optional[Union[Date, List[Date]]] = None
    availabilityStarts: Optional[Union[Date, List[Date]]] = None
    availabilityStarts: Optional[Union[Time, List[Time]]] = None
    availabilityStarts: Optional[Union[DateTime, List[DateTime]]] = None
    warranty: Optional[Union[WarrantyPromise, List[WarrantyPromise]]] = None
    ineligibleRegion: Optional[Union[Place, List[Place]]] = None
    ineligibleRegion: Optional[Union[Text, List[Text]]] = None
    ineligibleRegion: Optional[Union[GeoShape, List[GeoShape]]] = None
    mpn: Optional[Union[Text, List[Text]]] = None
    availableAtOrFrom: Optional[Union[Place, List[Place]]] = None
    eligibleQuantity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
