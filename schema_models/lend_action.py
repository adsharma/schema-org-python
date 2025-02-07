from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.person import Person
from schema_models.transfer_action import TransferAction


class LendAction(TransferAction):
    borrower: Optional[Union[Person, List[Person]]] = None
