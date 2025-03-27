from dataclasses import dataclass

from schema_models.learning_resource import LearningResource


@dataclass
class Quiz(LearningResource):
    """
    Quiz: A test of knowledge, skills and abilities.
    """
