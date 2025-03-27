from dataclasses import dataclass

from schema_models.medical_enumeration import MedicalEnumeration


@dataclass
class MedicalDevicePurpose(MedicalEnumeration):
    """
    Categories of medical devices, organized by the purpose or intended use of the device.
    """
