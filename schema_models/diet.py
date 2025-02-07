from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.text import Text


class Diet(CreativeWork):
    dietFeatures: Optional[Union[Text, List[Text]]] = None
    endorsers: Optional[Union[Person, List[Person]]] = None
    endorsers: Optional[Union[Organization, List[Organization]]] = None
    expertConsiderations: Optional[Union[Text, List[Text]]] = None
    physiologicalBenefits: Optional[Union[Text, List[Text]]] = None
    risks: Optional[Union[Text, List[Text]]] = None
