from typing import List, Optional, Union

from schema_models.brand import Brand
from schema_models.certification import Certification
from schema_models.contact_point import ContactPoint
from schema_models.country import Country
from schema_models.creative_work import CreativeWork
from schema_models.date import Date
from schema_models.defined_term import DefinedTerm
from schema_models.demand import Demand
from schema_models.distance import Distance
from schema_models.educational_occupational_credential import (
    EducationalOccupationalCredential,
)
from schema_models.educational_organization import EducationalOrganization
from schema_models.event import Event
from schema_models.gender_type import GenderType
from schema_models.grant import Grant
from schema_models.interaction_counter import InteractionCounter
from schema_models.language import Language
from schema_models.member_program_tier import MemberProgramTier
from schema_models.monetary_amount import MonetaryAmount
from schema_models.occupation import Occupation
from schema_models.offer import Offer
from schema_models.offer_catalog import OfferCatalog
from schema_models.organization import Organization
from schema_models.ownership_info import OwnershipInfo
from schema_models.place import Place
from schema_models.postal_address import PostalAddress
from schema_models.price_specification import PriceSpecification
from schema_models.product import Product
from schema_models.program_membership import ProgramMembership
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class Person(Thing):
    deathDate: Optional[Union[Date, List[Date]]] = None
    affiliation: Optional[Union[Organization, List[Organization]]] = None
    awards: Optional[Union[Text, List[Text]]] = None
    taxID: Optional[Union[Text, List[Text]]] = None
    alumniOf: Optional[
        Union[EducationalOrganization, List[EducationalOrganization]]
    ] = None
    alumniOf: Optional[Union[Organization, List[Organization]]] = None
    hasOfferCatalog: Optional[Union[OfferCatalog, List[OfferCatalog]]] = None
    birthPlace: Optional[Union[Place, List[Place]]] = None
    workLocation: Optional[Union[ContactPoint, List[ContactPoint]]] = None
    workLocation: Optional[Union[Place, List[Place]]] = None
    hasCredential: Optional[
        Union[
            EducationalOccupationalCredential, List[EducationalOccupationalCredential]
        ]
    ] = None
    relatedTo: Optional[Union["Person", List["Person"]]] = None
    contactPoints: Optional[Union[ContactPoint, List[ContactPoint]]] = None
    hasCertification: Optional[Union[Certification, List[Certification]]] = None
    additionalName: Optional[Union[Text, List[Text]]] = None
    birthDate: Optional[Union[Date, List[Date]]] = None
    seeks: Optional[Union[Demand, List[Demand]]] = None
    gender: Optional[Union[GenderType, List[GenderType]]] = None
    gender: Optional[Union[Text, List[Text]]] = None
    knowsAbout: Optional[Union[URL, List[URL]]] = None
    knowsAbout: Optional[Union[Thing, List[Thing]]] = None
    knowsAbout: Optional[Union[Text, List[Text]]] = None
    jobTitle: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    jobTitle: Optional[Union[Text, List[Text]]] = None
    duns: Optional[Union[Text, List[Text]]] = None
    knows: Optional[Union["Person", List["Person"]]] = None
    givenName: Optional[Union[Text, List[Text]]] = None
    spouse: Optional[Union["Person", List["Person"]]] = None
    award: Optional[Union[Text, List[Text]]] = None
    callSign: Optional[Union[Text, List[Text]]] = None
    contactPoint: Optional[Union[ContactPoint, List[ContactPoint]]] = None
    publishingPrinciples: Optional[Union[URL, List[URL]]] = None
    publishingPrinciples: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    interactionStatistic: Optional[
        Union[InteractionCounter, List[InteractionCounter]]
    ] = None
    parents: Optional[Union["Person", List["Person"]]] = None
    isicV4: Optional[Union[Text, List[Text]]] = None
    nationality: Optional[Union[Country, List[Country]]] = None
    follows: Optional[Union["Person", List["Person"]]] = None
    honorificPrefix: Optional[Union[Text, List[Text]]] = None
    worksFor: Optional[Union[Organization, List[Organization]]] = None
    children: Optional[Union["Person", List["Person"]]] = None
    owns: Optional[Union[OwnershipInfo, List[OwnershipInfo]]] = None
    owns: Optional[Union[Product, List[Product]]] = None
    vatID: Optional[Union[Text, List[Text]]] = None
    globalLocationNumber: Optional[Union[Text, List[Text]]] = None
    skills: Optional[Union[Text, List[Text]]] = None
    skills: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    email: Optional[Union[Text, List[Text]]] = None
    weight: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    deathPlace: Optional[Union[Place, List[Place]]] = None
    knowsLanguage: Optional[Union[Text, List[Text]]] = None
    knowsLanguage: Optional[Union[Language, List[Language]]] = None
    familyName: Optional[Union[Text, List[Text]]] = None
    memberOf: Optional[Union[ProgramMembership, List[ProgramMembership]]] = None
    memberOf: Optional[Union[Organization, List[Organization]]] = None
    memberOf: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = None
    sibling: Optional[Union["Person", List["Person"]]] = None
    hasOccupation: Optional[Union[Occupation, List[Occupation]]] = None
    brand: Optional[Union[Organization, List[Organization]]] = None
    brand: Optional[Union[Brand, List[Brand]]] = None
    funding: Optional[Union[Grant, List[Grant]]] = None
    address: Optional[Union[Text, List[Text]]] = None
    address: Optional[Union[PostalAddress, List[PostalAddress]]] = None
    siblings: Optional[Union["Person", List["Person"]]] = None
    hasPOS: Optional[Union[Place, List[Place]]] = None
    telephone: Optional[Union[Text, List[Text]]] = None
    colleague: Optional[Union["Person", List["Person"]]] = None
    colleague: Optional[Union[URL, List[URL]]] = None
    faxNumber: Optional[Union[Text, List[Text]]] = None
    honorificSuffix: Optional[Union[Text, List[Text]]] = None
    makesOffer: Optional[Union[Offer, List[Offer]]] = None
    performerIn: Optional[Union[Event, List[Event]]] = None
    sponsor: Optional[Union["Person", List["Person"]]] = None
    sponsor: Optional[Union[Organization, List[Organization]]] = None
    homeLocation: Optional[Union[ContactPoint, List[ContactPoint]]] = None
    homeLocation: Optional[Union[Place, List[Place]]] = None
    agentInteractionStatistic: Optional[
        Union[InteractionCounter, List[InteractionCounter]]
    ] = None
    funder: Optional[Union["Person", List["Person"]]] = None
    funder: Optional[Union[Organization, List[Organization]]] = None
    parent: Optional[Union["Person", List["Person"]]] = None
    netWorth: Optional[Union[PriceSpecification, List[PriceSpecification]]] = None
    netWorth: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    colleagues: Optional[Union["Person", List["Person"]]] = None
    naics: Optional[Union[Text, List[Text]]] = None
    height: Optional[Union[Distance, List[Distance]]] = None
    height: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
