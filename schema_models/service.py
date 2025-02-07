from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.administrative_area import AdministrativeArea
from schema_models.aggregate_rating import AggregateRating
from schema_models.audience import Audience
from schema_models.brand import Brand
from schema_models.category_code import CategoryCode
from schema_models.certification import Certification
from schema_models.demand import Demand
from schema_models.geo_shape import GeoShape
from schema_models.government_benefits_type import GovernmentBenefitsType
from schema_models.image_object import ImageObject
from schema_models.intangible import Intangible
from schema_models.offer import Offer
from schema_models.offer_catalog import OfferCatalog
from schema_models.opening_hours_specification import OpeningHoursSpecification
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.physical_activity_category import PhysicalActivityCategory
from schema_models.place import Place
from schema_models.product import Product
from schema_models.review import Review
from schema_models.service import Service
from schema_models.service_channel import ServiceChannel
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class Service(Intangible):
    serviceType: Optional[
        Union[GovernmentBenefitsType, List[GovernmentBenefitsType]]
    ] = None
    serviceType: Optional[Union[Text, List[Text]]] = None
    areaServed: Optional[Union[Text, List[Text]]] = None
    areaServed: Optional[Union[Place, List[Place]]] = None
    areaServed: Optional[Union[GeoShape, List[GeoShape]]] = None
    areaServed: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    hoursAvailable: Optional[
        Union[OpeningHoursSpecification, List[OpeningHoursSpecification]]
    ] = None
    produces: Optional[Union[Thing, List[Thing]]] = None
    hasOfferCatalog: Optional[Union[OfferCatalog, List[OfferCatalog]]] = None
    review: Optional[Union[Review, List[Review]]] = None
    broker: Optional[Union[Organization, List[Organization]]] = None
    broker: Optional[Union[Person, List[Person]]] = None
    logo: Optional[Union[URL, List[URL]]] = None
    logo: Optional[Union[ImageObject, List[ImageObject]]] = None
    serviceArea: Optional[Union[GeoShape, List[GeoShape]]] = None
    serviceArea: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    serviceArea: Optional[Union[Place, List[Place]]] = None
    hasCertification: Optional[Union[Certification, List[Certification]]] = None
    award: Optional[Union[Text, List[Text]]] = None
    serviceOutput: Optional[Union[Thing, List[Thing]]] = None
    availableChannel: Optional[Union[ServiceChannel, List[ServiceChannel]]] = None
    offers: Optional[Union[Offer, List[Offer]]] = None
    offers: Optional[Union[Demand, List[Demand]]] = None
    slogan: Optional[Union[Text, List[Text]]] = None
    serviceAudience: Optional[Union[Audience, List[Audience]]] = None
    providerMobility: Optional[Union[Text, List[Text]]] = None
    isRelatedTo: Optional[Union[Product, List[Product]]] = None
    isRelatedTo: Optional[Union["Service", List["Service"]]] = None
    brand: Optional[Union[Organization, List[Organization]]] = None
    brand: Optional[Union[Brand, List[Brand]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union[PhysicalActivityCategory, List[PhysicalActivityCategory]]
    ] = None
    category: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    category: Optional[Union[Text, List[Text]]] = None
    category: Optional[Union[URL, List[URL]]] = None
    termsOfService: Optional[Union[Text, List[Text]]] = None
    termsOfService: Optional[Union[URL, List[URL]]] = None
    aggregateRating: Optional[Union[AggregateRating, List[AggregateRating]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    isSimilarTo: Optional[Union[Product, List[Product]]] = None
    isSimilarTo: Optional[Union["Service", List["Service"]]] = None
    audience: Optional[Union[Audience, List[Audience]]] = None
