from typing import List, Optional, Union

from schema_models.drug_legal_status import DrugLegalStatus
from schema_models.grant import Grant
from schema_models.medical_code import MedicalCode
from schema_models.medical_enumeration import MedicalEnumeration
from schema_models.medical_guideline import MedicalGuideline
from schema_models.medical_specialty import MedicalSpecialty
from schema_models.medical_study import MedicalStudy
from schema_models.medicine_system import MedicineSystem
from schema_models.organization import Organization
from schema_models.text import Text
from schema_models.thing import Thing


class MedicalEntity(Thing):
    recognizingAuthority: Optional[Union[Organization, List[Organization]]] = None
    relevantSpecialty: Optional[Union[MedicalSpecialty, List[MedicalSpecialty]]] = None
    code: Optional[Union[MedicalCode, List[MedicalCode]]] = None
    study: Optional[Union[MedicalStudy, List[MedicalStudy]]] = None
    medicineSystem: Optional[Union[MedicineSystem, List[MedicineSystem]]] = None
    legalStatus: Optional[Union[DrugLegalStatus, List[DrugLegalStatus]]] = None
    legalStatus: Optional[Union[MedicalEnumeration, List[MedicalEnumeration]]] = None
    legalStatus: Optional[Union[Text, List[Text]]] = None
    funding: Optional[Union[Grant, List[Grant]]] = None
    guideline: Optional[Union[MedicalGuideline, List[MedicalGuideline]]] = None
