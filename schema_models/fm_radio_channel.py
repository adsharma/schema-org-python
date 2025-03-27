from dataclasses import dataclass

from schema_models.radio_channel import RadioChannel


@dataclass
class FMRadioChannel(RadioChannel):
    """
    A radio channel that uses FM.
    """
