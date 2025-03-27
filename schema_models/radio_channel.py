from dataclasses import dataclass

from schema_models.broadcast_channel import BroadcastChannel


@dataclass
class RadioChannel(BroadcastChannel):
    """
    A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.
    """
