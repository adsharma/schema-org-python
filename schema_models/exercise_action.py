from typing import List, Optional, Union

from schema_models.diet import Diet
from schema_models.distance import Distance
from schema_models.person import Person
from schema_models.place import Place
from schema_models.play_action import PlayAction
from schema_models.sports_event import SportsEvent
from schema_models.sports_team import SportsTeam


class ExerciseAction(PlayAction):
    """
    The act of participating in exertive activity for the purposes of improving health and fitness.
    """

    course: Optional[Union[Place, List[Place]]] = None
    exerciseRelatedDiet: Optional[Union[Diet, List[Diet]]] = None
    fromLocation: Optional[Union[Place, List[Place]]] = None
    toLocation: Optional[Union[Place, List[Place]]] = None
    sportsTeam: Optional[Union[SportsTeam, List[SportsTeam]]] = None
    exercisePlan: Optional[Union["ExercisePlan", List["ExercisePlan"]]] = None
    diet: Optional[Union[Diet, List[Diet]]] = None
    sportsActivityLocation: Optional[
        Union["SportsActivityLocation", List["SportsActivityLocation"]]
    ] = None
    exerciseCourse: Optional[Union[Place, List[Place]]] = None
    distance: Optional[Union[Distance, List[Distance]]] = None
    opponent: Optional[Union[Person, List[Person]]] = None
    exerciseType: Optional[Union[str, List[str]]] = None
    sportsEvent: Optional[Union[SportsEvent, List[SportsEvent]]] = None
