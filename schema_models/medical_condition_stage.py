from typing import List, Optional, Union

from schema_models.medical_intangible import MedicalIntangible


class MedicalConditionStage(MedicalIntangible):
    """
    A stage of a medical condition, such as 'Stage IIIa'.
    """

    stageAsNumber: Optional[Union[float, List[float]]] = None
    subStageSuffix: Optional[Union[str, List[str]]] = None
