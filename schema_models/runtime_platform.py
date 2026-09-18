from dataclasses import dataclass

from schema_models.software_application import SoftwareApplication


@dataclass
class RuntimePlatform(SoftwareApplication):
    """
    Runtime platform or script interpreter dependencies (example: Java v1, Python 2.3, .NET Framework 3.0).
    """
