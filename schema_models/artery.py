from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.vessel import Vessel


class Artery(Vessel):
    arterialBranch: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = (
        None
    )
    supplyTo: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = None
