from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.social_media_posting import SocialMediaPosting


class BlogPosting(SocialMediaPosting):
    pass
