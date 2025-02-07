from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition
from schema_models.text import Text


class InfectiousDisease(MedicalCondition):
    infectiousAgentClass: Optional[
        Union["InfectiousAgentClass", List["InfectiousAgentClass"]]
    ] = None
    infectiousAgent: Optional[Union[Text, List[Text]]] = None
    transmissionMethod: Optional[Union[Text, List[Text]]] = None
