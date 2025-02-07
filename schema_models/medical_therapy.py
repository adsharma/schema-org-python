from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_contraindication import MedicalContraindication
from schema_models.medical_entity import MedicalEntity
from schema_models.medical_therapy import MedicalTherapy
from schema_models.text import Text
from schema_models.therapeutic_procedure import TherapeuticProcedure


class MedicalTherapy(TherapeuticProcedure):
    seriousAdverseOutcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    contraindication: Optional[Union[Text, List[Text]]] = None
    contraindication: Optional[
        Union[MedicalContraindication, List[MedicalContraindication]]
    ] = None
    duplicateTherapy: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
