from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import field_validator, ConfigDict, Field, HttpUrl
from schema_models.transfer_action import TransferAction


class TakeAction(TransferAction):
    pass
