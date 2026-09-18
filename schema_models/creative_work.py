from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.duration import Duration
from schema_models.thing import Thing


@dataclass
class CreativeWork(Thing):
    """
    The most generic kind of creative work, including books, movies, photographs, software programs, etc.
    """

    about: Optional[Union[Thing, List[Thing]]] = None
    abstract: Optional[Union[str, List[str]]] = None
    accessMode: Optional[Union[str, List[str]]] = None
    accessModeSufficient: Optional[Union["ItemList", List["ItemList"]]] = None
    accessibilityAPI: Optional[Union[str, List[str]]] = None
    accessibilityControl: Optional[Union[str, List[str]]] = None
    accessibilityFeature: Optional[Union[str, List[str]]] = None
    accessibilityHazard: Optional[Union[str, List[str]]] = None
    accessibilitySummary: Optional[Union[str, List[str]]] = None
    accountablePerson: Optional[Union["Person", List["Person"]]] = None
    acquireLicensePage: Optional[
        Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]
    ] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    alternativeHeadline: Optional[Union[str, List[str]]] = None
    archivedAt: Optional[Union[HttpUrl, List[HttpUrl], "WebPage", List["WebPage"]]] = (
        None
    )
    assesses: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
    associatedMedia: Optional[Union["MediaObject", List["MediaObject"]]] = None
    audience: Optional[Union["Audience", List["Audience"]]] = None
    audio: Optional[
        Union[
            "AudioObject",
            List["AudioObject"],
            "Clip",
            List["Clip"],
            "MusicRecording",
            List["MusicRecording"],
        ]
    ] = None
    author: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    award: Optional[Union[str, List[str]]] = None
    awards: Optional[Union[str, List[str]]] = None
    character: Optional[Union["Person", List["Person"]]] = None
    citation: Optional[Union["CreativeWork", List["CreativeWork"], str, List[str]]] = (
        None
    )
    comment: Optional[Union["Comment", List["Comment"]]] = None
    commentCount: Optional[Union[int, List[int]]] = None
    conditionsOfAccess: Optional[Union[str, List[str]]] = None
    contentLocation: Optional[Union["Place", List["Place"]]] = None
    contentRating: Optional[Union["Rating", List["Rating"], str, List[str]]] = None
    contentReferenceTime: Optional[Union[datetime, List[datetime]]] = None
    contributor: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    copyrightHolder: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    copyrightNotice: Optional[Union[str, List[str]]] = None
    copyrightYear: Optional[Union[float, List[float]]] = None
    correction: Optional[
        Union[
            "CorrectionComment",
            List["CorrectionComment"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    creativeWorkStatus: Optional[
        Union["DefinedTerm", List["DefinedTerm"], str, List[str]]
    ] = None
    creator: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    creditText: Optional[Union[str, List[str]]] = None
    dateCreated: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    dateModified: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    datePublished: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    digitalSourceType: Optional[
        Union["IPTCDigitalSourceEnumeration", List["IPTCDigitalSourceEnumeration"]]
    ] = None
    discussionUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    displayLocation: Optional[Union["Place", List["Place"]]] = None
    editEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    editor: Optional[Union["Person", List["Person"]]] = None
    educationalAlignment: Optional[
        Union["AlignmentObject", List["AlignmentObject"]]
    ] = None
    educationalLevel: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    educationalUse: Optional[
        Union["DefinedTerm", List["DefinedTerm"], str, List[str]]
    ] = None
    encoding: Optional[Union["MediaObject", List["MediaObject"]]] = None
    encodingFormat: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    encodings: Optional[Union["MediaObject", List["MediaObject"]]] = None
    exampleOfWork: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    expires: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    fileFormat: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    funder: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    genre: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    hasPart: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    headline: Optional[Union[str, List[str]]] = None
    inLanguage: Optional[Union["Language", List["Language"], str, List[str]]] = None
    interactionStatistic: Optional[
        Union["InteractionCounter", List["InteractionCounter"]]
    ] = None
    interactivityType: Optional[Union[str, List[str]]] = None
    interpretedAsClaim: Optional[Union["Claim", List["Claim"]]] = None
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = None
    isBasedOn: Optional[
        Union[
            "CreativeWork",
            List["CreativeWork"],
            "Product",
            List["Product"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    isBasedOnUrl: Optional[
        Union[
            "CreativeWork",
            List["CreativeWork"],
            "Product",
            List["Product"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    isFamilyFriendly: Optional[Union[bool, List[bool]]] = None
    isPartOf: Optional[
        Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]
    ] = None
    keywords: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    learningResourceType: Optional[
        Union["DefinedTerm", List["DefinedTerm"], str, List[str]]
    ] = None
    license: Optional[
        Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]
    ] = None
    locationCreated: Optional[Union["Place", List["Place"]]] = None
    mainEntity: Optional[Union[Thing, List[Thing]]] = None
    maintainer: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    material: Optional[
        Union["Product", List["Product"], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    materialExtent: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], str, List[str]]
    ] = None
    mentions: Optional[Union[Thing, List[Thing]]] = None
    offers: Optional[Union["Demand", List["Demand"], "Offer", List["Offer"]]] = None
    pattern: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
    position: Optional[Union[int, List[int], str, List[str]]] = None
    producer: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    provider: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    publication: Optional[Union["PublicationEvent", List["PublicationEvent"]]] = None
    publisher: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    publisherImprint: Optional[Union["Organization", List["Organization"]]] = None
    publishingPrinciples: Optional[
        Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]
    ] = None
    recordedAt: Optional[Union["Event", List["Event"]]] = None
    releasedEvent: Optional[Union["PublicationEvent", List["PublicationEvent"]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    reviews: Optional[Union["Review", List["Review"]]] = None
    schemaVersion: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    sdDatePublished: Optional[Union[date, List[date]]] = None
    sdLicense: Optional[
        Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]
    ] = None
    sdPublisher: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    size: Optional[
        Union[
            "DefinedTerm",
            List["DefinedTerm"],
            "QuantitativeValue",
            List["QuantitativeValue"],
            "SizeSpecification",
            List["SizeSpecification"],
            str,
            List[str],
        ]
    ] = None
    sourceOrganization: Optional[Union["Organization", List["Organization"]]] = None
    spatial: Optional[Union["Place", List["Place"]]] = None
    spatialCoverage: Optional[Union["Place", List["Place"]]] = None
    sponsor: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    teaches: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
    temporal: Optional[Union[datetime, List[datetime], str, List[str]]] = None
    temporalCoverage: Optional[
        Union[datetime, List[datetime], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    text: Optional[Union[str, List[str]]] = None
    thumbnail: Optional[Union["ImageObject", List["ImageObject"]]] = None
    thumbnailUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    timeRequired: Optional[Union[Duration, List[Duration]]] = None
    translationOfWork: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    translator: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    typicalAgeRange: Optional[Union[str, List[str]]] = None
    usageInfo: Optional[
        Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]
    ] = None
    version: Optional[Union[float, List[float], str, List[str]]] = None
    video: Optional[Union["Clip", List["Clip"], "VideoObject", List["VideoObject"]]] = (
        None
    )
    wordCount: Optional[Union[int, List[int]]] = None
    workExample: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    workTranslation: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
