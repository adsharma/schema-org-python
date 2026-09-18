from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.transfer_action import TransferAction


@dataclass
class GiveAction(TransferAction):
    """
    The act of transferring ownership of an object to a destination. Reciprocal of TakeAction.

    Related actions:

    * [[TakeAction]]: Reciprocal of GiveAction.
    * [[SendAction]]: Unlike SendAction, GiveAction implies that ownership is being transferred (e.g. I may send my laptop to you, but that doesn't mean I'm giving it to you).
    """

    recipient: Optional[
        Union[
            Audience,
            List[Audience],
            "ContactPoint",
            List["ContactPoint"],
            Organization,
            List[Organization],
            Person,
            List[Person],
        ]
    ] = None
