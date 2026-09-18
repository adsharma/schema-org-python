from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.distance import Distance
from schema_models.event import Event
from schema_models.mass import Mass
from schema_models.organization import Organization
from schema_models.thing import Thing


@dataclass
class Person(Thing):
    """
    A person (alive, dead, undead, or fictional).
    """

    additionalName: Optional[Union[str, List[str]]] = None
    address: Optional[Union["PostalAddress", List["PostalAddress"], str, List[str]]] = (
        None
    )
    affiliation: Optional[Union[Organization, List[Organization]]] = None
    agentInteractionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    alumniOf: Optional[
        Union[
            "EducationalOrganization",
            List["EducationalOrganization"],
            Organization,
            List[Organization],
        ]
    ] = None
    award: Optional[Union[str, List[str]]] = None
    awards: Optional[Union[str, List[str]]] = None
    birthDate: Optional[Union[date, List[date]]] = None
    birthPlace: Optional[Union["Place", List["Place"]]] = None
    brand: Optional[Union["Brand", List["Brand"], Organization, List[Organization]]] = (
        None
    )
    callSign: Optional[Union[str, List[str]]] = None
    children: Optional[Union["Person", List["Person"]]] = None
    colleague: Optional[Union["Person", List["Person"], HttpUrl, List[HttpUrl]]] = None
    colleagues: Optional[Union["Person", List["Person"]]] = None
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    contactPoints: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    deathDate: Optional[Union[date, List[date]]] = None
    deathPlace: Optional[Union["Place", List["Place"]]] = None
    duns: Optional[Union[str, List[str]]] = None
    email: Optional[Union[str, List[str]]] = None
    familyName: Optional[Union[str, List[str]]] = None
    faxNumber: Optional[Union[str, List[str]]] = None
    follows: Optional[Union["Person", List["Person"]]] = None
    funder: Optional[
        Union[Organization, List[Organization], "Person", List["Person"]]
    ] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    gender: Optional[Union["GenderType", List["GenderType"], str, List[str]]] = None
    givenName: Optional[Union[str, List[str]]] = None
    globalLocationNumber: Optional[Union[str, List[str]]] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    hasCredential: Optional[Union["Credential", List["Credential"]]] = None
    hasOccupation: Optional[Union["Occupation", List["Occupation"]]] = None
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = None
    hasPOS: Optional[Union["Place", List["Place"]]] = None
    height: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    homeLocation: Optional[
        Union["ContactPoint", List["ContactPoint"], "Place", List["Place"]]
    ] = None
    honorificPrefix: Optional[Union[str, List[str]]] = None
    honorificSuffix: Optional[Union[str, List[str]]] = None
    interactionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    isicV4: Optional[Union[str, List[str]]] = None
    jobTitle: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
    knows: Optional[Union["Person", List["Person"]]] = None
    knowsAbout: Optional[
        Union[str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]
    ] = None
    knowsLanguage: Optional[Union["Language", List["Language"], str, List[str]]] = None
    lifeEvent: Optional[Union[Event, List[Event]]] = None
    makesOffer: Optional[Union["Offer", List["Offer"]]] = None
    memberOf: Optional[
        Union[
            "MemberProgramTier",
            List["MemberProgramTier"],
            Organization,
            List[Organization],
            "ProgramMembership",
            List["ProgramMembership"],
        ]
    ] = None
    naics: Optional[Union[str, List[str]]] = None
    nationality: Optional[Union["Country", List["Country"]]] = None
    netWorth: Optional[
        Union[
            "MonetaryAmount",
            List["MonetaryAmount"],
            "PriceSpecification",
            List["PriceSpecification"],
        ]
    ] = None
    owns: Optional[Union[Thing, List[Thing]]] = None
    parent: Optional[Union["Person", List["Person"]]] = None
    parents: Optional[Union["Person", List["Person"]]] = None
    performerIn: Optional[Union[Event, List[Event]]] = None
    pronouns: Optional[
        Union[
            "DefinedTerm",
            List["DefinedTerm"],
            "StructuredValue",
            List["StructuredValue"],
            str,
            List[str],
        ]
    ] = None
    publishingPrinciples: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    relatedTo: Optional[Union["Person", List["Person"]]] = None
    seeks: Optional[Union["Demand", List["Demand"]]] = None
    sibling: Optional[Union["Person", List["Person"]]] = None
    siblings: Optional[Union["Person", List["Person"]]] = None
    skills: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
    sponsor: Optional[
        Union[Organization, List[Organization], "Person", List["Person"]]
    ] = None
    spouse: Optional[Union["Person", List["Person"]]] = None
    taxID: Optional[Union[str, List[str]]] = None
    telephone: Optional[Union[str, List[str]]] = None
    vatID: Optional[Union[str, List[str]]] = None
    weight: Optional[
        Union[Mass, List[Mass], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    workLocation: Optional[
        Union["ContactPoint", List["ContactPoint"], "Place", List["Place"]]
    ] = None
    worksFor: Optional[Union[Organization, List[Organization]]] = None
