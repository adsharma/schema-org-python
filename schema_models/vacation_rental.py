from dataclasses import dataclass

from schema_models.lodging_business import LodgingBusiness


@dataclass
class VacationRental(LodgingBusiness):
    """
    A kind of lodging business that focuses on renting single properties for limited time.
    """
