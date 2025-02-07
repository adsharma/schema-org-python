from typing import List, Optional, Union

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.category_code import CategoryCode
from schema_models.lifestyle_modification import LifestyleModification
from schema_models.physical_activity_category import PhysicalActivityCategory
from schema_models.superficial_anatomy import SuperficialAnatomy
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class PhysicalActivity(LifestyleModification):
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union[PhysicalActivityCategory, List[PhysicalActivityCategory]]
    ] = None
    category: Optional[Union[CategoryCode, List[CategoryCode]]] = None
    category: Optional[Union[Text, List[Text]]] = None
    category: Optional[Union[URL, List[URL]]] = None
    epidemiology: Optional[Union[Text, List[Text]]] = None
    associatedAnatomy: Optional[
        Union[AnatomicalStructure, List[AnatomicalStructure]]
    ] = None
    associatedAnatomy: Optional[Union[AnatomicalSystem, List[AnatomicalSystem]]] = None
    associatedAnatomy: Optional[Union[SuperficialAnatomy, List[SuperficialAnatomy]]] = (
        None
    )
    pathophysiology: Optional[Union[Text, List[Text]]] = None
