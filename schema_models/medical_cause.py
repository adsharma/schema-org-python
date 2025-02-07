from typing import List, Optional, Union

from schema_models.medical_entity import MedicalEntity


class MedicalCause(MedicalEntity):
    causeOf: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
