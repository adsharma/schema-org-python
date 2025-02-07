from typing import List, Optional, Union

from schema_models.about_page import AboutPage
from schema_models.article import Article
from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.text import Text
from schema_models.url import URL


class NewsMediaOrganization(Organization):
    diversityStaffingReport: Optional[Union[URL, List[URL]]] = None
    diversityStaffingReport: Optional[Union[Article, List[Article]]] = None
    ownershipFundingInfo: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    ownershipFundingInfo: Optional[Union[Text, List[Text]]] = None
    ownershipFundingInfo: Optional[Union[URL, List[URL]]] = None
    ownershipFundingInfo: Optional[Union[AboutPage, List[AboutPage]]] = None
    unnamedSourcesPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    unnamedSourcesPolicy: Optional[Union[URL, List[URL]]] = None
    noBylinesPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    noBylinesPolicy: Optional[Union[URL, List[URL]]] = None
    verificationFactCheckingPolicy: Optional[
        Union[CreativeWork, List[CreativeWork]]
    ] = None
    verificationFactCheckingPolicy: Optional[Union[URL, List[URL]]] = None
    actionableFeedbackPolicy: Optional[Union[URL, List[URL]]] = None
    actionableFeedbackPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    diversityPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    diversityPolicy: Optional[Union[URL, List[URL]]] = None
    ethicsPolicy: Optional[Union[URL, List[URL]]] = None
    ethicsPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    correctionsPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    correctionsPolicy: Optional[Union[URL, List[URL]]] = None
    missionCoveragePrioritiesPolicy: Optional[Union[URL, List[URL]]] = None
    missionCoveragePrioritiesPolicy: Optional[
        Union[CreativeWork, List[CreativeWork]]
    ] = None
    masthead: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    masthead: Optional[Union[URL, List[URL]]] = None
