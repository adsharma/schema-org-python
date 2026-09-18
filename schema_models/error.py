from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.defined_term import DefinedTerm
from schema_models.instantaneous_event import InstantaneousEvent
from schema_models.status_enumeration import StatusEnumeration


@dataclass
class Error(InstantaneousEvent):
    """
    For failed actions, more information on the cause of the failure. Consider using the Error type.
    """

    errorCode: Optional[
        Union[
            DefinedTerm,
            List[DefinedTerm],
            int,
            List[int],
            StatusEnumeration,
            List[StatusEnumeration],
            str,
            List[str],
        ]
    ] = None
