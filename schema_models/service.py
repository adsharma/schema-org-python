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
    serviceType: Optional[
        Union["GovernmentBenefitsType", List["GovernmentBenefitsType"]]
    ] = None
    serviceType: Optional[Union[str, List[str]]] = None
    areaServed: Optional[Union[str, List[str]]] = None
    areaServed: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union["GeoShape", List["GeoShape"]]] = None
    areaServed: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = None
    hoursAvailable: Optional[
        Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]
    ] = None
    produces: Optional[Union[Thing, List[Thing]]] = None
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    broker: Optional[Union[Organization, List[Organization]]] = None
    broker: Optional[Union[Person, List[Person]]] = None
    logo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    logo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    serviceArea: Optional[Union["GeoShape", List["GeoShape"]]] = None
    serviceArea: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = (
        None
    )
    serviceArea: Optional[Union[Place, List[Place]]] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    award: Optional[Union[str, List[str]]] = None
    serviceOutput: Optional[Union[Thing, List[Thing]]] = None
    availableChannel: Optional[Union[ServiceChannel, List[ServiceChannel]]] = None
    offers: Optional[Union[Offer, List[Offer]]] = None
    offers: Optional[Union[Demand, List[Demand]]] = None
    slogan: Optional[Union[str, List[str]]] = None
    serviceAudience: Optional[Union["Audience", List["Audience"]]] = None
    providerMobility: Optional[Union[str, List[str]]] = None
    isRelatedTo: Optional[Union[Product, List[Product]]] = None
    isRelatedTo: Optional[Union["Service", List["Service"]]] = None
    brand: Optional[Union[Organization, List[Organization]]] = None
    brand: Optional[Union["Brand", List["Brand"]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union["PhysicalActivityCategory", List["PhysicalActivityCategory"]]
    ] = None
    category: Optional[Union["CategoryCode", List["CategoryCode"]]] = None
    category: Optional[Union[str, List[str]]] = None
    category: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    termsOfService: Optional[Union[str, List[str]]] = None
    termsOfService: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    isSimilarTo: Optional[Union[Product, List[Product]]] = None
    isSimilarTo: Optional[Union["Service", List["Service"]]] = None
    audience: Optional[Union["Audience", List["Audience"]]] = None
