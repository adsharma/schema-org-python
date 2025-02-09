from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.speakable_specification import SpeakableSpecification
from schema_models.web_page_element import WebPageElement


class WebPage(CreativeWork):
    mainContentOfPage: Optional[Union[WebPageElement, List[WebPageElement]]] = None
    significantLinks: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    primaryImageOfPage: Optional[Union["ImageObject", List["ImageObject"]]] = None
    lastReviewed: Optional[Union[date, List[date]]] = None
    significantLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    specialty: Optional[Union["Specialty", List["Specialty"]]] = None
    relatedLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    speakable: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    speakable: Optional[Union[SpeakableSpecification, List[SpeakableSpecification]]] = (
        None
    )
    reviewedBy: Optional[Union[Person, List[Person]]] = None
    reviewedBy: Optional[Union[Organization, List[Organization]]] = None
    breadcrumb: Optional[Union["BreadcrumbList", List["BreadcrumbList"]]] = None
    breadcrumb: Optional[Union[str, List[str]]] = None
