from typing import List, Optional, Union

from schema_models.medical_contraindication import MedicalContraindication
from schema_models.medical_entity import MedicalEntity


class MedicalDevice(MedicalEntity):
    procedure: Optional[Union[str, List[str]]] = None
    adverseOutcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    postOp: Optional[Union[str, List[str]]] = None
    seriousAdverseOutcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    contraindication: Optional[Union[str, List[str]]] = None
    contraindication: Optional[
        Union[MedicalContraindication, List[MedicalContraindication]]
    ] = None
    preOp: Optional[Union[str, List[str]]] = None
