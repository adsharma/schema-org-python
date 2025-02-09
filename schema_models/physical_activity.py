from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.lifestyle_modification import LifestyleModification
from schema_models.superficial_anatomy import SuperficialAnatomy
from schema_models.thing import Thing


class PhysicalActivity(LifestyleModification):
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union["PhysicalActivityCategory", List["PhysicalActivityCategory"]]
    ] = None
    category: Optional[Union["CategoryCode", List["CategoryCode"]]] = None
    category: Optional[Union[str, List[str]]] = None
    category: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    epidemiology: Optional[Union[str, List[str]]] = None
    associatedAnatomy: Optional[
        Union[AnatomicalStructure, List[AnatomicalStructure]]
    ] = None
    associatedAnatomy: Optional[Union[AnatomicalSystem, List[AnatomicalSystem]]] = None
    associatedAnatomy: Optional[Union[SuperficialAnatomy, List[SuperficialAnatomy]]] = (
        None
    )
    pathophysiology: Optional[Union[str, List[str]]] = None
