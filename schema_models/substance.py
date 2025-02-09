from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class Substance(MedicalEntity):
    activeIngredient: Optional[Union[str, List[str]]] = None
    maximumIntake: Optional[
        Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]
    ] = None
