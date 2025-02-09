from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition


class InfectiousDisease(MedicalCondition):
    infectiousAgentClass: Optional[
        Union["InfectiousAgentClass", List["InfectiousAgentClass"]]
    ] = None
    infectiousAgent: Optional[Union[str, List[str]]] = None
    transmissionMethod: Optional[Union[str, List[str]]] = None
