from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class DrugClass(MedicalEntity):
    """
    The class of drug this belongs to (e.g., statins).
    """

    drug: Optional[Union["Drug", List["Drug"]]] = None
