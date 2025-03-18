from typing import List, Optional, Union

from schema_models.thing import Thing


class MedicalEntity(Thing):
    """
    The most generic type of entity related to health and the practice of medicine.
    """

    recognizingAuthority: Optional[Union["Organization", List["Organization"]]] = None
    relevantSpecialty: Optional[Union["MedicalSpecialty", List["MedicalSpecialty"]]] = (
        None
    )
    code: Optional[Union["MedicalCode", List["MedicalCode"]]] = None
    study: Optional[Union["MedicalStudy", List["MedicalStudy"]]] = None
    medicineSystem: Optional[Union["MedicineSystem", List["MedicineSystem"]]] = None
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
    funding: Optional[Union["Grant", List["Grant"]]] = None
    guideline: Optional[Union["MedicalGuideline", List["MedicalGuideline"]]] = None
