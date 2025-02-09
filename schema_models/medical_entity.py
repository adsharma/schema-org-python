from typing import List, Optional, Union

from schema_models.thing import Thing


class MedicalEntity(Thing):
    recognizingAuthority: Optional[Union["Organization", List["Organization"]]] = None
    relevantSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = (
        None
    )
    code: Optional[Union["MedicalCode", List["MedicalCode"]]] = None
    study: Optional[Union["MedicalStudy", List["MedicalStudy"]]] = None
    medicineSystem: Optional[Union["MedicineSystem", List["MedicineSystem"]]] = None
    legalStatus: Optional[Union["DrugLegalStatus", List["DrugLegalStatus"]]] = None
    legalStatus: Optional[Union["MedicalEnumeration", List["MedicalEnumeration"]]] = (
        None
    )
    legalStatus: Optional[Union[str, List[str]]] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    guideline: Optional[Union["MedicalGuideline", List["MedicalGuideline"]]] = None
