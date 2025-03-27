from dataclasses import dataclass

from schema_models.broadcast_channel import BroadcastChannel


@dataclass
class TelevisionChannel(BroadcastChannel):
    """
    A unique instance of a television BroadcastService on a CableOrSatelliteService lineup.
    """
