from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.administrative_area import AdministrativeArea
from schema_models.adult_oriented_enumeration import AdultOrientedEnumeration
from schema_models.aggregate_offer import AggregateOffer
from schema_models.aggregate_rating import AggregateRating
from schema_models.boolean import Boolean
from schema_models.business_entity_type import BusinessEntityType
from schema_models.business_function import BusinessFunction
from schema_models.category_code import CategoryCode
from schema_models.creative_work import CreativeWork
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.delivery_method import DeliveryMethod
from schema_models.duration import Duration
from schema_models.event import Event
from schema_models.geo_shape import GeoShape
from schema_models.intangible import Intangible
from schema_models.item_availability import ItemAvailability
from schema_models.loan_or_credit import LoanOrCredit
from schema_models.member_program_tier import MemberProgramTier
from schema_models.menu_item import MenuItem
from schema_models.merchant_return_policy import MerchantReturnPolicy
from schema_models.number import Number
from schema_models.offer import Offer
from schema_models.offer_item_condition import OfferItemCondition
from schema_models.offer_shipping_details import OfferShippingDetails
from schema_models.organization import Organization
from schema_models.payment_method import PaymentMethod
from schema_models.person import Person
from schema_models.physical_activity_category import PhysicalActivityCategory
from schema_models.place import Place
from schema_models.price_specification import PriceSpecification
from schema_models.product import Product
from schema_models.property_value import PropertyValue
from schema_models.quantitative_value import QuantitativeValue
from schema_models.review import Review
from schema_models.service import Service
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.time import Time
from schema_models.trip import Trip
from schema_models.type_and_quantity_node import TypeAndQuantityNode
from schema_models.url import URL
from schema_models.warranty_promise import WarrantyPromise


class Offer(Intangible):
    hasGS1DigitalLink: Optional[Union[URL, List[URL]]] = None
    areaServed: Optional[Union[Text, List[Text]]] = None
    areaServed: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union[GeoShape, List[GeoShape]]] = None
    areaServed: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    aggregateRating: Optional[Union[AggregateRating, List[AggregateRating]]] = None
    priceSpecification: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = None
    gtin8: Optional[Union[Text, List[Text]]] = None
    gtin14: Optional[Union[Text, List[Text]]] = None
    hasMerchantReturnPolicy: Optional[
        Union[MerchantReturnPolicy, List[MerchantReturnPolicy]]
    ] = None
    includesObject: Optional[Union[TypeAndQuantityNode, List[TypeAndQuantityNode]]] = (
        None
    )
    review: Optional[Union[Review, List[Review]]] = None
    checkoutPageURLTemplate: Optional[Union[Text, List[Text]]] = None
    eligibleRegion: Optional[Union[GeoShape, List[GeoShape]]] = None
    eligibleRegion: Optional[Union[Text, List[Text]]] = None
    eligibleRegion: Optional[Union[Place, List[Place]]] = None
    advanceBookingRequirement: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    leaseLength: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    leaseLength: Optional[Union[Duration, List[Duration]]] = None
    eligibleCustomerType: Optional[
        Union[BusinessEntityType, List[BusinessEntityType]]
    ] = None
    availableDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = (
        None
    )
    eligibleDuration: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    itemOffered: Optional[Union[MenuItem, List[MenuItem]]] = None
    itemOffered: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    itemOffered: Optional[Union[Service, List[Service]]] = None
    itemOffered: Optional[Union[Product, List[Product]]] = None
    itemOffered: Optional[Union[Trip, List[Trip]]] = None
    itemOffered: Optional[Union[Event, List[Event]]] = None
    itemOffered: Optional[Union[AggregateOffer, List[AggregateOffer]]] = None
    shippingDetails: Optional[
        Union[OfferShippingDetails, List[OfferShippingDetails]]
    ] = None
    eligibleTransactionVolume: Optional[
        Union[PriceSpecification, List[PriceSpecification]]
    ] = None
    validFrom: Optional[Union[DateTime, List[DateTime]]] = None
    validFrom: Optional[Union[Date, List[Date]]] = None
    deliveryLeadTime: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
    reviews: Optional[Union[Review, List[Review]]] = None
    hasAdultConsideration: Optional[
        Union[AdultOrientedEnumeration, List[AdultOrientedEnumeration]]
    ] = None
    itemCondition: Optional[Union[OfferItemCondition, List[OfferItemCondition]]] = None
    hasMeasurement: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    gtin13: Optional[Union[Text, List[Text]]] = None
    acceptedPaymentMethod: Optional[Union[Text, List[Text]]] = None
    acceptedPaymentMethod: Optional[Union[PaymentMethod, List[PaymentMethod]]] = None
    acceptedPaymentMethod: Optional[Union[LoanOrCredit, List[LoanOrCredit]]] = None
    seller: Optional[Union[Person, List[Person]]] = None
    seller: Optional[Union[Organization, List[Organization]]] = None
    availability: Optional[Union[ItemAvailability, List[ItemAvailability]]] = None
    additionalProperty: Optional[Union[PropertyValue, List[PropertyValue]]] = None
    mobileUrl: Optional[Union[Text, List[Text]]] = None
    sku: Optional[Union[Text, List[Text]]] = None
    gtin: Optional[Union[Text, List[Text]]] = None
    gtin: Optional[Union[URL, List[URL]]] = None
    inventoryLevel: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    availabilityEnds: Optional[Union[DateTime, List[DateTime]]] = None
    availabilityEnds: Optional[Union[Time, List[Time]]] = None
    availabilityEnds: Optional[Union[Date, List[Date]]] = None
    validThrough: Optional[Union[DateTime, List[DateTime]]] = None
    validThrough: Optional[Union[Date, List[Date]]] = None
    asin: Optional[Union[Text, List[Text]]] = None
    asin: Optional[Union[URL, List[URL]]] = None
    warranty: Optional[Union[WarrantyPromise, List[WarrantyPromise]]] = None
    ineligibleRegion: Optional[Union[Place, List[Place]]] = None
    ineligibleRegion: Optional[Union[Text, List[Text]]] = None
    ineligibleRegion: Optional[Union[GeoShape, List[GeoShape]]] = None
    mpn: Optional[Union[Text, List[Text]]] = None
    serialNumber: Optional[Union[Text, List[Text]]] = None
    offeredBy: Optional[Union[Person, List[Person]]] = None
    offeredBy: Optional[Union[Organization, List[Organization]]] = None
    availableAtOrFrom: Optional[Union[Place, List[Place]]] = None
    eligibleQuantity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    price: Optional[Union[Text, List[Text]]] = None
    price: Optional[Union[Number, List[Number]]] = None
    gtin12: Optional[Union[Text, List[Text]]] = None
    priceCurrency: Optional[Union[Text, List[Text]]] = None
    addOn: Optional[Union["Offer", List["Offer"]]] = None
    businessFunction: Optional[Union[BusinessFunction, List[BusinessFunction]]] = None
    availabilityStarts: Optional[Union[Date, List[Date]]] = None
    availabilityStarts: Optional[Union[Time, List[Time]]] = None
    availabilityStarts: Optional[Union[DateTime, List[DateTime]]] = None
    isFamilyFriendly: Optional[Union[Boolean, List[Boolean]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union[PhysicalActivityCategory, List[PhysicalActivityCategory]]
    ] = None
    category: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    category: Optional[Union[Text, List[Text]]] = None
    category: Optional[Union[URL, List[URL]]] = None
    priceValidUntil: Optional[Union[Date, List[Date]]] = None
