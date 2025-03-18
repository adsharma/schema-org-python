from typing import List, Optional, Union

from schema_models.substance import Substance


class DietarySupplement(Substance):
    """
    A product taken by mouth that contains a dietary ingredient intended to supplement the diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals, amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites.
    """

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
    safetyConsideration: Optional[Union[str, List[str]]] = None
    nonProprietaryName: Optional[Union[str, List[str]]] = None
