from dataclasses import dataclass

from schema_models.educational_organization import EducationalOrganization


@dataclass
class HighSchool(EducationalOrganization):
    """
    A high school.
    """
