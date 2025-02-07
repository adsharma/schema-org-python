from typing import List, Optional, Union

from schema_models.anatomical_system import AnatomicalSystem
from schema_models.medical_entity import MedicalEntity
from schema_models.text import Text


class MedicalCondition(MedicalEntity):
    epidemiology: Optional[Union[Text, List[Text]]] = None
    stage: Optional[Union["MedicalConditionStage", List["MedicalConditionStage"]]] = (
        None
    )
    riskFactor: Optional[Union["MedicalRiskFactor", List["MedicalRiskFactor"]]] = None
    possibleComplication: Optional[Union[Text, List[Text]]] = None
    associatedAnatomy: Optional[
        Union["AnatomicalStructure", List["AnatomicalStructure"]]
    ] = None
    associatedAnatomy: Optional[Union[AnatomicalSystem, List[AnatomicalSystem]]] = None
    associatedAnatomy: Optional[
        Union["SuperficialAnatomy", List["SuperficialAnatomy"]]
    ] = None
    differentialDiagnosis: Optional[Union["DDxElement", List["DDxElement"]]] = None
    typicalTest: Optional[Union["MedicalTest", List["MedicalTest"]]] = None
    drug: Optional[Union["Drug", List["Drug"]]] = None
    pathophysiology: Optional[Union[Text, List[Text]]] = None
    signOrSymptom: Optional[
        Union["MedicalSignOrSymptom", List["MedicalSignOrSymptom"]]
    ] = None
    expectedPrognosis: Optional[Union[Text, List[Text]]] = None
    possibleTreatment: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
    naturalProgression: Optional[Union[Text, List[Text]]] = None
    status: Optional[Union["MedicalStudyStatus", List["MedicalStudyStatus"]]] = None
    status: Optional[Union[Text, List[Text]]] = None
    status: Optional[Union["EventStatusType", List["EventStatusType"]]] = None
    primaryPrevention: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
    secondaryPrevention: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = (
        None
    )
