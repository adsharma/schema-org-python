from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition


class InfectiousDisease(MedicalCondition):
    """
    An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease.
    """

    infectiousAgentClass: Optional[
        Union["InfectiousAgentClass", List["InfectiousAgentClass"]]
    ] = None
    infectiousAgent: Optional[Union[str, List[str]]] = None
    transmissionMethod: Optional[Union[str, List[str]]] = None
