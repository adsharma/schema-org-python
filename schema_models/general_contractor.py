from dataclasses import dataclass

from schema_models.home_and_construction_business import HomeAndConstructionBusiness


@dataclass
class GeneralContractor(HomeAndConstructionBusiness):
    """
    A general contractor.
    """
