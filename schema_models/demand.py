from dataclasses import dataclass
from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.event import Event
from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place
from schema_models.product import Product


@dataclass
class Demand(Intangible):
    """
    A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.
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
    advanceBookingRequirement: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
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
    includesObject: Optional[
        Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]
    ] = None
    ineligibleRegion: Optional[
        Union["GeoShape", List["GeoShape"], Place, List[Place], str, List[str]]
    ] = None
    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
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
            "MenuItem",
            List["MenuItem"],
            Product,
            List[Product],
            "Service",
            List["Service"],
            "Trip",
            List["Trip"],
        ]
    ] = None
    mpn: Optional[Union[str, List[str]]] = None
    priceSpecification: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    seller: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    serialNumber: Optional[Union[str, List[str]]] = None
    sku: Optional[Union[str, List[str]]] = None
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    warranty: Optional[Union["WarrantyPromise", List["WarrantyPromise"]]] = None
