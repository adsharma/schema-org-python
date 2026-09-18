from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class HowToStep(CreativeWork):
    """
    A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection and/or HowToTip items.
    """
