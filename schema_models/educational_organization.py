from typing import List, Optional, Union

from schema_models.civic_structure import CivicStructure
from schema_models.person import Person


class EducationalOrganization(CivicStructure):
    """
    An educational organization.
    """

    alumni: Optional[Union[Person, List[Person]]] = None
