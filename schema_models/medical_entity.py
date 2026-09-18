from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.thing import Thing


@dataclass
class MedicalEntity(Thing):
    """
    The most generic type of entity related to health and the practice of medicine.
    """

    code: Optional[Union["MedicalCode", List["MedicalCode"]]] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    guideline: Optional[Union["MedicalGuideline", List["MedicalGuideline"]]] = None
    legalStatus: Optional[
        Union[
            "DrugLegalStatus",
            List["DrugLegalStatus"],
            "MedicalEnumeration",
            List["MedicalEnumeration"],
            str,
            List[str],
        ]
    ] = None
    medicineSystem: Optional[Union["MedicineSystem", List["MedicineSystem"]]] = None
    recognizingAuthority: Optional[Union["Organization", List["Organization"]]] = None
    relevantSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = (
        None
    )
    study: Optional[Union["MedicalStudy", List["MedicalStudy"]]] = None
