from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.medical_contraindication import MedicalContraindication
from schema_models.medical_entity import MedicalEntity
from schema_models.therapeutic_procedure import TherapeuticProcedure


@dataclass
class MedicalTherapy(TherapeuticProcedure):
    """
    Any medical intervention designed to prevent, treat, and cure human diseases and medical conditions, including both curative and palliative therapies. Medical therapies are typically processes of care relying upon pharmacotherapy, behavioral therapy, supportive therapy (with fluid or nutrition for example), or detoxification (e.g. hemodialysis) aimed at improving or preventing a health condition.
    """

    contraindication: Optional[
        Union[MedicalContraindication, List[MedicalContraindication], str, List[str]]
    ] = None
    duplicateTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
    seriousAdverseOutcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
