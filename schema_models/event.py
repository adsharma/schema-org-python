from dataclasses import dataclass
from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration
from schema_models.thing import Thing


@dataclass
class Event(Thing):
    """
    Upcoming or past event associated with this place, organization, or action.
    """

    about: Optional[Union[Thing, List[Thing]]] = None
    actor: Optional[
        Union["PerformingGroup", List["PerformingGroup"], "Person", List["Person"]]
    ] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    attendee: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    attendees: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    audience: Optional[Union["Audience", List["Audience"]]] = None
    composer: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    contributor: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    director: Optional[Union["Person", List["Person"]]] = None
    doorTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    duration: Optional[
        Union[Duration, List[Duration], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    endDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    eventAttendanceMode: Optional[
        Union["EventAttendanceModeEnumeration", List["EventAttendanceModeEnumeration"]]
    ] = None
    eventSchedule: Optional[Union["Schedule", List["Schedule"]]] = None
    eventStatus: Optional[Union["EventStatusType", List["EventStatusType"]]] = None
    funder: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    hasParticipationOffer: Optional[Union["Offer", List["Offer"]]] = None
    hasSponsorshipOffer: Optional[Union["Offer", List["Offer"]]] = None
    inLanguage: Optional[Union["Language", List["Language"], str, List[str]]] = None
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = None
    keywords: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
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
    maximumAttendeeCapacity: Optional[Union[int, List[int]]] = None
    maximumPhysicalAttendeeCapacity: Optional[Union[int, List[int]]] = None
    maximumVirtualAttendeeCapacity: Optional[Union[int, List[int]]] = None
    offers: Optional[Union["Demand", List["Demand"], "Offer", List["Offer"]]] = None
    organizer: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    performer: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    performers: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    previousStartDate: Optional[Union[date, List[date], datetime, List[datetime]]] = (
        None
    )
    recordedIn: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    remainingAttendeeCapacity: Optional[Union[int, List[int]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    sponsor: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    subEvent: Optional[Union["Event", List["Event"]]] = None
    subEvents: Optional[Union["Event", List["Event"]]] = None
    superEvent: Optional[Union["Event", List["Event"]]] = None
    translator: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    typicalAgeRange: Optional[Union[str, List[str]]] = None
    workFeatured: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    workPerformed: Optional[Union[CreativeWork, List[CreativeWork]]] = None
