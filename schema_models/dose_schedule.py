from typing import List, Optional, Union

from schema_models.medical_intangible import MedicalIntangible


class DoseSchedule(MedicalIntangible):
    doseValue: Optional[Union[float, List[float]]] = None
    doseValue: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    frequency: Optional[Union[str, List[str]]] = None
    targetPopulation: Optional[Union[str, List[str]]] = None
    doseUnit: Optional[Union[str, List[str]]] = None
