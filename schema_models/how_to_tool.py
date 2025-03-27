from dataclasses import dataclass

from schema_models.how_to_item import HowToItem


@dataclass
class HowToTool(HowToItem):
    """
    A tool used (but not consumed) when performing instructions for how to achieve a result.
    """
