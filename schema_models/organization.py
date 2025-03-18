from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event
from schema_models.product import Product
from schema_models.thing import Thing


class Organization(Thing):
    """
    An organization such as a school, NGO, corporation, club, etc.
    """

    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    areaServed: Optional[
        Union[
            str,
            List[str],
            "Place",
            List["Place"],
            "GeoShape",
            List["GeoShape"],
            "AdministrativeArea",
            List["AdministrativeArea"],
        ]
    ] = None
    nonprofitStatus: Optional[Union["NonprofitType", List["NonprofitType"]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    makesOffer: Optional[Union["Offer", List["Offer"]]] = None
    sponsor: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    hasMemberProgram: Optional[Union["MemberProgram", List["MemberProgram"]]] = None
    parentOrganization: Optional[Union["Organization", List["Organization"]]] = None
    taxID: Optional[Union[str, List[str]]] = None
    funder: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    hasMerchantReturnPolicy: Optional[
        Union["MerchantReturnPolicy", List["MerchantReturnPolicy"]]
    ] = None
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = None
    employees: Optional[Union["Person", List["Person"]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    contactPoints: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    member: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    alumni: Optional[Union["Person", List["Person"]]] = None
    unnamedSourcesPolicy: Optional[
        Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]
    ] = None
    dissolutionDate: Optional[Union[date, List[date]]] = None
    awards: Optional[Union[str, List[str]]] = None
    diversityPolicy: Optional[
        Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]
    ] = None
    foundingDate: Optional[Union[date, List[date]]] = None
    award: Optional[Union[str, List[str]]] = None
    department: Optional[Union["Organization", List["Organization"]]] = None
    hasCredential: Optional[
        Union[
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
        ]
    ] = None
    logo: Optional[
        Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]
    ] = None
    interactionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    serviceArea: Optional[
        Union[
            "GeoShape",
            List["GeoShape"],
            "AdministrativeArea",
            List["AdministrativeArea"],
            "Place",
            List["Place"],
        ]
    ] = None
    actionableFeedbackPolicy: Optional[
        Union[HttpUrl, List[HttpUrl], "CreativeWork", List["CreativeWork"]]
    ] = None
    keywords: Optional[
        Union[
            HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"], str, List[str]
        ]
    ] = None
    ethicsPolicy: Optional[
        Union[HttpUrl, List[HttpUrl], "CreativeWork", List["CreativeWork"]]
    ] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    reviews: Optional[Union["Review", List["Review"]]] = None
    seeks: Optional[Union["Demand", List["Demand"]]] = None
    knowsAbout: Optional[
        Union[HttpUrl, List[HttpUrl], Thing, List[Thing], str, List[str]]
    ] = None
    duns: Optional[Union[str, List[str]]] = None
    events: Optional[Union[Event, List[Event]]] = None
    owns: Optional[
        Union["OwnershipInfo", List["OwnershipInfo"], Product, List[Product]]
    ] = None
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
    vatID: Optional[Union[str, List[str]]] = None
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    hasProductReturnPolicy: Optional[
        Union["ProductReturnPolicy", List["ProductReturnPolicy"]]
    ] = None
    correctionsPolicy: Optional[
        Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]
    ] = None
    publishingPrinciples: Optional[
        Union[HttpUrl, List[HttpUrl], "CreativeWork", List["CreativeWork"]]
    ] = None
    iso6523Code: Optional[Union[str, List[str]]] = None
    isicV4: Optional[Union[str, List[str]]] = None
    founder: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    founders: Optional[Union["Person", List["Person"]]] = None
    leiCode: Optional[Union[str, List[str]]] = None
    members: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    numberOfEmployees: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    slogan: Optional[Union[str, List[str]]] = None
    telephone: Optional[Union[str, List[str]]] = None
    faxNumber: Optional[Union[str, List[str]]] = None
    globalLocationNumber: Optional[Union[str, List[str]]] = None
    skills: Optional[Union[str, List[str], "DefinedTerm", List["DefinedTerm"]]] = None
    subOrganization: Optional[Union["Organization", List["Organization"]]] = None
    email: Optional[Union[str, List[str]]] = None
    knowsLanguage: Optional[Union[str, List[str], "Language", List["Language"]]] = None
    foundingLocation: Optional[Union["Place", List["Place"]]] = None
    memberOf: Optional[
        Union[
            "ProgramMembership",
            List["ProgramMembership"],
            "Organization",
            List["Organization"],
            "MemberProgramTier",
            List["MemberProgramTier"],
        ]
    ] = None
    agentInteractionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    location: Optional[
        Union[
            str,
            List[str],
            "Place",
            List["Place"],
            "VirtualLocation",
            List["VirtualLocation"],
            "PostalAddress",
            List["PostalAddress"],
        ]
    ] = None
    diversityStaffingReport: Optional[
        Union[HttpUrl, List[HttpUrl], "Article", List["Article"]]
    ] = None
    event: Optional[Union[Event, List[Event]]] = None
    employee: Optional[Union["Person", List["Person"]]] = None
    naics: Optional[Union[str, List[str]]] = None
    brand: Optional[
        Union["Organization", List["Organization"], "Brand", List["Brand"]]
    ] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    address: Optional[Union[str, List[str], "PostalAddress", List["PostalAddress"]]] = (
        None
    )
    legalName: Optional[Union[str, List[str]]] = None
    ownershipFundingInfo: Optional[
        Union[
            "CreativeWork",
            List["CreativeWork"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
            "AboutPage",
            List["AboutPage"],
        ]
    ] = None
    hasPOS: Optional[Union["Place", List["Place"]]] = None
