from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class DrugClass(MedicalEntity):
    drug: Optional[Union["Drug", List["Drug"]]] = None
