from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.assess_action import AssessAction
from schema_models.review import Review


class ReviewAction(AssessAction):
    resultReview: Optional[Union[Review, List[Review]]] = None
