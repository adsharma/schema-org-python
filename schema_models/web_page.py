from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.speakable_specification import SpeakableSpecification
from schema_models.web_page_element import WebPageElement


class WebPage(CreativeWork):
    """
    A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.
    """

    mainContentOfPage: Optional[Union[WebPageElement, List[WebPageElement]]] = None
    significantLinks: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    primaryImageOfPage: Optional[Union["ImageObject", List["ImageObject"]]] = None
    lastReviewed: Optional[Union[date, List[date]]] = None
    significantLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    specialty: Optional[Union["Specialty", List["Specialty"]]] = None
    relatedLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    speakable: Optional[
        Union[
            HttpUrl, List[HttpUrl], SpeakableSpecification, List[SpeakableSpecification]
        ]
    ] = None
    reviewedBy: Optional[
        Union[Person, List[Person], Organization, List[Organization]]
    ] = None
    breadcrumb: Optional[
        Union["BreadcrumbList", List["BreadcrumbList"], str, List[str]]
    ] = None
