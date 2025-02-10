from typing import List, Optional, Union

from schema_models.administrative_area import AdministrativeArea
from schema_models.medical_intangible import MedicalIntangible


class DrugLegalStatus(MedicalIntangible):
    """
    The legal availability status of a medical drug.
    """

    applicableLocation: Optional[
        Union[AdministrativeArea, List[AdministrativeArea]]
    ] = None
