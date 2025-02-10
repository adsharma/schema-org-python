from typing import List, Optional, Union

from schema_models.duration import Duration
from schema_models.energy import Energy
from schema_models.physical_activity import PhysicalActivity
from schema_models.quantitative_value import QuantitativeValue


class ExercisePlan(PhysicalActivity):
    """
    A sub property of instrument. The exercise plan used on this action.
    """

    additionalVariable: Optional[Union[str, List[str]]] = None
    exerciseType: Optional[Union[str, List[str]]] = None
    restPeriods: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    restPeriods: Optional[Union[str, List[str]]] = None
    repetitions: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    repetitions: Optional[Union[float, List[float]]] = None
    activityDuration: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    activityDuration: Optional[Union[Duration, List[Duration]]] = None
    activityFrequency: Optional[Union[str, List[str]]] = None
    activityFrequency: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = (
        None
    )
    workload: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    workload: Optional[Union[Energy, List[Energy]]] = None
    intensity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    intensity: Optional[Union[str, List[str]]] = None
