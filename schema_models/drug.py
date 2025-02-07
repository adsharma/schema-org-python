from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.dose_schedule import DoseSchedule
from schema_models.drug_class import DrugClass
from schema_models.drug_legal_status import DrugLegalStatus
from schema_models.drug_pregnancy_category import DrugPregnancyCategory
from schema_models.drug_prescription_status import DrugPrescriptionStatus
from schema_models.drug_strength import DrugStrength
from schema_models.health_insurance_plan import HealthInsurancePlan
from schema_models.maximum_dose_schedule import MaximumDoseSchedule
from schema_models.medical_enumeration import MedicalEnumeration
from schema_models.substance import Substance
from schema_models.text import Text
from schema_models.url import URL


class Drug(Substance):
    dosageForm: Optional[Union[Text, List[Text]]] = None
    alcoholWarning: Optional[Union[Text, List[Text]]] = None
    mechanismOfAction: Optional[Union[Text, List[Text]]] = None
    interactingDrug: Optional[Union["Drug", List["Drug"]]] = None
    prescriptionStatus: Optional[
        Union[DrugPrescriptionStatus, List[DrugPrescriptionStatus]]
    ] = None
    prescriptionStatus: Optional[Union[Text, List[Text]]] = None
    relatedDrug: Optional[Union["Drug", List["Drug"]]] = None
    availableStrength: Optional[Union[DrugStrength, List[DrugStrength]]] = None
    clincalPharmacology: Optional[Union[Text, List[Text]]] = None
    rxcui: Optional[Union[Text, List[Text]]] = None
    administrationRoute: Optional[Union[Text, List[Text]]] = None
    maximumIntake: Optional[Union[MaximumDoseSchedule, List[MaximumDoseSchedule]]] = (
        None
    )
    legalStatus: Optional[Union[DrugLegalStatus, List[DrugLegalStatus]]] = None
    legalStatus: Optional[Union[MedicalEnumeration, List[MedicalEnumeration]]] = None
    legalStatus: Optional[Union[Text, List[Text]]] = None
    drugUnit: Optional[Union[Text, List[Text]]] = None
    pregnancyCategory: Optional[
        Union[DrugPregnancyCategory, List[DrugPregnancyCategory]]
    ] = None
    labelDetails: Optional[Union[URL, List[URL]]] = None
    overdosage: Optional[Union[Text, List[Text]]] = None
    warning: Optional[Union[Text, List[Text]]] = None
    warning: Optional[Union[URL, List[URL]]] = None
    proprietaryName: Optional[Union[Text, List[Text]]] = None
    nonProprietaryName: Optional[Union[Text, List[Text]]] = None
    activeIngredient: Optional[Union[Text, List[Text]]] = None
    prescribingInfo: Optional[Union[URL, List[URL]]] = None
    clinicalPharmacology: Optional[Union[Text, List[Text]]] = None
    isAvailableGenerically: Optional[Union[Boolean, List[Boolean]]] = None
    includedInHealthInsurancePlan: Optional[
        Union[HealthInsurancePlan, List[HealthInsurancePlan]]
    ] = None
    pregnancyWarning: Optional[Union[Text, List[Text]]] = None
    drugClass: Optional[Union[DrugClass, List[DrugClass]]] = None
    doseSchedule: Optional[Union[DoseSchedule, List[DoseSchedule]]] = None
    breastfeedingWarning: Optional[Union[Text, List[Text]]] = None
    isProprietary: Optional[Union[Boolean, List[Boolean]]] = None
    foodWarning: Optional[Union[Text, List[Text]]] = None
