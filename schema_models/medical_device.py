from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_contraindication import MedicalContraindication
from schema_models.medical_entity import MedicalEntity
from schema_models.text import Text


class MedicalDevice(MedicalEntity):
    procedure: Optional[Union[Text, List[Text]]] = None
    adverseOutcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    postOp: Optional[Union[Text, List[Text]]] = None
    seriousAdverseOutcome: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
    contraindication: Optional[Union[Text, List[Text]]] = None
    contraindication: Optional[
        Union[MedicalContraindication, List[MedicalContraindication]]
    ] = None
    preOp: Optional[Union[Text, List[Text]]] = None
