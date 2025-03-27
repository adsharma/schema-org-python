from dataclasses import dataclass

from schema_models.broadcast_service import BroadcastService


@dataclass
class RadioBroadcastService(BroadcastService):
    """
    A delivery service through which radio content is provided via broadcast over the air or online.
    """
