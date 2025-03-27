from dataclasses import dataclass

from schema_models.create_action import CreateAction


@dataclass
class PaintAction(CreateAction):
    """
    The act of producing a painting, typically with paint and canvas as instruments.
    """
