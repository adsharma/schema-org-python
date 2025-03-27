from dataclasses import dataclass

from schema_models.create_action import CreateAction


@dataclass
class PhotographAction(CreateAction):
    """
    The act of capturing still images of objects using a camera.
    """
