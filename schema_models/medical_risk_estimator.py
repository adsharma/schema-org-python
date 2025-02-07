from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.medical_entity import MedicalEntity
from schema_models.medical_risk_factor import MedicalRiskFactor


class MedicalRiskEstimator(MedicalEntity):
    includedRiskFactor: Optional[Union[MedicalRiskFactor, List[MedicalRiskFactor]]] = (
        None
    )
    estimatesRiskOf: Optional[Union[MedicalEntity, List[MedicalEntity]]] = None
