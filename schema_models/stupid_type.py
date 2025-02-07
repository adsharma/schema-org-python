from typing import List, Optional, Union

from schema_models.thing import Thing


class StupidType(Thing):
    stupidProperty: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
