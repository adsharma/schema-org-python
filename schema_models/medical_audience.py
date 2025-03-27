from dataclasses import dataclass

from schema_models.people_audience import PeopleAudience


@dataclass
class MedicalAudience(PeopleAudience):
    """
    Medical audience for page.
    """
