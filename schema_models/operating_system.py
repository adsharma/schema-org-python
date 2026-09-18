from dataclasses import dataclass

from schema_models.software_application import SoftwareApplication


@dataclass
class OperatingSystem(SoftwareApplication):
    """
    Operating systems supported (Windows 7, OS X 10.6, Android 1.6).
    """
