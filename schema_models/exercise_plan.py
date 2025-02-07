from typing import List, Optional, Union

from schema_models.duration import Duration
from schema_models.energy import Energy
from schema_models.number import Number
from schema_models.physical_activity import PhysicalActivity
from schema_models.quantitative_value import QuantitativeValue
from schema_models.text import Text


class ExercisePlan(PhysicalActivity):
    additionalVariable: Optional[Union[Text, List[Text]]] = None
    exerciseType: Optional[Union[Text, List[Text]]] = None
    restPeriods: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    restPeriods: Optional[Union[Text, List[Text]]] = None
    repetitions: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    repetitions: Optional[Union[Number, List[Number]]] = None
    activityDuration: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    activityDuration: Optional[Union[Duration, List[Duration]]] = None
    activityFrequency: Optional[Union[Text, List[Text]]] = None
    activityFrequency: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = (
        None
    )
    workload: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    workload: Optional[Union[Energy, List[Energy]]] = None
    intensity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    intensity: Optional[Union[Text, List[Text]]] = None
