from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.drug_class import DrugClass
from schema_models.health_insurance_plan import HealthInsurancePlan
from schema_models.substance import Substance


class Drug(Substance):
    """
    Specifying a drug or medicine used in a medication procedure.
    """

    dosageForm: Optional[Union[str, List[str]]] = None
    alcoholWarning: Optional[Union[str, List[str]]] = None
    mechanismOfAction: Optional[Union[str, List[str]]] = None
    interactingDrug: Optional[Union["Drug", List["Drug"]]] = None
    prescriptionStatus: Optional[
        Union["DrugPrescriptionStatus", List["DrugPrescriptionStatus"]]
    ] = None
    prescriptionStatus: Optional[Union[str, List[str]]] = None
    relatedDrug: Optional[Union["Drug", List["Drug"]]] = None
    availableStrength: Optional[Union["DrugStrength", List["DrugStrength"]]] = None
    clincalPharmacology: Optional[Union[str, List[str]]] = None
    rxcui: Optional[Union[str, List[str]]] = None
    administrationRoute: Optional[Union[str, List[str]]] = None
    maximumIntake: Optional[
        Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]
    ] = None
    legalStatus: Optional[Union["DrugLegalStatus", List["DrugLegalStatus"]]] = None
    legalStatus: Optional[Union["MedicalEnumeration", List["MedicalEnumeration"]]] = (
        None
    )
    legalStatus: Optional[Union[str, List[str]]] = None
    drugUnit: Optional[Union[str, List[str]]] = None
    pregnancyCategory: Optional[
        Union["DrugPregnancyCategory", List["DrugPregnancyCategory"]]
    ] = None
    labelDetails: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    overdosage: Optional[Union[str, List[str]]] = None
    warning: Optional[Union[str, List[str]]] = None
    warning: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    proprietaryName: Optional[Union[str, List[str]]] = None
    nonProprietaryName: Optional[Union[str, List[str]]] = None
    activeIngredient: Optional[Union[str, List[str]]] = None
    prescribingInfo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    clinicalPharmacology: Optional[Union[str, List[str]]] = None
    isAvailableGenerically: Optional[Union[bool, List[bool]]] = None
    includedInHealthInsurancePlan: Optional[
        Union[HealthInsurancePlan, List[HealthInsurancePlan]]
    ] = None
    pregnancyWarning: Optional[Union[str, List[str]]] = None
    drugClass: Optional[Union[DrugClass, List[DrugClass]]] = None
    doseSchedule: Optional[Union["DoseSchedule", List["DoseSchedule"]]] = None
    breastfeedingWarning: Optional[Union[str, List[str]]] = None
    isProprietary: Optional[Union[bool, List[bool]]] = None
    foodWarning: Optional[Union[str, List[str]]] = None
