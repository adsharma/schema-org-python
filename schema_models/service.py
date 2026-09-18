from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.audience import Audience
from schema_models.brand import Brand
from schema_models.certification import Certification
from schema_models.demand import Demand
from schema_models.intangible import Intangible
from schema_models.offer import Offer
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place
from schema_models.product import Product
from schema_models.review import Review
from schema_models.thing import Thing


@dataclass
class Service(Intangible):
    """
    A service provided by an organization, e.g. delivery service, print services, etc.
    """

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
    audience: Optional[Union[Audience, List[Audience]]] = None
    availableChannel: Optional[Union["ServiceChannel", List["ServiceChannel"]]] = None
    award: Optional[Union[str, List[str]]] = None
    brand: Optional[Union[Brand, List[Brand], Organization, List[Organization]]] = None
    broker: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
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
    hasCertification: Optional[Union[Certification, List[Certification]]] = None
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = None
    hoursAvailable: Optional[
        Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]
    ] = None
    isRelatedTo: Optional[Union[Product, List[Product], "Service", List["Service"]]] = (
        None
    )
    isSimilarTo: Optional[Union[Product, List[Product], "Service", List["Service"]]] = (
        None
    )
    logo: Optional[
        Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]
    ] = None
    offers: Optional[Union[Demand, List[Demand], Offer, List[Offer]]] = None
    produces: Optional[Union[Thing, List[Thing]]] = None
    provider: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    providerMobility: Optional[Union[str, List[str]]] = None
    review: Optional[Union[Review, List[Review]]] = None
    serviceArea: Optional[
        Union[
            "AdministrativeArea",
            List["AdministrativeArea"],
            "GeoShape",
            List["GeoShape"],
            Place,
            List[Place],
        ]
    ] = None
    serviceAudience: Optional[Union[Audience, List[Audience]]] = None
    serviceOutput: Optional[Union[Thing, List[Thing]]] = None
    serviceType: Optional[
        Union["GovernmentBenefitsType", List["GovernmentBenefitsType"], str, List[str]]
    ] = None
    slogan: Optional[Union[str, List[str]]] = None
    termsOfService: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
