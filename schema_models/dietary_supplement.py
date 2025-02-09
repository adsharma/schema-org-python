from typing import List, Optional, Union

from schema_models.substance import Substance


class DietarySupplement(Substance):
    activeIngredient: Optional[Union[str, List[str]]] = None
    isProprietary: Optional[Union[bool, List[bool]]] = None
    recommendedIntake: Optional[
        Union["RecommendedDoseSchedule", List["RecommendedDoseSchedule"]]
    ] = None
    mechanismOfAction: Optional[Union[str, List[str]]] = None
    targetPopulation: Optional[Union[str, List[str]]] = None
    proprietaryName: Optional[Union[str, List[str]]] = None
    maximumIntake: Optional[
        Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]
    ] = None
    legalStatus: Optional[Union["DrugLegalStatus", List["DrugLegalStatus"]]] = None
    legalStatus: Optional[Union["MedicalEnumeration", List["MedicalEnumeration"]]] = (
        None
    )
    legalStatus: Optional[Union[str, List[str]]] = None
    safetyConsideration: Optional[Union[str, List[str]]] = None
    nonProprietaryName: Optional[Union[str, List[str]]] = None
