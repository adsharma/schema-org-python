from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.infectious_agent_class import InfectiousAgentClass
from schema_models.medical_condition import MedicalCondition
from schema_models.text import Text


class InfectiousDisease(MedicalCondition):
    infectiousAgentClass: Optional[
        Union[InfectiousAgentClass, List[InfectiousAgentClass]]
    ] = None
    infectiousAgent: Optional[Union[Text, List[Text]]] = None
    transmissionMethod: Optional[Union[Text, List[Text]]] = None
