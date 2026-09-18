from dataclasses import dataclass
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.category_code import CategoryCode
from schema_models.lifestyle_modification import LifestyleModification
from schema_models.physical_activity_category import PhysicalActivityCategory
from schema_models.superficial_anatomy import SuperficialAnatomy
from schema_models.thing import Thing


@dataclass
class PhysicalActivity(LifestyleModification):
    """
    Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan.
    """

    associatedAnatomy: Optional[
        Union[
            AnatomicalStructure,
            List[AnatomicalStructure],
            AnatomicalSystem,
            List[AnatomicalSystem],
            SuperficialAnatomy,
            List[SuperficialAnatomy],
        ]
    ] = None
    category: Optional[
        Union[
            CategoryCode,
            List[CategoryCode],
            PhysicalActivityCategory,
            List[PhysicalActivityCategory],
            str,
            List[str],
            Thing,
            List[Thing],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    epidemiology: Optional[Union[str, List[str]]] = None
    pathophysiology: Optional[Union[str, List[str]]] = None
