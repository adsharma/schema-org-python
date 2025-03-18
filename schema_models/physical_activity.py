from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.anatomical_structure import AnatomicalStructure
from schema_models.anatomical_system import AnatomicalSystem
from schema_models.lifestyle_modification import LifestyleModification
from schema_models.superficial_anatomy import SuperficialAnatomy
from schema_models.thing import Thing


class PhysicalActivity(LifestyleModification):
    """
    Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan.
    """

    category: Optional[
        Union[
            Thing,
            List[Thing],
            "PhysicalActivityCategory",
            List["PhysicalActivityCategory"],
            "CategoryCode",
            List["CategoryCode"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    epidemiology: Optional[Union[str, List[str]]] = None
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
    pathophysiology: Optional[Union[str, List[str]]] = None
