from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person


class Quotation(CreativeWork):
    """
    A quotation. Often but not necessarily from some written work, attributable to a real world author and - if associated with a fictional character - to any fictional Person. Use [[isBasedOn]] to link to source/origin. The [[recordedIn]] property can be used to reference a Quotation from an [[Event]].
    """

    spokenByCharacter: Optional[Union[Organization, List[Organization]]] = None
    spokenByCharacter: Optional[Union[Person, List[Person]]] = None
