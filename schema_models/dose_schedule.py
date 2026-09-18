from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.medical_intangible import MedicalIntangible
from schema_models.qualitative_value import QualitativeValue


@dataclass
class DoseSchedule(MedicalIntangible):
    """
    A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.
    """

    doseUnit: Optional[Union[str, List[str]]] = None
    doseValue: Optional[
        Union[float, List[float], QualitativeValue, List[QualitativeValue]]
    ] = None
    frequency: Optional[Union[str, List[str]]] = None
    targetPopulation: Optional[Union[str, List[str]]] = None
