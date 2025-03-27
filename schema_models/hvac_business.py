from dataclasses import dataclass

from schema_models.home_and_construction_business import HomeAndConstructionBusiness


@dataclass
class HVACBusiness(HomeAndConstructionBusiness):
    """
    A business that provides Heating, Ventilation and Air Conditioning services.
    """
