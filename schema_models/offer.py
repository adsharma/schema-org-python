from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.event import Event
from schema_models.intangible import Intangible
from schema_models.member_program_tier import MemberProgramTier
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place
from schema_models.product import Product
from schema_models.thing import Thing
from schema_models.trip import Trip


class Offer(Intangible):
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    areaServed: Optional[Union[str, List[str]]] = None
    areaServed: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union["GeoShape", List["GeoShape"]]] = None
    areaServed: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    priceSpecification: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    gtin8: Optional[Union[str, List[str]]] = None
    gtin14: Optional[Union[str, List[str]]] = None
    hasMerchantReturnPolicy: Optional[
        Union["MerchantReturnPolicy", List["MerchantReturnPolicy"]]
    ] = None
    includesObject: Optional[
        Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]
    ] = None
    review: Optional[Union["Review", List["Review"]]] = None
    checkoutPageURLTemplate: Optional[Union[str, List[str]]] = None
    eligibleRegion: Optional[Union["GeoShape", List["GeoShape"]]] = None
    eligibleRegion: Optional[Union[str, List[str]]] = None
    eligibleRegion: Optional[Union[Place, List[Place]]] = None
    advanceBookingRequirement: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    leaseLength: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    leaseLength: Optional[Union["Duration", List["Duration"]]] = None
    eligibleCustomerType: Optional[
        Union["BusinessEntityType", List["BusinessEntityType"]]
    ] = None
    availableDeliveryMethod: Optional[
        Union["DeliveryMethod", List["DeliveryMethod"]]
    ] = None
    eligibleDuration: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    itemOffered: Optional[Union["MenuItem", List["MenuItem"]]] = None
    itemOffered: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    itemOffered: Optional[Union["Service", List["Service"]]] = None
    itemOffered: Optional[Union[Product, List[Product]]] = None
    itemOffered: Optional[Union[Trip, List[Trip]]] = None
    itemOffered: Optional[Union[Event, List[Event]]] = None
    itemOffered: Optional[Union["AggregateOffer", List["AggregateOffer"]]] = None
    shippingDetails: Optional[
        Union["OfferShippingDetails", List["OfferShippingDetails"]]
    ] = None
    eligibleTransactionVolume: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    validFrom: Optional[Union[datetime, List[datetime]]] = None
    validFrom: Optional[Union[date, List[date]]] = None
    deliveryLeadTime: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
    reviews: Optional[Union["Review", List["Review"]]] = None
    hasAdultConsideration: Optional[
        Union["AdultOrientedEnumeration", List["AdultOrientedEnumeration"]]
    ] = None
    itemCondition: Optional[Union["OfferItemCondition", List["OfferItemCondition"]]] = (
        None
    )
    hasMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    gtin13: Optional[Union[str, List[str]]] = None
    acceptedPaymentMethod: Optional[Union[str, List[str]]] = None
    acceptedPaymentMethod: Optional[Union["PaymentMethod", List["PaymentMethod"]]] = (
        None
    )
    acceptedPaymentMethod: Optional[Union["LoanOrCredit", List["LoanOrCredit"]]] = None
    seller: Optional[Union[Person, List[Person]]] = None
    seller: Optional[Union[Organization, List[Organization]]] = None
    availability: Optional[Union["ItemAvailability", List["ItemAvailability"]]] = None
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    mobileUrl: Optional[Union[str, List[str]]] = None
    sku: Optional[Union[str, List[str]]] = None
    gtin: Optional[Union[str, List[str]]] = None
    gtin: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    availabilityEnds: Optional[Union[datetime, List[datetime]]] = None
    availabilityEnds: Optional[Union[time, List[time]]] = None
    availabilityEnds: Optional[Union[date, List[date]]] = None
    validThrough: Optional[Union[datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date]]] = None
    asin: Optional[Union[str, List[str]]] = None
    asin: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    warranty: Optional[Union["WarrantyPromise", List["WarrantyPromise"]]] = None
    ineligibleRegion: Optional[Union[Place, List[Place]]] = None
    ineligibleRegion: Optional[Union[str, List[str]]] = None
    ineligibleRegion: Optional[Union["GeoShape", List["GeoShape"]]] = None
    mpn: Optional[Union[str, List[str]]] = None
    serialNumber: Optional[Union[str, List[str]]] = None
    offeredBy: Optional[Union[Person, List[Person]]] = None
    offeredBy: Optional[Union[Organization, List[Organization]]] = None
    availableAtOrFrom: Optional[Union[Place, List[Place]]] = None
    eligibleQuantity: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    price: Optional[Union[str, List[str]]] = None
    price: Optional[Union[float, List[float]]] = None
    gtin12: Optional[Union[str, List[str]]] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    addOn: Optional[Union["Offer", List["Offer"]]] = None
    businessFunction: Optional[Union["BusinessFunction", List["BusinessFunction"]]] = (
        None
    )
    availabilityStarts: Optional[Union[date, List[date]]] = None
    availabilityStarts: Optional[Union[time, List[time]]] = None
    availabilityStarts: Optional[Union[datetime, List[datetime]]] = None
    isFamilyFriendly: Optional[Union[bool, List[bool]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union["PhysicalActivityCategory", List["PhysicalActivityCategory"]]
    ] = None
    category: Optional[Union["CategoryCode", List["CategoryCode"]]] = None
    category: Optional[Union[str, List[str]]] = None
    category: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    priceValidUntil: Optional[Union[date, List[date]]] = None
