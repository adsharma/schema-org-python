from dataclasses import dataclass

from schema_models.transfer_action import TransferAction


@dataclass
class DownloadAction(TransferAction):
    """
    The act of downloading an object.
    """
