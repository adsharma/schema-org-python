from typing import List, Optional, Union

from schema_models.date import Date
from schema_models.event import Event
from schema_models.product import Product
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class Organization(Thing):
    hasGS1DigitalLink: Optional[Union[URL, List[URL]]] = None
    areaServed: Optional[Union[Text, List[Text]]] = None
    areaServed: Optional[Union["Place", List["Place"]]] = None
    areaServed: Optional[Union["GeoShape", List["GeoShape"]]] = None
    areaServed: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = None
    nonprofitStatus: Optional[Union["NonprofitType", List["NonprofitType"]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    makesOffer: Optional[Union["Offer", List["Offer"]]] = None
    sponsor: Optional[Union["Person", List["Person"]]] = None
    sponsor: Optional[Union["Organization", List["Organization"]]] = None
    hasMemberProgram: Optional[Union["MemberProgram", List["MemberProgram"]]] = None
    parentOrganization: Optional[Union["Organization", List["Organization"]]] = None
    taxID: Optional[Union[Text, List[Text]]] = None
    funder: Optional[Union["Person", List["Person"]]] = None
    funder: Optional[Union["Organization", List["Organization"]]] = None
    hasMerchantReturnPolicy: Optional[
        Union["MerchantReturnPolicy", List["MerchantReturnPolicy"]]
    ] = None
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = None
    employees: Optional[Union["Person", List["Person"]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    contactPoints: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    member: Optional[Union["Person", List["Person"]]] = None
    member: Optional[Union["Organization", List["Organization"]]] = None
    alumni: Optional[Union["Person", List["Person"]]] = None
    unnamedSourcesPolicy: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    unnamedSourcesPolicy: Optional[Union[URL, List[URL]]] = None
    dissolutionDate: Optional[Union[Date, List[Date]]] = None
    awards: Optional[Union[Text, List[Text]]] = None
    diversityPolicy: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    diversityPolicy: Optional[Union[URL, List[URL]]] = None
    foundingDate: Optional[Union[Date, List[Date]]] = None
    award: Optional[Union[Text, List[Text]]] = None
    department: Optional[Union["Organization", List["Organization"]]] = None
    hasCredential: Optional[
        Union[
            "EducationalOccupationalCredential",
            List["EducationalOccupationalCredential"],
        ]
    ] = None
    logo: Optional[Union[URL, List[URL]]] = None
    logo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    interactionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    serviceArea: Optional[Union["GeoShape", List["GeoShape"]]] = None
    serviceArea: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = (
        None
    )
    serviceArea: Optional[Union["Place", List["Place"]]] = None
    actionableFeedbackPolicy: Optional[Union[URL, List[URL]]] = None
    actionableFeedbackPolicy: Optional[Union["CreativeWork", List["CreativeWork"]]] = (
        None
    )
    keywords: Optional[Union[URL, List[URL]]] = None
    keywords: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    keywords: Optional[Union[Text, List[Text]]] = None
    ethicsPolicy: Optional[Union[URL, List[URL]]] = None
    ethicsPolicy: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    reviews: Optional[Union["Review", List["Review"]]] = None
    seeks: Optional[Union["Demand", List["Demand"]]] = None
    knowsAbout: Optional[Union[URL, List[URL]]] = None
    knowsAbout: Optional[Union[Thing, List[Thing]]] = None
    knowsAbout: Optional[Union[Text, List[Text]]] = None
    duns: Optional[Union[Text, List[Text]]] = None
    events: Optional[Union[Event, List[Event]]] = None
    owns: Optional[Union["OwnershipInfo", List["OwnershipInfo"]]] = None
    owns: Optional[Union[Product, List[Product]]] = None
    acceptedPaymentMethod: Optional[Union[Text, List[Text]]] = None
    acceptedPaymentMethod: Optional[Union["PaymentMethod", List["PaymentMethod"]]] = (
        None
    )
    acceptedPaymentMethod: Optional[Union["LoanOrCredit", List["LoanOrCredit"]]] = None
    vatID: Optional[Union[Text, List[Text]]] = None
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = None
    hasProductReturnPolicy: Optional[
        Union["ProductReturnPolicy", List["ProductReturnPolicy"]]
    ] = None
    correctionsPolicy: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    correctionsPolicy: Optional[Union[URL, List[URL]]] = None
    publishingPrinciples: Optional[Union[URL, List[URL]]] = None
    publishingPrinciples: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    iso6523Code: Optional[Union[Text, List[Text]]] = None
    isicV4: Optional[Union[Text, List[Text]]] = None
    founder: Optional[Union["Person", List["Person"]]] = None
    founder: Optional[Union["Organization", List["Organization"]]] = None
    founders: Optional[Union["Person", List["Person"]]] = None
    leiCode: Optional[Union[Text, List[Text]]] = None
    members: Optional[Union["Organization", List["Organization"]]] = None
    members: Optional[Union["Person", List["Person"]]] = None
    numberOfEmployees: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    slogan: Optional[Union[Text, List[Text]]] = None
    telephone: Optional[Union[Text, List[Text]]] = None
    faxNumber: Optional[Union[Text, List[Text]]] = None
    globalLocationNumber: Optional[Union[Text, List[Text]]] = None
    skills: Optional[Union[Text, List[Text]]] = None
    skills: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    subOrganization: Optional[Union["Organization", List["Organization"]]] = None
    email: Optional[Union[Text, List[Text]]] = None
    knowsLanguage: Optional[Union[Text, List[Text]]] = None
    knowsLanguage: Optional[Union["Language", List["Language"]]] = None
    foundingLocation: Optional[Union["Place", List["Place"]]] = None
    memberOf: Optional[Union["ProgramMembership", List["ProgramMembership"]]] = None
    memberOf: Optional[Union["Organization", List["Organization"]]] = None
    memberOf: Optional[Union["MemberProgramTier", List["MemberProgramTier"]]] = None
    agentInteractionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    location: Optional[Union[Text, List[Text]]] = None
    location: Optional[Union["Place", List["Place"]]] = None
    location: Optional[Union["VirtualLocation", List["VirtualLocation"]]] = None
    location: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    diversityStaffingReport: Optional[Union[URL, List[URL]]] = None
    diversityStaffingReport: Optional[Union["Article", List["Article"]]] = None
    event: Optional[Union[Event, List[Event]]] = None
    employee: Optional[Union["Person", List["Person"]]] = None
    naics: Optional[Union[Text, List[Text]]] = None
    brand: Optional[Union["Organization", List["Organization"]]] = None
    brand: Optional[Union["Brand", List["Brand"]]] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    address: Optional[Union[Text, List[Text]]] = None
    address: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    legalName: Optional[Union[Text, List[Text]]] = None
    ownershipFundingInfo: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    ownershipFundingInfo: Optional[Union[Text, List[Text]]] = None
    ownershipFundingInfo: Optional[Union[URL, List[URL]]] = None
    ownershipFundingInfo: Optional[Union["AboutPage", List["AboutPage"]]] = None
    hasPOS: Optional[Union["Place", List["Place"]]] = None
