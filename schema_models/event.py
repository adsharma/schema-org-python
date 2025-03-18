from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.thing import Thing


class Event(Thing):
    """
    Upcoming or past event associated with this place, organization, or action.
    """

    eventAttendanceMode: Optional[
        Union["EventAttendanceModeEnumeration", List["EventAttendanceModeEnumeration"]]
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
    duration: Optional[Union["Duration", List["Duration"]]] = None
    doorTime: Optional[Union[datetime, List[datetime], time, List[time]]] = None
    director: Optional[Union["Person", List["Person"]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    organizer: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    sponsor: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    typicalAgeRange: Optional[Union[str, List[str]]] = None
    about: Optional[Union[Thing, List[Thing]]] = None
    funder: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    audience: Optional[Union["Audience", List["Audience"]]] = None
    performer: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    review: Optional[Union["Review", List["Review"]]] = None
    inLanguage: Optional[Union["Language", List["Language"], str, List[str]]] = None
    remainingAttendeeCapacity: Optional[Union[int, List[int]]] = None
    subEvents: Optional[Union["Event", List["Event"]]] = None
    startDate: Optional[Union[datetime, List[datetime], date, List[date]]] = None
    superEvent: Optional[Union["Event", List["Event"]]] = None
    attendee: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    maximumVirtualAttendeeCapacity: Optional[Union[int, List[int]]] = None
    eventSchedule: Optional[Union["Schedule", List["Schedule"]]] = None
    contributor: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    eventStatus: Optional[Union["EventStatusType", List["EventStatusType"]]] = None
    keywords: Optional[
        Union[
            HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"], str, List[str]
        ]
    ] = None
    attendees: Optional[
        Union["Organization", List["Organization"], "Person", List["Person"]]
    ] = None
    previousStartDate: Optional[Union[date, List[date]]] = None
    maximumPhysicalAttendeeCapacity: Optional[Union[int, List[int]]] = None
    subEvent: Optional[Union["Event", List["Event"]]] = None
    workPerformed: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    offers: Optional[Union["Offer", List["Offer"], "Demand", List["Demand"]]] = None
    workFeatured: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = None
    performers: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    translator: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    composer: Optional[
        Union["Person", List["Person"], "Organization", List["Organization"]]
    ] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    endDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    recordedIn: Optional[Union["CreativeWork", List["CreativeWork"]]] = None
    actor: Optional[
        Union["Person", List["Person"], "PerformingGroup", List["PerformingGroup"]]
    ] = None
    maximumAttendeeCapacity: Optional[Union[int, List[int]]] = None
