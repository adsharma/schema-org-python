from dataclasses import dataclass
from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration
from schema_models.event import Event
from schema_models.intangible import Intangible
from schema_models.member_program_tier import MemberProgramTier
from schema_models.menu_item import MenuItem
from schema_models.merchant_return_policy import MerchantReturnPolicy
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place
from schema_models.product import Product
from schema_models.review import Review
from schema_models.thing import Thing


@dataclass
class Offer(Intangible):
    """
    An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.

    Note: As the [[businessFunction]] property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.

    For [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator) and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide) from [GS1](http://www.gs1.org/).
    """

    acceptedPaymentMethod: Optional[
        Union[
            "LoanOrCredit",
            List["LoanOrCredit"],
            "PaymentMethod",
            List["PaymentMethod"],
            str,
            List[str],
        ]
    ] = None
    addOn: Optional[Union["Offer", List["Offer"]]] = None
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    advanceBookingRequirement: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    areaServed: Optional[
        Union[
            "AdministrativeArea",
            List["AdministrativeArea"],
            "GeoShape",
            List["GeoShape"],
            Place,
            List[Place],
            str,
            List[str],
        ]
    ] = None
    asin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    availability: Optional[Union["ItemAvailability", List["ItemAvailability"]]] = None
    availabilityEnds: Optional[
        Union[date, List[date], datetime, List[datetime], time, List[time]]
    ] = None
    availabilityStarts: Optional[
        Union[date, List[date], datetime, List[datetime], time, List[time]]
    ] = None
    availableAtOrFrom: Optional[Union[Place, List[Place]]] = None
    availableDeliveryMethod: Optional[
        Union["DeliveryMethod", List["DeliveryMethod"]]
    ] = None
    businessFunction: Optional[Union["BusinessFunction", List["BusinessFunction"]]] = (
        None
    )
    category: Optional[
        Union[
            "CategoryCode",
            List["CategoryCode"],
            "PhysicalActivityCategory",
            List["PhysicalActivityCategory"],
            str,
            List[str],
            Thing,
            List[Thing],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    checkoutPageURLTemplate: Optional[Union[str, List[str]]] = None
    deliveryLeadTime: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    eligibleCustomerType: Optional[
        Union["BusinessEntityType", List["BusinessEntityType"]]
    ] = None
    eligibleDuration: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    eligibleQuantity: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    eligibleRegion: Optional[
        Union["GeoShape", List["GeoShape"], Place, List[Place], str, List[str]]
    ] = None
    eligibleTransactionVolume: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    gtin12: Optional[Union[str, List[str]]] = None
    gtin13: Optional[Union[str, List[str]]] = None
    gtin14: Optional[Union[str, List[str]]] = None
    gtin8: Optional[Union[str, List[str]]] = None
    gtin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    hasAdultConsideration: Optional[
        Union["AdultOrientedEnumeration", List["AdultOrientedEnumeration"]]
    ] = None
    hasDigitalProductPassport: Optional[
        Union[
            "DigitalProductPassport",
            List["DigitalProductPassport"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    hasMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    hasMerchantReturnPolicy: Optional[
        Union[MerchantReturnPolicy, List[MerchantReturnPolicy]]
    ] = None
    includesObject: Optional[
        Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]
    ] = None
    ineligibleRegion: Optional[
        Union["GeoShape", List["GeoShape"], Place, List[Place], str, List[str]]
    ] = None
    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    isFamilyFriendly: Optional[Union[bool, List[bool]]] = None
    itemCondition: Optional[Union["OfferItemCondition", List["OfferItemCondition"]]] = (
        None
    )
    itemOffered: Optional[
        Union[
            "AggregateOffer",
            List["AggregateOffer"],
            CreativeWork,
            List[CreativeWork],
            Event,
            List[Event],
            MenuItem,
            List[MenuItem],
            Product,
            List[Product],
            "Service",
            List["Service"],
            "Trip",
            List["Trip"],
        ]
    ] = None
    itemPopularity: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    leaseLength: Optional[
        Union[Duration, List[Duration], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    mobileUrl: Optional[Union[str, List[str]]] = None
    mpn: Optional[Union[str, List[str]]] = None
    offeredBy: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    price: Optional[Union[float, List[float], str, List[str]]] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    priceSpecification: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    priceValidUntil: Optional[Union[date, List[date]]] = None
    review: Optional[Union[Review, List[Review]]] = None
    reviews: Optional[Union[Review, List[Review]]] = None
    seller: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    serialNumber: Optional[Union[str, List[str]]] = None
    shippingDetails: Optional[
        Union["OfferShippingDetails", List["OfferShippingDetails"]]
    ] = None
    sku: Optional[Union[str, List[str]]] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    warranty: Optional[Union["WarrantyPromise", List["WarrantyPromise"]]] = None
