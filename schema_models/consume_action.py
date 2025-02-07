from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.action import Action
from schema_models.action_access_specification import ActionAccessSpecification
from schema_models.offer import Offer


class ConsumeAction(Action):
    expectsAcceptanceOf: Optional[Union[Offer, List[Offer]]] = None
    actionAccessibilityRequirement: Optional[
        Union[ActionAccessSpecification, List[ActionAccessSpecification]]
    ] = None
