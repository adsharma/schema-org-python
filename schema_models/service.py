from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.demand import Demand
from schema_models.intangible import Intangible
from schema_models.offer import Offer
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place
from schema_models.product import Product
from schema_models.service_channel import ServiceChannel
from schema_models.thing import Thing


class Service(Intangible):
    """
    A service provided by an organization, e.g. delivery service, print services, etc.
    """

    serviceType: Optional[
        Union["GovernmentBenefitsType", List["GovernmentBenefitsType"], str, List[str]]
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
    hoursAvailable: Optional[
        Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]
    ] = None
    produces: Optional[Union[Thing, List[Thing]]] = None
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    broker: Optional[Union[Organization, List[Organization], Person, List[Person]]] = (
        None
    )
    logo: Optional[
        Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]
    ] = None
    serviceArea: Optional[
        Union[
            "GeoShape",
            List["GeoShape"],
            "AdministrativeArea",
            List["AdministrativeArea"],
            Place,
            List[Place],
        ]
    ] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    award: Optional[Union[str, List[str]]] = None
    serviceOutput: Optional[Union[Thing, List[Thing]]] = None
    availableChannel: Optional[Union[ServiceChannel, List[ServiceChannel]]] = None
    offers: Optional[Union[Offer, List[Offer], Demand, List[Demand]]] = None
    slogan: Optional[Union[str, List[str]]] = None
    serviceAudience: Optional[Union["Audience", List["Audience"]]] = None
    providerMobility: Optional[Union[str, List[str]]] = None
    isRelatedTo: Optional[Union[Product, List[Product], "Service", List["Service"]]] = (
        None
    )
    brand: Optional[Union[Organization, List[Organization], "Brand", List["Brand"]]] = (
        None
    )
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
    termsOfService: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    provider: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
    isSimilarTo: Optional[Union[Product, List[Product], "Service", List["Service"]]] = (
        None
    )
    audience: Optional[Union["Audience", List["Audience"]]] = None
