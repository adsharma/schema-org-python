from dataclasses import dataclass

from schema_models.government_office import GovernmentOffice


@dataclass
class PostOffice(GovernmentOffice):
    """
    A post office.
    """
