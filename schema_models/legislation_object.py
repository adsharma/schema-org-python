from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.legal_value_level import LegalValueLevel
from schema_models.legislation import Legislation


class LegislationObject(Legislation):
    legislationLegalValue: Optional[Union[LegalValueLevel, List[LegalValueLevel]]] = (
        None
    )
