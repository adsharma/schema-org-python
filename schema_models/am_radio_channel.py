from dataclasses import dataclass

from schema_models.radio_channel import RadioChannel


@dataclass
class AMRadioChannel(RadioChannel):
    """
    A radio channel that uses AM.
    """
