from dataclasses import dataclass

from schema_models.project import Project


@dataclass
class ResearchProject(Project):
    """
    A Research project.
    """
