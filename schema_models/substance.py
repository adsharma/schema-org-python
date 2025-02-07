from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity
from schema_models.text import Text


class Substance(MedicalEntity):
    activeIngredient: Optional[Union[Text, List[Text]]] = None
    maximumIntake: Optional[
        Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]
    ] = None
