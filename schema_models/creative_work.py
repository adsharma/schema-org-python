from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.event import Event
from schema_models.organization import Organization
from schema_models.place import Place
from schema_models.product import Product
from schema_models.thing import Thing


class CreativeWork(Thing):
    character: Optional[Union["Person", List["Person"]]] = None
    awards: Optional[Union[str, List[str]]] = None
    temporal: Optional[Union[datetime, List[datetime]]] = None
    temporal: Optional[Union[str, List[str]]] = None
    award: Optional[Union[str, List[str]]] = None
    sdLicense: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    sdLicense: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    educationalUse: Optional[Union[str, List[str]]] = None
    educationalUse: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    mainEntity: Optional[Union[Thing, List[Thing]]] = None
    assesses: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    assesses: Optional[Union[str, List[str]]] = None
    interactionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    acquireLicensePage: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    acquireLicensePage: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    contributor: Optional[Union[Organization, List[Organization]]] = None
    contributor: Optional[Union["Person", List["Person"]]] = None
    educationalLevel: Optional[Union[str, List[str]]] = None
    educationalLevel: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    educationalLevel: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    sdDatePublished: Optional[Union[date, List[date]]] = None
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    encodingFormat: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    encodingFormat: Optional[Union[str, List[str]]] = None
    keywords: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    keywords: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    keywords: Optional[Union[str, List[str]]] = None
    interpretedAsClaim: Optional[Union["Claim", List["Claim"]]] = None
    usageInfo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    usageInfo: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    dateCreated: Optional[Union[datetime, List[datetime]]] = None
    dateCreated: Optional[Union[date, List[date]]] = None
    creator: Optional[Union["Person", List["Person"]]] = None
    creator: Optional[Union[Organization, List[Organization]]] = None
    translationOfWork: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    reviews: Optional[Union["Review", List["Review"]]] = None
    material: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    material: Optional[Union[Product, List[Product]]] = None
    material: Optional[Union[str, List[str]]] = None
    timeRequired: Optional[Union["Duration", List["Duration"]]] = None
    archivedAt: Optional[Union["WebPage", List["WebPage"]]] = None
    archivedAt: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    headline: Optional[Union[str, List[str]]] = None
    thumbnailUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    locationCreated: Optional[Union[Place, List[Place]]] = None
    copyrightNotice: Optional[Union[str, List[str]]] = None
    digitalSourceType: Optional[
        Union["IPTCDigitalSourceEnumeration", List["IPTCDigitalSourceEnumeration"]]
    ] = None
    version: Optional[Union[float, List[float]]] = None
    version: Optional[Union[str, List[str]]] = None
    license: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    license: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    accessibilityFeature: Optional[Union[str, List[str]]] = None
    sourceOrganization: Optional[Union[Organization, List[Organization]]] = None
    spatialCoverage: Optional[Union[Place, List[Place]]] = None
    copyrightHolder: Optional[Union["Person", List["Person"]]] = None
    copyrightHolder: Optional[Union[Organization, List[Organization]]] = None
    creditText: Optional[Union[str, List[str]]] = None
    accessibilityHazard: Optional[Union[str, List[str]]] = None
    accountablePerson: Optional[Union["Person", List["Person"]]] = None
    genre: Optional[Union[str, List[str]]] = None
    genre: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    accessMode: Optional[Union[str, List[str]]] = None
    publishingPrinciples: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    publishingPrinciples: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    contentReferenceTime: Optional[Union[datetime, List[datetime]]] = None
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = None
    editor: Optional[Union["Person", List["Person"]]] = None
    educationalAlignment: Optional[
        Union["AlignmentObject", List["AlignmentObject"]]
    ] = None
    exampleOfWork: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    publication: Optional[Union["PublicationEvent", List["PublicationEvent"]]] = None
    producer: Optional[Union["Person", List["Person"]]] = None
    producer: Optional[Union[Organization, List[Organization]]] = None
    offers: Optional[Union["Offer", List["Offer"]]] = None
    offers: Optional[Union["Demand", List["Demand"]]] = None
    accessibilityAPI: Optional[Union[str, List[str]]] = None
    contentRating: Optional[Union["Rating", List["Rating"]]] = None
    contentRating: Optional[Union[str, List[str]]] = None
    size: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    size: Optional[Union["SizeSpecification", List["SizeSpecification"]]] = None
    size: Optional[Union[str, List[str]]] = None
    size: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    encoding: Optional[Union["MediaObject", List["MediaObject"]]] = None
    workExample: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    spatial: Optional[Union[Place, List[Place]]] = None
    accessibilitySummary: Optional[Union[str, List[str]]] = None
    recordedAt: Optional[Union[Event, List[Event]]] = None
    dateModified: Optional[Union[date, List[date]]] = None
    dateModified: Optional[Union[datetime, List[datetime]]] = None
    alternativeHeadline: Optional[Union[str, List[str]]] = None
    isBasedOn: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    isBasedOn: Optional[Union[Product, List[Product]]] = None
    isBasedOn: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    temporalCoverage: Optional[Union[str, List[str]]] = None
    temporalCoverage: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    temporalCoverage: Optional[Union[datetime, List[datetime]]] = None
    abstract: Optional[Union[str, List[str]]] = None
    learningResourceType: Optional[Union[str, List[str]]] = None
    learningResourceType: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    comment: Optional[Union["Comment", List["Comment"]]] = None
    position: Optional[Union[str, List[str]]] = None
    position: Optional[Union[int, List[int]]] = None
    conditionsOfAccess: Optional[Union[str, List[str]]] = None
    contentLocation: Optional[Union[Place, List[Place]]] = None
    associatedMedia: Optional[Union["MediaObject", List["MediaObject"]]] = None
    materialExtent: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    materialExtent: Optional[Union[str, List[str]]] = None
    publisherImprint: Optional[Union[Organization, List[Organization]]] = None
    releasedEvent: Optional[Union["PublicationEvent", List["PublicationEvent"]]] = None
    translator: Optional[Union["Person", List["Person"]]] = None
    translator: Optional[Union[Organization, List[Organization]]] = None
    correction: Optional[Union[str, List[str]]] = None
    correction: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    correction: Optional[Union["CorrectionComment", List["CorrectionComment"]]] = None
    isFamilyFriendly: Optional[Union[bool, List[bool]]] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    sdPublisher: Optional[Union["Person", List["Person"]]] = None
    sdPublisher: Optional[Union[Organization, List[Organization]]] = None
    expires: Optional[Union[date, List[date]]] = None
    expires: Optional[Union[datetime, List[datetime]]] = None
    teaches: Optional[Union[str, List[str]]] = None
    teaches: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    isBasedOnUrl: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    isBasedOnUrl: Optional[Union[Product, List[Product]]] = None
    isBasedOnUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    editEIDR: Optional[Union[str, List[str]]] = None
    editEIDR: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    provider: Optional[Union["Person", List["Person"]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    sponsor: Optional[Union["Person", List["Person"]]] = None
    sponsor: Optional[Union[Organization, List[Organization]]] = None
    mentions: Optional[Union[Thing, List[Thing]]] = None
    typicalAgeRange: Optional[Union[str, List[str]]] = None
    text: Optional[Union[str, List[str]]] = None
    about: Optional[Union[Thing, List[Thing]]] = None
    creativeWorkStatus: Optional[Union[str, List[str]]] = None
    creativeWorkStatus: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    datePublished: Optional[Union[date, List[date]]] = None
    datePublished: Optional[Union[datetime, List[datetime]]] = None
    citation: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    citation: Optional[Union[str, List[str]]] = None
    accessModeSufficient: Optional[Union["ItemList", List["ItemList"]]] = None
    funder: Optional[Union["Person", List["Person"]]] = None
    funder: Optional[Union[Organization, List[Organization]]] = None
    video: Optional[Union["Clip", List["Clip"]]] = None
    video: Optional[Union["VideoObject", List["VideoObject"]]] = None
    accessibilityControl: Optional[Union[str, List[str]]] = None
    audience: Optional[Union["Audience", List["Audience"]]] = None
    hasPart: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    schemaVersion: Optional[Union[str, List[str]]] = None
    schemaVersion: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    maintainer: Optional[Union["Person", List["Person"]]] = None
    maintainer: Optional[Union[Organization, List[Organization]]] = None
    publisher: Optional[Union["Person", List["Person"]]] = None
    publisher: Optional[Union[Organization, List[Organization]]] = None
    isPartOf: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    isPartOf: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    inLanguage: Optional[Union["Language", List["Language"]]] = None
    inLanguage: Optional[Union[str, List[str]]] = None
    encodings: Optional[Union["MediaObject", List["MediaObject"]]] = None
    workTranslation: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    audio: Optional[Union["MusicRecording", List["MusicRecording"]]] = None
    audio: Optional[Union["AudioObject", List["AudioObject"]]] = None
    audio: Optional[Union["Clip", List["Clip"]]] = None
    author: Optional[Union["Person", List["Person"]]] = None
    author: Optional[Union[Organization, List[Organization]]] = None
    fileFormat: Optional[Union[str, List[str]]] = None
    fileFormat: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    pattern: Optional[Union[str, List[str]]] = None
    pattern: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    thumbnail: Optional[Union["ImageObject", List["ImageObject"]]] = None
    copyrightYear: Optional[Union[float, List[float]]] = None
    commentCount: Optional[Union[int, List[int]]] = None
    discussionUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    interactivityType: Optional[Union[str, List[str]]] = None
