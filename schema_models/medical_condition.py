from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.drug_class import DrugClass
from schema_models.lifestyle_modification import LifestyleModification
from schema_models.medical_cause import MedicalCause
from schema_models.medical_entity import MedicalEntity


@dataclass
class MedicalCondition(MedicalEntity):
    """
    Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc.
    """

    associatedAnatomy: Optional[
        Union[
            AnatomicalStructure,
            List[AnatomicalStructure],
            AnatomicalSystem,
            List[AnatomicalSystem],
            "SuperficialAnatomy",
            List["SuperficialAnatomy"],
        ]
    ] = None
    cause: Optional[Union[MedicalCause, List[MedicalCause]]] = None
    differentialDiagnosis: Optional[Union["DDxElement", List["DDxElement"]]] = None
    drug: Optional[Union["Drug", List["Drug"]]] = None
    epidemiology: Optional[Union[str, List[str]]] = None
    expectedPrognosis: Optional[Union[str, List[str]]] = None
    naturalProgression: Optional[Union[str, List[str]]] = None
    pathophysiology: Optional[Union[str, List[str]]] = None
    possibleComplication: Optional[Union[str, List[str]]] = None
    possibleTreatment: Optional[
        Union[
            "Drug",
            List["Drug"],
            DrugClass,
            List[DrugClass],
            LifestyleModification,
            List[LifestyleModification],
            "MedicalTherapy",
            List["MedicalTherapy"],
        ]
    ] = None
    primaryPrevention: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = None
    riskFactor: Optional[Union["MedicalRiskFactor", List["MedicalRiskFactor"]]] = None
    secondaryPrevention: Optional[
        Union[
            "Drug",
            List["Drug"],
            DrugClass,
            List[DrugClass],
            LifestyleModification,
            List[LifestyleModification],
            "MedicalTherapy",
            List["MedicalTherapy"],
        ]
    ] = None
    signOrSymptom: Optional[
        Union["MedicalSignOrSymptom", List["MedicalSignOrSymptom"]]
    ] = None
    stage: Optional[Union["MedicalConditionStage", List["MedicalConditionStage"]]] = (
        None
    )
    status: Optional[
        Union[
            "EventStatusType",
            List["EventStatusType"],
            "MedicalStudyStatus",
            List["MedicalStudyStatus"],
            str,
            List[str],
        ]
    ] = None
    typicalTest: Optional[Union["MedicalTest", List["MedicalTest"]]] = None
