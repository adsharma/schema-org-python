from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.maximum_dose_schedule import MaximumDoseSchedule
from schema_models.medical_entity import MedicalEntity
from schema_models.text import Text


class Substance(MedicalEntity):
    activeIngredient: Optional[Union[Text, List[Text]]] = None
    maximumIntake: Optional[Union[MaximumDoseSchedule, List[MaximumDoseSchedule]]] = (
        None
    )
