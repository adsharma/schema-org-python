from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.thing import Thing


@dataclass
class StupidType(Thing):
    """
    A StupidType for testing.
    """

    stupidProperty: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
