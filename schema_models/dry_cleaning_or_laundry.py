from dataclasses import dataclass

from schema_models.local_business import LocalBusiness


@dataclass
class DryCleaningOrLaundry(LocalBusiness):
    """
    A dry-cleaning business.
    """
