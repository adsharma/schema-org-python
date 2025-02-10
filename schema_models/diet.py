from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person


class Diet(CreativeWork):
    """
    A strategy of regulating the intake of food to achieve or maintain a specific health-related goal.
    """

    dietFeatures: Optional[Union[str, List[str]]] = None
    endorsers: Optional[Union[Person, List[Person]]] = None
    endorsers: Optional[Union[Organization, List[Organization]]] = None
    expertConsiderations: Optional[Union[str, List[str]]] = None
    physiologicalBenefits: Optional[Union[str, List[str]]] = None
    risks: Optional[Union[str, List[str]]] = None
