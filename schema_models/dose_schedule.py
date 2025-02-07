from typing import List, Optional, Union

from schema_models.medical_intangible import MedicalIntangible
from schema_models.number import Number
from schema_models.qualitative_value import QualitativeValue
from schema_models.text import Text


class DoseSchedule(MedicalIntangible):
    doseValue: Optional[Union[Number, List[Number]]] = None
    doseValue: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    frequency: Optional[Union[Text, List[Text]]] = None
    targetPopulation: Optional[Union[Text, List[Text]]] = None
    doseUnit: Optional[Union[Text, List[Text]]] = None
