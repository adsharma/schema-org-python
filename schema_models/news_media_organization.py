from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.article import Article
from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization


@dataclass
class NewsMediaOrganization(Organization):
    """
    A News/Media organization such as a newspaper or TV station.
    """

    actionableFeedbackPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    correctionsPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    diversityPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    diversityStaffingReport: Optional[
        Union[Article, List[Article], HttpUrl, List[HttpUrl]]
    ] = None
    ethicsPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    masthead: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    missionCoveragePrioritiesPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    noBylinesPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    ownershipFundingInfo: Optional[
        Union[
            "AboutPage",
            List["AboutPage"],
            CreativeWork,
            List[CreativeWork],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    unnamedSourcesPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
    verificationFactCheckingPolicy: Optional[
        Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]
    ] = None
