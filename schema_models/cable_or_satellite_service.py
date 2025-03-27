from dataclasses import dataclass

from schema_models.service import Service


@dataclass
class CableOrSatelliteService(Service):
    """
    A service which provides access to media programming like TV or radio. Access may be via cable or satellite.
    """
