from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization


class NewsMediaOrganization(Organization):
    """
    A News/Media organization such as a newspaper or TV station.
    """

    diversityStaffingReport: Optional[
        Union[HttpUrl, List[HttpUrl], "Article", List["Article"]]
    ] = None
    ownershipFundingInfo: Optional[
        Union[
            CreativeWork,
            List[CreativeWork],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
            "AboutPage",
            List["AboutPage"],
        ]
    ] = None
    unnamedSourcesPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    noBylinesPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    verificationFactCheckingPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    actionableFeedbackPolicy: Optional[
        Union[HttpUrl, List[HttpUrl], CreativeWork, List[CreativeWork]]
    ] = None
    diversityPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    ethicsPolicy: Optional[
        Union[HttpUrl, List[HttpUrl], CreativeWork, List[CreativeWork]]
    ] = None
    correctionsPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    missionCoveragePrioritiesPolicy: Optional[
        Union[HttpUrl, List[HttpUrl], CreativeWork, List[CreativeWork]]
    ] = None
    masthead: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
