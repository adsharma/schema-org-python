from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.article import Article
from schema_models.creative_work import CreativeWork


class SocialMediaPosting(Article):
    sharedContent: Optional[Union[CreativeWork, List[CreativeWork]]] = None
