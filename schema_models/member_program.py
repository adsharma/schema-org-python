from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.intangible import Intangible
from schema_models.member_program_tier import MemberProgramTier
from schema_models.organization import Organization


class MemberProgram(Intangible):
    hostingOrganization: Optional[Union[Organization, List[Organization]]] = None
    hasTiers: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = None
