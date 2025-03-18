from typing import List, Optional, Union

from schema_models.medical_intangible import MedicalIntangible


class DoseSchedule(MedicalIntangible):
    """
    A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.
    """

    doseValue: Optional[
        Union[float, List[float], "QualitativeValue", List["QualitativeValue"]]
    ] = None
    frequency: Optional[Union[str, List[str]]] = None
    targetPopulation: Optional[Union[str, List[str]]] = None
    doseUnit: Optional[Union[str, List[str]]] = None
