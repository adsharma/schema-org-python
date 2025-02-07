from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.aggregate_rating import AggregateRating
from schema_models.alignment_object import AlignmentObject
from schema_models.audience import Audience
from schema_models.audio_object import AudioObject
from schema_models.boolean import Boolean
from schema_models.claim import Claim
from schema_models.clip import Clip
from schema_models.comment import Comment
from schema_models.correction_comment import CorrectionComment
from schema_models.country import Country
from schema_models.creative_work import CreativeWork
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.defined_term import DefinedTerm
from schema_models.demand import Demand
from schema_models.duration import Duration
from schema_models.event import Event
from schema_models.grant import Grant
from schema_models.i_p_t_c_digital_source_enumeration import (
    IPTCDigitalSourceEnumeration,
)
from schema_models.image_object import ImageObject
from schema_models.integer import Integer
from schema_models.interaction_counter import InteractionCounter
from schema_models.item_list import ItemList
from schema_models.language import Language
from schema_models.media_object import MediaObject
from schema_models.music_recording import MusicRecording
from schema_models.number import Number
from schema_models.offer import Offer
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place
from schema_models.product import Product
from schema_models.publication_event import PublicationEvent
from schema_models.quantitative_value import QuantitativeValue
from schema_models.rating import Rating
from schema_models.review import Review
from schema_models.size_specification import SizeSpecification
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL
from schema_models.video_object import VideoObject
from schema_models.web_page import WebPage


