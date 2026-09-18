from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.action import Action


@dataclass
class ConsumeAction(Action):
    """
    The act of ingesting information/resources/food.
    """

    actionAccessibilityRequirement: Optional[
        Union["ActionAccessSpecification", List["ActionAccessSpecification"]]
    ] = None
    expectsAcceptanceOf: Optional[Union["Offer", List["Offer"]]] = None
