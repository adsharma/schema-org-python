from dataclasses import dataclass

from schema_models.administrative_area import AdministrativeArea


@dataclass
class Country(AdministrativeArea):
    """
    A country.
    """
