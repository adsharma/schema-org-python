from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.review import Review
from schema_models.text import Text


class ClaimReview(Review):
    claimReviewed: Optional[Union[Text, List[Text]]] = None
