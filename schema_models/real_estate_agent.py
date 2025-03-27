from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class RealEstateAgent(LocalBusiness):
    """
    A sub property of participant. The real estate agent involved in the action.
    """
