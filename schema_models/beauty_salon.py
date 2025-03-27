from dataclasses import dataclass

from schema_models.health_and_beauty_business import HealthAndBeautyBusiness


@dataclass
class BeautySalon(HealthAndBeautyBusiness):
    """
    Beauty salon.
    """