class CreativeWork(Thing):
    character: Optional[Union[Person, List[Person]]] = None
    awards: Optional[Union[Text, List[Text]]] = None
    temporal: Optional[Union[DateTime, List[DateTime]]] = None
    temporal: Optional[Union[Text, List[Text]]] = None
    award: Optional[Union[Text, List[Text]]] = None
    sdLicense: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    sdLicense: Optional[Union[URL, List[URL]]] = None
    educationalUse: Optional[Union[Text, List[Text]]] = None
    educationalUse: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    mainEntity: Optional[Union[Thing, List[Thing]]] = None
    assesses: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    assesses: Optional[Union[Text, List[Text]]] = None
    interactionStatistic: Optional[
        Union[InteractionCounter, List[InteractionCounter]]
    ] = None
    acquireLicensePage: Optional[Union[URL, List[URL]]] = None
    acquireLicensePage: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    contributor: Optional[Union[Organization, List[Organization]]] = None
    contributor: Optional[Union[Person, List[Person]]] = None
    educationalLevel: Optional[Union[Text, List[Text]]] = None
    educationalLevel: Optional[Union[URL, List[URL]]] = None
    educationalLevel: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    sdDatePublished: Optional[Union[Date, List[Date]]] = None
    countryOfOrigin: Optional[Union[Country, List[Country]]] = None
    encodingFormat: Optional[Union[URL, List[URL]]] = None
    encodingFormat: Optional[Union[Text, List[Text]]] = None
    keywords: Optional[Union[URL, List[URL]]] = None
    keywords: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    keywords: Optional[Union[Text, List[Text]]] = None
    interpretedAsClaim: Optional[Union[Claim, List[Claim]]] = None
    usageInfo: Optional[Union[URL, List[URL]]] = None
    usageInfo: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    dateCreated: Optional[Union[DateTime, List[DateTime]]] = None
    dateCreated: Optional[Union[Date, List[Date]]] = None
    creator: Optional[Union[Person, List[Person]]] = None
    creator: Optional[Union[Organization, List[Organization]]] = None
    translationOfWork: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    reviews: Optional[Union[Review, List[Review]]] = None
    material: Optional[Union[URL, List[URL]]] = None
    material: Optional[Union[Product, List[Product]]] = None
    material: Optional[Union[Text, List[Text]]] = None
    timeRequired: Optional[Union[Duration, List[Duration]]] = None
    archivedAt: Optional[Union[WebPage, List[WebPage]]] = None
    archivedAt: Optional[Union[URL, List[URL]]] = None
    headline: Optional[Union[Text, List[Text]]] = None
    thumbnailUrl: Optional[Union[URL, List[URL]]] = None
    locationCreated: Optional[Union[Place, List[Place]]] = None
    copyrightNotice: Optional[Union[Text, List[Text]]] = None
    digitalSourceType: Optional[
        Union[IPTCDigitalSourceEnumeration, List[IPTCDigitalSourceEnumeration]]
    ] = None
    version: Optional[Union[Number, List[Number]]] = None
    version: Optional[Union[Text, List[Text]]] = None
    license: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    license: Optional[Union[URL, List[URL]]] = None
    accessibilityFeature: Optional[Union[Text, List[Text]]] = None
    sourceOrganization: Optional[Union[Organization, List[Organization]]] = None
    spatialCoverage: Optional[Union[Place, List[Place]]] = None
    copyrightHolder: Optional[Union[Person, List[Person]]] = None
    copyrightHolder: Optional[Union[Organization, List[Organization]]] = None
    creditText: Optional[Union[Text, List[Text]]] = None
    accessibilityHazard: Optional[Union[Text, List[Text]]] = None
    accountablePerson: Optional[Union[Person, List[Person]]] = None
    genre: Optional[Union[Text, List[Text]]] = None
    genre: Optional[Union[URL, List[URL]]] = None
    accessMode: Optional[Union[Text, List[Text]]] = None
    publishingPrinciples: Optional[Union[URL, List[URL]]] = None
    publishingPrinciples: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    contentReferenceTime: Optional[Union[DateTime, List[DateTime]]] = None
    isAccessibleForFree: Optional[Union[Boolean, List[Boolean]]] = None
    editor: Optional[Union[Person, List[Person]]] = None
    educationalAlignment: Optional[Union[AlignmentObject, List[AlignmentObject]]] = None
    exampleOfWork: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    publication: Optional[Union[PublicationEvent, List[PublicationEvent]]] = None
    producer: Optional[Union[Person, List[Person]]] = None
    producer: Optional[Union[Organization, List[Organization]]] = None
    offers: Optional[Union[Offer, List[Offer]]] = None
    offers: Optional[Union[Demand, List[Demand]]] = None
    accessibilityAPI: Optional[Union[Text, List[Text]]] = None
    contentRating: Optional[Union[Rating, List[Rating]]] = None
    contentRating: Optional[Union[Text, List[Text]]] = None
    size: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    size: Optional[Union[SizeSpecification, List[SizeSpecification]]] = None
    size: Optional[Union[Text, List[Text]]] = None
    size: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    encoding: Optional[Union[MediaObject, List[MediaObject]]] = None
    workExample: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    spatial: Optional[Union[Place, List[Place]]] = None
    accessibilitySummary: Optional[Union[Text, List[Text]]] = None
    recordedAt: Optional[Union[Event, List[Event]]] = None
    dateModified: Optional[Union[Date, List[Date]]] = None
    dateModified: Optional[Union[DateTime, List[DateTime]]] = None
    alternativeHeadline: Optional[Union[Text, List[Text]]] = None
    isBasedOn: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    isBasedOn: Optional[Union[Product, List[Product]]] = None
    isBasedOn: Optional[Union[URL, List[URL]]] = None
    temporalCoverage: Optional[Union[Text, List[Text]]] = None
    temporalCoverage: Optional[Union[URL, List[URL]]] = None
    temporalCoverage: Optional[Union[DateTime, List[DateTime]]] = None
    abstract: Optional[Union[Text, List[Text]]] = None
    learningResourceType: Optional[Union[Text, List[Text]]] = None
    learningResourceType: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    comment: Optional[Union[Comment, List[Comment]]] = None
    position: Optional[Union[Text, List[Text]]] = None
    position: Optional[Union[Integer, List[Integer]]] = None
    conditionsOfAccess: Optional[Union[Text, List[Text]]] = None
    contentLocation: Optional[Union[Place, List[Place]]] = None
    associatedMedia: Optional[Union[MediaObject, List[MediaObject]]] = None
    materialExtent: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    materialExtent: Optional[Union[Text, List[Text]]] = None
    publisherImprint: Optional[Union[Organization, List[Organization]]] = None
    releasedEvent: Optional[Union[PublicationEvent, List[PublicationEvent]]] = None
    translator: Optional[Union[Person, List[Person]]] = None
    translator: Optional[Union[Organization, List[Organization]]] = None
    correction: Optional[Union[Text, List[Text]]] = None
    correction: Optional[Union[URL, List[URL]]] = None
    correction: Optional[Union[CorrectionComment, List[CorrectionComment]]] = None
    isFamilyFriendly: Optional[Union[Boolean, List[Boolean]]] = None
    funding: Optional[Union[Grant, List[Grant]]] = None
    sdPublisher: Optional[Union[Person, List[Person]]] = None
    sdPublisher: Optional[Union[Organization, List[Organization]]] = None
    expires: Optional[Union[Date, List[Date]]] = None
    expires: Optional[Union[DateTime, List[DateTime]]] = None
    teaches: Optional[Union[Text, List[Text]]] = None
    teaches: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    isBasedOnUrl: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    isBasedOnUrl: Optional[Union[Product, List[Product]]] = None
    isBasedOnUrl: Optional[Union[URL, List[URL]]] = None
    aggregateRating: Optional[Union[AggregateRating, List[AggregateRating]]] = None
    editEIDR: Optional[Union[Text, List[Text]]] = None
    editEIDR: Optional[Union[URL, List[URL]]] = None
    provider: Optional[Union[Person, List[Person]]] = None
    provider: Optional[Union[Organization, List[Organization]]] = None
    sponsor: Optional[Union[Person, List[Person]]] = None
    sponsor: Optional[Union[Organization, List[Organization]]] = None
    mentions: Optional[Union[Thing, List[Thing]]] = None
    typicalAgeRange: Optional[Union[Text, List[Text]]] = None
    text: Optional[Union[Text, List[Text]]] = None
    about: Optional[Union[Thing, List[Thing]]] = None
    creativeWorkStatus: Optional[Union[Text, List[Text]]] = None
    creativeWorkStatus: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    datePublished: Optional[Union[Date, List[Date]]] = None
    datePublished: Optional[Union[DateTime, List[DateTime]]] = None
    citation: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    citation: Optional[Union[Text, List[Text]]] = None
    accessModeSufficient: Optional[Union[ItemList, List[ItemList]]] = None
    funder: Optional[Union[Person, List[Person]]] = None
    funder: Optional[Union[Organization, List[Organization]]] = None
    video: Optional[Union[Clip, List[Clip]]] = None
    video: Optional[Union[VideoObject, List[VideoObject]]] = None
    accessibilityControl: Optional[Union[Text, List[Text]]] = None
    audience: Optional[Union[Audience, List[Audience]]] = None
    hasPart: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    schemaVersion: Optional[Union[Text, List[Text]]] = None
    schemaVersion: Optional[Union[URL, List[URL]]] = None
    maintainer: Optional[Union[Person, List[Person]]] = None
    maintainer: Optional[Union[Organization, List[Organization]]] = None
    publisher: Optional[Union[Person, List[Person]]] = None
    publisher: Optional[Union[Organization, List[Organization]]] = None
    isPartOf: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    isPartOf: Optional[Union[URL, List[URL]]] = None
    review: Optional[Union[Review, List[Review]]] = None
    inLanguage: Optional[Union[Language, List[Language]]] = None
    inLanguage: Optional[Union[Text, List[Text]]] = None
    encodings: Optional[Union[MediaObject, List[MediaObject]]] = None
    workTranslation: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    audio: Optional[Union[MusicRecording, List[MusicRecording]]] = None
    audio: Optional[Union[AudioObject, List[AudioObject]]] = None
    audio: Optional[Union[Clip, List[Clip]]] = None
    author: Optional[Union[Person, List[Person]]] = None
    author: Optional[Union[Organization, List[Organization]]] = None
    fileFormat: Optional[Union[Text, List[Text]]] = None
    fileFormat: Optional[Union[URL, List[URL]]] = None
    pattern: Optional[Union[Text, List[Text]]] = None
    pattern: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
    thumbnail: Optional[Union[ImageObject, List[ImageObject]]] = None
    copyrightYear: Optional[Union[Number, List[Number]]] = None
    commentCount: Optional[Union[Integer, List[Integer]]] = None
    discussionUrl: Optional[Union[URL, List[URL]]] = None
    interactivityType: Optional[Union[Text, List[Text]]] = None
