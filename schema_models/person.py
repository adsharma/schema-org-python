from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.event import Event
from schema_models.organization import Organization
from schema_models.place import Place
from schema_models.product import Product
from schema_models.thing import Thing


class Person(Thing):
    deathDate: Optional[Union[date, List[date]]] = None
    affiliation: Optional[Union[Organization, List[Organization]]] = None
    awards: Optional[Union[str, List[str]]] = None
    taxID: Optional[Union[str, List[str]]] = None
    alumniOf: Optional[
        Union["EducationalOrganization", List["EducationalOrganization"]]
    ] = None
    alumniOf: Optional[Union[Organization, List[Organization]]] = None
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = None
    birthPlace: Optional[Union[Place, List[Place]]] = None
    workLocation: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    workLocation: Optional[Union[Place, List[Place]]] = None
    hasCredential: Optional[
        Union[
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
        ]
    ] = None
    relatedTo: Optional[Union["Person", List["Person"]]] = None
    contactPoints: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    additionalName: Optional[Union[str, List[str]]] = None
    birthDate: Optional[Union[date, List[date]]] = None
    seeks: Optional[Union["Demand", List["Demand"]]] = None
    gender: Optional[Union["GenderType", List["GenderType"]]] = None
    gender: Optional[Union[str, List[str]]] = None
    knowsAbout: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    knowsAbout: Optional[Union[Thing, List[Thing]]] = None
    knowsAbout: Optional[Union[str, List[str]]] = None
    jobTitle: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    jobTitle: Optional[Union[str, List[str]]] = None
    duns: Optional[Union[str, List[str]]] = None
    knows: Optional[Union["Person", List["Person"]]] = None
    givenName: Optional[Union[str, List[str]]] = None
    spouse: Optional[Union["Person", List["Person"]]] = None
    award: Optional[Union[str, List[str]]] = None
    callSign: Optional[Union[str, List[str]]] = None
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    publishingPrinciples: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    publishingPrinciples: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    interactionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    parents: Optional[Union["Person", List["Person"]]] = None
    isicV4: Optional[Union[str, List[str]]] = None
    nationality: Optional[Union["Country", List["Country"]]] = None
    follows: Optional[Union["Person", List["Person"]]] = None
    honorificPrefix: Optional[Union[str, List[str]]] = None
    worksFor: Optional[Union[Organization, List[Organization]]] = None
    children: Optional[Union["Person", List["Person"]]] = None
    owns: Optional[Union["OwnershipInfo", List["OwnershipInfo"]]] = None
    owns: Optional[Union[Product, List[Product]]] = None
    vatID: Optional[Union[str, List[str]]] = None
    globalLocationNumber: Optional[Union[str, List[str]]] = None
    skills: Optional[Union[str, List[str]]] = None
    skills: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    email: Optional[Union[str, List[str]]] = None
    weight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    deathPlace: Optional[Union[Place, List[Place]]] = None
    knowsLanguage: Optional[Union[str, List[str]]] = None
    knowsLanguage: Optional[Union["Language", List["Language"]]] = None
    familyName: Optional[Union[str, List[str]]] = None
    memberOf: Optional[Union["ProgramMembership", List["ProgramMembership"]]] = None
    memberOf: Optional[Union[Organization, List[Organization]]] = None
    memberOf: Optional[Union["MemberProgramTier", List["MemberProgramTier"]]] = None
    sibling: Optional[Union["Person", List["Person"]]] = None
    hasOccupation: Optional[Union["Occupation", List["Occupation"]]] = None
    brand: Optional[Union[Organization, List[Organization]]] = None
    brand: Optional[Union["Brand", List["Brand"]]] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    address: Optional[Union[str, List[str]]] = None
    address: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    siblings: Optional[Union["Person", List["Person"]]] = None
    hasPOS: Optional[Union[Place, List[Place]]] = None
    telephone: Optional[Union[str, List[str]]] = None
    colleague: Optional[Union["Person", List["Person"]]] = None
    colleague: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    faxNumber: Optional[Union[str, List[str]]] = None
    honorificSuffix: Optional[Union[str, List[str]]] = None
    makesOffer: Optional[Union["Offer", List["Offer"]]] = None
    performerIn: Optional[Union[Event, List[Event]]] = None
    sponsor: Optional[Union["Person", List["Person"]]] = None
    sponsor: Optional[Union[Organization, List[Organization]]] = None
    homeLocation: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    homeLocation: Optional[Union[Place, List[Place]]] = None
    agentInteractionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    funder: Optional[Union["Person", List["Person"]]] = None
    funder: Optional[Union[Organization, List[Organization]]] = None
    parent: Optional[Union["Person", List["Person"]]] = None
    netWorth: Optional[Union["PriceSpecification", List["PriceSpecification"]]] = None
    netWorth: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    colleagues: Optional[Union["Person", List["Person"]]] = None
    naics: Optional[Union[str, List[str]]] = None
    height: Optional[Union["Distance", List["Distance"]]] = None
    height: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
