from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.integer import Integer
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.time import Time
from schema_models.url import URL


class Event(Thing):
    eventAttendanceMode: Optional[
        Union["EventAttendanceModeEnumeration", List["EventAttendanceModeEnumeration"]]
    ] = None
    location: Optional[Union[Text, List[Text]]] = None
    location: Optional[Union["Place", List["Place"]]] = None
    location: Optional[Union["VirtualLocation", List["VirtualLocation"]]] = None
    location: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    duration: Optional[Union["Duration", List["Duration"]]] = None
    doorTime: Optional[Union[DateTime, List[DateTime]]] = None
    doorTime: Optional[Union[Time, List[Time]]] = None
    director: Optional[Union["Person", List["Person"]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    organizer: Optional[Union["Person", List["Person"]]] = None
    organizer: Optional[Union["Organization", List["Organization"]]] = None
    sponsor: Optional[Union["Person", List["Person"]]] = None
    sponsor: Optional[Union["Organization", List["Organization"]]] = None
    typicalAgeRange: Optional[Union[Text, List[Text]]] = None
    about: Optional[Union[Thing, List[Thing]]] = None
    funder: Optional[Union["Person", List["Person"]]] = None
    funder: Optional[Union["Organization", List["Organization"]]] = None
    audience: Optional[Union["Audience", List["Audience"]]] = None
    performer: Optional[Union["Person", List["Person"]]] = None
    performer: Optional[Union["Organization", List["Organization"]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    inLanguage: Optional[Union["Language", List["Language"]]] = None
    inLanguage: Optional[Union[Text, List[Text]]] = None
    remainingAttendeeCapacity: Optional[Union[Integer, List[Integer]]] = None
    subEvents: Optional[Union["Event", List["Event"]]] = None
    startDate: Optional[Union[DateTime, List[DateTime]]] = None
    startDate: Optional[Union[Date, List[Date]]] = None
    superEvent: Optional[Union["Event", List["Event"]]] = None
    attendee: Optional[Union["Person", List["Person"]]] = None
    attendee: Optional[Union["Organization", List["Organization"]]] = None
    maximumVirtualAttendeeCapacity: Optional[Union[Integer, List[Integer]]] = None
    eventSchedule: Optional[Union["Schedule", List["Schedule"]]] = None
    contributor: Optional[Union["Organization", List["Organization"]]] = None
    contributor: Optional[Union["Person", List["Person"]]] = None
    eventStatus: Optional[Union["EventStatusType", List["EventStatusType"]]] = None
    keywords: Optional[Union[URL, List[URL]]] = None
    keywords: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    keywords: Optional[Union[Text, List[Text]]] = None
    attendees: Optional[Union["Organization", List["Organization"]]] = None
    attendees: Optional[Union["Person", List["Person"]]] = None
    previousStartDate: Optional[Union[Date, List[Date]]] = None
    maximumPhysicalAttendeeCapacity: Optional[Union[Integer, List[Integer]]] = None
    subEvent: Optional[Union["Event", List["Event"]]] = None
    workPerformed: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    offers: Optional[Union["Offer", List["Offer"]]] = None
    offers: Optional[Union["Demand", List["Demand"]]] = None
    workFeatured: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    isAccessibleForFree: Optional[Union[Boolean, List[Boolean]]] = None
    performers: Optional[Union["Person", List["Person"]]] = None
    performers: Optional[Union["Organization", List["Organization"]]] = None
    translator: Optional[Union["Person", List["Person"]]] = None
    translator: Optional[Union["Organization", List["Organization"]]] = None
    composer: Optional[Union["Person", List["Person"]]] = None
    composer: Optional[Union["Organization", List["Organization"]]] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    endDate: Optional[Union[Date, List[Date]]] = None
    endDate: Optional[Union[DateTime, List[DateTime]]] = None
    recordedIn: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    actor: Optional[Union["Person", List["Person"]]] = None
    actor: Optional[Union["PerformingGroup", List["PerformingGroup"]]] = None
    maximumAttendeeCapacity: Optional[Union[Integer, List[Integer]]] = None
