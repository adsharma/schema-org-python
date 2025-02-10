from typing import List, Optional, Union

from schema_models.medical_condition import MedicalCondition
from schema_models.medical_intangible import MedicalIntangible
from schema_models.medical_sign_or_symptom import MedicalSignOrSymptom


class DDxElement(MedicalIntangible):
    """
    An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.
    """

    diagnosis: Optional[Union[MedicalCondition, List[MedicalCondition]]] = None
    distinguishingSign: Optional[
        Union[MedicalSignOrSymptom, List[MedicalSignOrSymptom]]
    ] = None
