from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.allocate_action import AllocateAction


class RejectAction(AllocateAction):
    pass
