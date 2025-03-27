from dataclasses import dataclass

from schema_models.administrative_area import AdministrativeArea


@dataclass
class SchoolDistrict(AdministrativeArea):
    """
    A School District is an administrative area for the administration of schools.
    """
