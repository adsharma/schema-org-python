from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.boolean import Boolean
from schema_models.medical_specialty import MedicalSpecialty
from schema_models.organization import Organization
from schema_models.text import Text


class MedicalOrganization(Organization):
    medicalSpecialty: Optional[Union[MedicalSpecialty, List[MedicalSpecialty]]] = None
    isAcceptingNewPatients: Optional[Union[Boolean, List[Boolean]]] = None
    healthPlanNetworkId: Optional[Union[Text, List[Text]]] = None
