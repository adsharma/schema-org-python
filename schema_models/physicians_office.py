from dataclasses import dataclass

from schema_models.physician import Physician


@dataclass
class PhysiciansOffice(Physician):
    """
    A doctor's office or clinic.
    """
