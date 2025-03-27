from dataclasses import dataclass

from schema_models.organization import Organization


@dataclass
class Project(Organization):
    """
    An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.
    Use properties from [[Organization]], [[subOrganization]]/[[parentOrganization]] to indicate project sub-structures.

    """
