from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.medical_intangible import MedicalIntangible
from schema_models.number import Number
from schema_models.text import Text


class DrugStrength(MedicalIntangible):
    strengthUnit: Optional[Union[Text, List[Text]]] = None
    strengthValue: Optional[Union[Number, List[Number]]] = None
    maximumIntake: Optional[
        Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]
    ] = None
    availableIn: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = None
    activeIngredient: Optional[Union[Text, List[Text]]] = None
