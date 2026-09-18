from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.drug_class import DrugClass
from schema_models.health_insurance_plan import HealthInsurancePlan
from schema_models.product import Product


@dataclass
class Drug(Product):
    """
    Specifying a drug or medicine used in a medication procedure.
    """

    activeIngredient: Optional[Union[str, List[str]]] = None
    administrationRoute: Optional[Union[str, List[str]]] = None
    alcoholWarning: Optional[Union[str, List[str]]] = None
    availableStrength: Optional[Union["DrugStrength", List["DrugStrength"]]] = None
    breastfeedingWarning: Optional[Union[str, List[str]]] = None
    clincalPharmacology: Optional[Union[str, List[str]]] = None
    clinicalPharmacology: Optional[Union[str, List[str]]] = None
    dosageForm: Optional[Union[str, List[str]]] = None
    doseSchedule: Optional[Union["DoseSchedule", List["DoseSchedule"]]] = None
    drugClass: Optional[Union[DrugClass, List[DrugClass]]] = None
    drugUnit: Optional[Union[str, List[str]]] = None
    foodWarning: Optional[Union[str, List[str]]] = None
    includedInHealthInsurancePlan: Optional[
        Union[HealthInsurancePlan, List[HealthInsurancePlan]]
    ] = None
    interactingDrug: Optional[Union["Drug", List["Drug"]]] = None
    isAvailableGenerically: Optional[Union[bool, List[bool]]] = None
    isProprietary: Optional[Union[bool, List[bool]]] = None
    labelDetails: Optional[Union[HttpUrl, List[HttpUrl]]] = None
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
    maximumIntake: Optional[
        Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]
    ] = None
    mechanismOfAction: Optional[Union[str, List[str]]] = None
    nonProprietaryName: Optional[Union[str, List[str]]] = None
    overdosage: Optional[Union[str, List[str]]] = None
    pregnancyCategory: Optional[
        Union["DrugPregnancyCategory", List["DrugPregnancyCategory"]]
    ] = None
    pregnancyWarning: Optional[Union[str, List[str]]] = None
    prescribingInfo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    prescriptionStatus: Optional[
        Union["DrugPrescriptionStatus", List["DrugPrescriptionStatus"], str, List[str]]
    ] = None
    proprietaryName: Optional[Union[str, List[str]]] = None
    relatedDrug: Optional[Union["Drug", List["Drug"]]] = None
    rxcui: Optional[Union[str, List[str]]] = None
    warning: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
