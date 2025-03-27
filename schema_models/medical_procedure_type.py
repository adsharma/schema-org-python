from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class MedicalProcedureType(MedicalEnumeration):
    """
    An enumeration that describes different types of medical procedures.
    """
