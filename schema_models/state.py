from dataclasses import dataclass

from schema_models.administrative_area import AdministrativeArea


@dataclass
class State(AdministrativeArea):
    """
    A state or province of a country.
    """
