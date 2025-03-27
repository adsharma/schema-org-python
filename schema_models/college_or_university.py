from dataclasses import dataclass

from schema_models.educational_organization import EducationalOrganization


@dataclass
class CollegeOrUniversity(EducationalOrganization):
    """
    A college, university, or other third-level educational institution.
    """
