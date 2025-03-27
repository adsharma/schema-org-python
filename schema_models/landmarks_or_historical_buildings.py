from dataclasses import dataclass

from schema_models.place import Place


@dataclass
class LandmarksOrHistoricalBuildings(Place):
    """
    An historical landmark or building.
    """
