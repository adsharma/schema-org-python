from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.substance import Substance
from schema_models.text import Text


class DietarySupplement(Substance):
    activeIngredient: Optional[Union[Text, List[Text]]] = None
    isProprietary: Optional[Union[Boolean, List[Boolean]]] = None
    recommendedIntake: Optional[
        Union["RecommendedDoseSchedule", List["RecommendedDoseSchedule"]]
    ] = None
    mechanismOfAction: Optional[Union[Text, List[Text]]] = None
    targetPopulation: Optional[Union[Text, List[Text]]] = None
    proprietaryName: Optional[Union[Text, List[Text]]] = None
    maximumIntake: Optional[
        Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]
    ] = None
    legalStatus: Optional[Union["DrugLegalStatus", List["DrugLegalStatus"]]] = None
    legalStatus: Optional[Union["MedicalEnumeration", List["MedicalEnumeration"]]] = (
        None
    )
    legalStatus: Optional[Union[Text, List[Text]]] = None
    safetyConsideration: Optional[Union[Text, List[Text]]] = None
    nonProprietaryName: Optional[Union[Text, List[Text]]] = None
