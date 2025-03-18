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
    """
    An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.

    Note: As the [[businessFunction]] property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.

    For [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator) and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide) from [GS1](http://www.gs1.org/).
    """

    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    areaServed: Optional[
        Union[
            str,
            List[str],
            Place,
            List[Place],
            "GeoShape",
            List["GeoShape"],
            "AdministrativeArea",
            List["AdministrativeArea"],
        ]
    ] = None
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
    eligibleRegion: Optional[
        Union["GeoShape", List["GeoShape"], str, List[str], Place, List[Place]]
    ] = None
    advanceBookingRequirement: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    leaseLength: Optional[
        Union[
            "QuantitativeValue", List["QuantitativeValue"], "Duration", List["Duration"]
        ]
    ] = None
    eligibleCustomerType: Optional[
        Union["BusinessEntityType", List["BusinessEntityType"]]
    ] = None
    availableDeliveryMethod: Optional[
        Union["DeliveryMethod", List["DeliveryMethod"]]
    ] = None
    eligibleDuration: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    itemOffered: Optional[
        Union[
            "MenuItem",
            List["MenuItem"],
            CreativeWork,
            List[CreativeWork],
            "Service",
            List["Service"],
            Product,
            List[Product],
            Trip,
            List[Trip],
            Event,
            List[Event],
            "AggregateOffer",
            List["AggregateOffer"],
        ]
    ] = None
    shippingDetails: Optional[
        Union["OfferShippingDetails", List["OfferShippingDetails"]]
    ] = None
    eligibleTransactionVolume: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    validFrom: Optional[Union[datetime, List[datetime], date, List[date]]] = None
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
    acceptedPaymentMethod: Optional[
        Union[
            str,
            List[str],
            "PaymentMethod",
            List["PaymentMethod"],
            "LoanOrCredit",
            List["LoanOrCredit"],
        ]
    ] = None
    seller: Optional[Union[Person, List[Person], Organization, List[Organization]]] = (
        None
    )
    availability: Optional[Union["ItemAvailability", List["ItemAvailability"]]] = None
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    mobileUrl: Optional[Union[str, List[str]]] = None
    sku: Optional[Union[str, List[str]]] = None
    gtin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    availabilityEnds: Optional[
        Union[datetime, List[datetime], time, List[time], date, List[date]]
    ] = None
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = None
    asin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    warranty: Optional[Union["WarrantyPromise", List["WarrantyPromise"]]] = None
    ineligibleRegion: Optional[
        Union[Place, List[Place], str, List[str], "GeoShape", List["GeoShape"]]
    ] = None
    mpn: Optional[Union[str, List[str]]] = None
    serialNumber: Optional[Union[str, List[str]]] = None
    offeredBy: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
    availableAtOrFrom: Optional[Union[Place, List[Place]]] = None
    eligibleQuantity: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    price: Optional[Union[str, List[str], float, List[float]]] = None
    gtin12: Optional[Union[str, List[str]]] = None
    priceCurrency: Optional[Union[str, List[str]]] = None
    addOn: Optional[Union["Offer", List["Offer"]]] = None
    businessFunction: Optional[Union["BusinessFunction", List["BusinessFunction"]]] = (
        None
    )
    availabilityStarts: Optional[
        Union[date, List[date], time, List[time], datetime, List[datetime]]
    ] = None
    isFamilyFriendly: Optional[Union[bool, List[bool]]] = None
    category: Optional[
        Union[
            Thing,
            List[Thing],
            "PhysicalActivityCategory",
            List["PhysicalActivityCategory"],
            "CategoryCode",
            List["CategoryCode"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    priceValidUntil: Optional[Union[date, List[date]]] = None
