from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_intangible import MedicalIntangible
from schema_models.number import Number
from schema_models.text import Text


class MedicalConditionStage(MedicalIntangible):
    stageAsNumber: Optional[Union[Number, List[Number]]] = None
    subStageSuffix: Optional[Union[Text, List[Text]]] = None
