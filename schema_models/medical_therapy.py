from typing import List, Optional, Union

from schema_models.medical_contraindication import MedicalContraindication
from schema_models.medical_entity import MedicalEntity
from schema_models.therapeutic_procedure import TherapeuticProcedure


class MedicalTherapy(TherapeuticProcedure):
    seriousAdverseOutcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    contraindication: Optional[Union[str, List[str]]] = None
    contraindication: Optional[
        Union[MedicalContraindication, List[MedicalContraindication]]
    ] = None
    duplicateTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
