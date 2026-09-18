from dataclasses import dataclass

from schema_models.audience import Audience


@dataclass
class MedicalAudience(Audience):
    """
    Medical audience for page.
    """
