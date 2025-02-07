from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.defined_term import DefinedTerm


class DefinedTermSet(CreativeWork):
    hasDefinedTerm: Optional[Union[DefinedTerm, List[DefinedTerm]]] = None
