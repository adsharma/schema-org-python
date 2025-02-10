from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.medical_intangible import MedicalIntangible


class DrugStrength(MedicalIntangible):
    """
    A specific strength in which a medical drug is available in a specific country.
    """

    strengthUnit: Optional[Union[str, List[str]]] = None
    strengthValue: Optional[Union[float, List[float]]] = None
    maximumIntake: Optional[
        Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]
    ] = None
    availableIn: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    activeIngredient: Optional[Union[str, List[str]]] = None
