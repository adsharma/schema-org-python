from dataclasses import dataclass

from schema_models.educational_organization import EducationalOrganization


@dataclass
class MiddleSchool(EducationalOrganization):
    """
    A middle school (typically for children aged around 11-14, although this varies somewhat).
    """
