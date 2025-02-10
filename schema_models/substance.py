from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class Substance(MedicalEntity):
    """
    Any matter of defined composition that has discrete existence, whose origin may be biological, mineral or chemical.
    """

    activeIngredient: Optional[Union[str, List[str]]] = None
    maximumIntake: Optional[
        Union["MaximumDoseSchedule", List["MaximumDoseSchedule"]]
    ] = None
