from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization


class NewsMediaOrganization(Organization):
    """
    A News/Media organization such as a newspaper or TV station.
    """

    diversityStaffingReport: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    diversityStaffingReport: Optional[Union["Article", List["Article"]]] = None
    ownershipFundingInfo: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    ownershipFundingInfo: Optional[Union[str, List[str]]] = None
    ownershipFundingInfo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    ownershipFundingInfo: Optional[Union["AboutPage", List["AboutPage"]]] = None
    unnamedSourcesPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    unnamedSourcesPolicy: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    noBylinesPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    noBylinesPolicy: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    verificationFactCheckingPolicy: Optional[
        Union[CreativeWork, List[CreativeWork]]
    ] = None
    verificationFactCheckingPolicy: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    actionableFeedbackPolicy: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    actionableFeedbackPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    diversityPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    diversityPolicy: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    ethicsPolicy: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    ethicsPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    correctionsPolicy: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    correctionsPolicy: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    missionCoveragePrioritiesPolicy: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    missionCoveragePrioritiesPolicy: Optional[
        Union[CreativeWork, List[CreativeWork]]
    ] = None
    masthead: Optional[Union[CreativeWork, List[CreativeWork]]] = None
    masthead: Optional[Union[HttpUrl, List[HttpUrl]]] = None
