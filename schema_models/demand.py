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
from schema_models.trip import Trip


class Demand(Intangible):
    """
    A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.
    """

    gtin14: Optional[Union[str, List[str]]] = None
    gtin12: Optional[Union[str, List[str]]] = None
    businessFunction: Optional[Union["BusinessFunction", List["BusinessFunction"]]] = (
        None
    )
    eligibleRegion: Optional[
        Union["GeoShape", List["GeoShape"], str, List[str], Place, List[Place]]
    ] = None
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
    priceSpecification: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    advanceBookingRequirement: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    gtin8: Optional[Union[str, List[str]]] = None
    availableDeliveryMethod: Optional[
        Union["DeliveryMethod", List["DeliveryMethod"]]
    ] = None
    includesObject: Optional[
        Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]
    ] = None
    eligibleTransactionVolume: Optional[
        Union["PriceSpecification", List["PriceSpecification"]]
    ] = None
    deliveryLeadTime: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    eligibleCustomerType: Optional[
        Union["BusinessEntityType", List["BusinessEntityType"]]
    ] = None
    seller: Optional[Union[Person, List[Person], Organization, List[Organization]]] = (
        None
    )
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
    availability: Optional[Union["ItemAvailability", List["ItemAvailability"]]] = None
    validFrom: Optional[Union[datetime, List[datetime], date, List[date]]] = None
    itemCondition: Optional[Union["OfferItemCondition", List["OfferItemCondition"]]] = (
        None
    )
    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = None
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
    asin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    serialNumber: Optional[Union[str, List[str]]] = None
    sku: Optional[Union[str, List[str]]] = None
    gtin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    availabilityEnds: Optional[
        Union[datetime, List[datetime], time, List[time], date, List[date]]
    ] = None
    availabilityStarts: Optional[
        Union[date, List[date], time, List[time], datetime, List[datetime]]
    ] = None
    warranty: Optional[Union["WarrantyPromise", List["WarrantyPromise"]]] = None
    ineligibleRegion: Optional[
        Union[Place, List[Place], str, List[str], "GeoShape", List["GeoShape"]]
    ] = None
    mpn: Optional[Union[str, List[str]]] = None
    availableAtOrFrom: Optional[Union[Place, List[Place]]] = None
    eligibleQuantity: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
