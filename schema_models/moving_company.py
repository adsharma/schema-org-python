from dataclasses import dataclass

from schema_models.home_and_construction_business import HomeAndConstructionBusiness


@dataclass
class MovingCompany(HomeAndConstructionBusiness):
    """
    A moving company.
    """
