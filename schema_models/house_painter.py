from dataclasses import dataclass

from schema_models.home_and_construction_business import HomeAndConstructionBusiness


@dataclass
class HousePainter(HomeAndConstructionBusiness):
    """
    A house painting service.
    """
