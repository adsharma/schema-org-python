from typing import List, Optional, Union

from schema_models.audience import Audience
from schema_models.language import Language
from schema_models.place import Place


class TouristAttraction(Place):
    """
    A tourist attraction.  In principle any Thing can be a [[TouristAttraction]], from a [[Mountain]] and [[LandmarksOrHistoricalBuildings]] to a [[LocalBusiness]].  This Type can be used on its own to describe a general [[TouristAttraction]], or be used as an [[additionalType]] to add tourist attraction properties to any other type.  (See examples below)
    """

    touristType: Optional[Union[str, List[str]]] = None
    touristType: Optional[Union[Audience, List[Audience]]] = None
    availableLanguage: Optional[Union[str, List[str]]] = None
    availableLanguage: Optional[Union[Language, List[Language]]] = None
