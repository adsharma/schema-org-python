from dataclasses import dataclass

from schema_models.comment import Comment


@dataclass
class CorrectionComment(Comment):
    """
    A [[comment]] that corrects [[CreativeWork]].
    """
