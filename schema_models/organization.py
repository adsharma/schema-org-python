from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.event import Event
from schema_models.thing import Thing


@dataclass
class Organization(Thing):
    """
    An organization such as a school, NGO, corporation, club, etc.
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
    actionableFeedbackPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    address: Optional[Union["PostalAddress", List["PostalAddress"], str, List[str]]] = (
        None
    )
    agentInteractionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    alumni: Optional[Union["Person", List["Person"]]] = None
    areaServed: Optional[
        Union[
            "AdministrativeArea",
            List["AdministrativeArea"],
            "GeoShape",
            List["GeoShape"],
            "Place",
            List["Place"],
            str,
            List[str],
        ]
    ] = None
    authorizedRepresentative: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    award: Optional[Union[str, List[str]]] = None
    awards: Optional[Union[str, List[str]]] = None
    brand: Optional[
        Union["Brand", List["Brand"], "Organization", List["Organization"]]
    ] = None
    companyRegistration: Optional[Union["Certification", List["Certification"]]] = None
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    contactPoints: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    correctionsPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    department: Optional[Union["Organization", List["Organization"]]] = None
    dissolutionDate: Optional[Union[date, List[date]]] = None
    diversityPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    diversityStaffingReport: Optional[
        Union["Article", List["Article"], HttpUrl, List[HttpUrl]]
    ] = None
    duns: Optional[Union[str, List[str]]] = None
    email: Optional[Union[str, List[str]]] = None
    employee: Optional[Union["Person", List["Person"]]] = None
    employees: Optional[Union["Person", List["Person"]]] = None
    ethicsPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    event: Optional[Union[Event, List[Event]]] = None
    events: Optional[Union[Event, List[Event]]] = None
    faxNumber: Optional[Union[str, List[str]]] = None
    founder: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    founders: Optional[Union["Person", List["Person"]]] = None
    foundingDate: Optional[Union[date, List[date]]] = None
    foundingLocation: Optional[Union["Place", List["Place"]]] = None
    funder: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    globalLocationNumber: Optional[Union[str, List[str]]] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    hasCredential: Optional[Union["Credential", List["Credential"]]] = None
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    hasMemberProgram: Optional[Union["MemberProgram", List["MemberProgram"]]] = None
    hasMerchantReturnPolicy: Optional[
        Union["MerchantReturnPolicy", List["MerchantReturnPolicy"]]
    ] = None
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = None
    hasPOS: Optional[Union["Place", List["Place"]]] = None
    hasProductReturnPolicy: Optional[
        Union["ProductReturnPolicy", List["ProductReturnPolicy"]]
    ] = None
    hasShippingService: Optional[Union["ShippingService", List["ShippingService"]]] = (
        None
    )
    interactionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    isicV4: Optional[Union[str, List[str]]] = None
    iso6523Code: Optional[Union[str, List[str]]] = None
    keywords: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    knowsAbout: Optional[
        Union[str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]
    ] = None
    knowsLanguage: Optional[Union["Language", List["Language"], str, List[str]]] = None
    legalAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    legalName: Optional[Union[str, List[str]]] = None
    legalRepresentative: Optional[Union["Person", List["Person"]]] = None
    leiCode: Optional[Union[str, List[str]]] = None
    location: Optional[
        Union[
            "Place",
            List["Place"],
            "PostalAddress",
            List["PostalAddress"],
            str,
            List[str],
            "VirtualLocation",
            List["VirtualLocation"],
        ]
    ] = None
    logo: Optional[
        Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]
    ] = None
    makesOffer: Optional[Union["Offer", List["Offer"]]] = None
    member: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    memberOf: Optional[
        Union[
            "MemberProgramTier",
            List["MemberProgramTier"],
            "Organization",
            List["Organization"],
            "ProgramMembership",
            List["ProgramMembership"],
        ]
    ] = None
    members: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    naics: Optional[Union[str, List[str]]] = None
    nonprofitStatus: Optional[Union["NonprofitType", List["NonprofitType"]]] = None
    numberOfEmployees: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    ownershipFundingInfo: Optional[
        Union[
            "AboutPage",
            List["AboutPage"],
            CreativeWork,
            List[CreativeWork],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    owns: Optional[Union[Thing, List[Thing]]] = None
    parentOrganization: Optional[Union["Organization", List["Organization"]]] = None
    publishingPrinciples: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    review: Optional[Union["Review", List["Review"]]] = None
    reviews: Optional[Union["Review", List["Review"]]] = None
    seeks: Optional[Union["Demand", List["Demand"]]] = None
    serviceArea: Optional[
        Union[
            "AdministrativeArea",
            List["AdministrativeArea"],
            "GeoShape",
            List["GeoShape"],
            "Place",
            List["Place"],
        ]
    ] = None
    skills: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
    slogan: Optional[Union[str, List[str]]] = None
    sponsor: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    subOrganization: Optional[Union["Organization", List["Organization"]]] = None
    taxID: Optional[Union[str, List[str]]] = None
    telephone: Optional[Union[str, List[str]]] = None
    unnamedSourcesPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    vatID: Optional[Union[str, List[str]]] = None
