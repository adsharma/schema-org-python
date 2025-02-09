from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.thing import Thing


class Event(Thing):
    eventAttendanceMode: Optional[
        Union["EventAttendanceModeEnumeration", List["EventAttendanceModeEnumeration"]]
    ] = None
    location: Optional[Union[str, List[str]]] = None
    location: Optional[Union["Place", List["Place"]]] = None
    location: Optional[Union["VirtualLocation", List["VirtualLocation"]]] = None
    location: Optional[Union["PostalAddress", List["PostalAddress"]]] = None
    duration: Optional[Union["Duration", List["Duration"]]] = None
    doorTime: Optional[Union[datetime, List[datetime]]] = None
    doorTime: Optional[Union[time, List[time]]] = None
    director: Optional[Union["Person", List["Person"]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    organizer: Optional[Union["Person", List["Person"]]] = None
    organizer: Optional[Union["Organization", List["Organization"]]] = None
    sponsor: Optional[Union["Person", List["Person"]]] = None
    sponsor: Optional[Union["Organization", List["Organization"]]] = None
    typicalAgeRange: Optional[Union[str, List[str]]] = None
    about: Optional[Union[Thing, List[Thing]]] = None
    funder: Optional[Union["Person", List["Person"]]] = None
    funder: Optional[Union["Organization", List["Organization"]]] = None
    audience: Optional[Union["Audience", List["Audience"]]] = None
    performer: Optional[Union["Person", List["Person"]]] = None
    performer: Optional[Union["Organization", List["Organization"]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    inLanguage: Optional[Union["Language", List["Language"]]] = None
    inLanguage: Optional[Union[str, List[str]]] = None
    remainingAttendeeCapacity: Optional[Union[int, List[int]]] = None
    subEvents: Optional[Union["Event", List["Event"]]] = None
    startDate: Optional[Union[datetime, List[datetime]]] = None
    startDate: Optional[Union[date, List[date]]] = None
    superEvent: Optional[Union["Event", List["Event"]]] = None
    attendee: Optional[Union["Person", List["Person"]]] = None
    attendee: Optional[Union["Organization", List["Organization"]]] = None
    maximumVirtualAttendeeCapacity: Optional[Union[int, List[int]]] = None
    eventSchedule: Optional[Union["Schedule", List["Schedule"]]] = None
    contributor: Optional[Union["Organization", List["Organization"]]] = None
    contributor: Optional[Union["Person", List["Person"]]] = None
    eventStatus: Optional[Union["EventStatusType", List["EventStatusType"]]] = None
    keywords: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    keywords: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    keywords: Optional[Union[str, List[str]]] = None
    attendees: Optional[Union["Organization", List["Organization"]]] = None
    attendees: Optional[Union["Person", List["Person"]]] = None
    previousStartDate: Optional[Union[date, List[date]]] = None
    maximumPhysicalAttendeeCapacity: Optional[Union[int, List[int]]] = None
    subEvent: Optional[Union["Event", List["Event"]]] = None
    workPerformed: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    offers: Optional[Union["Offer", List["Offer"]]] = None
    offers: Optional[Union["Demand", List["Demand"]]] = None
    workFeatured: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = None
    performers: Optional[Union["Person", List["Person"]]] = None
    performers: Optional[Union["Organization", List["Organization"]]] = None
    translator: Optional[Union["Person", List["Person"]]] = None
    translator: Optional[Union["Organization", List["Organization"]]] = None
    composer: Optional[Union["Person", List["Person"]]] = None
    composer: Optional[Union["Organization", List["Organization"]]] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    endDate: Optional[Union[date, List[date]]] = None
    endDate: Optional[Union[datetime, List[datetime]]] = None
    recordedIn: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    actor: Optional[Union["Person", List["Person"]]] = None
    actor: Optional[Union["PerformingGroup", List["PerformingGroup"]]] = None
    maximumAttendeeCapacity: Optional[Union[int, List[int]]] = None
