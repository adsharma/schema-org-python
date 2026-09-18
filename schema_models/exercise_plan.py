from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.duration import Duration
from schema_models.energy import Energy


@dataclass
class ExercisePlan(CreativeWork):
    """
    A sub property of instrument. The exercise plan used on this action.
    """

    activityDuration: Optional[
        Union[Duration, List[Duration], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    activityFrequency: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], str, List[str]]
    ] = None
    additionalVariable: Optional[Union[str, List[str]]] = None
    exerciseType: Optional[Union[str, List[str]]] = None
    intensity: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], str, List[str]]
    ] = None
    repetitions: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    restPeriods: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"], str, List[str]]
    ] = None
    workload: Optional[
        Union[Energy, List[Energy], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
