from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class Play(CreativeWork):
    """
    A play is a form of literature, usually consisting of dialogue between characters, intended for theatrical performance rather than just reading. Note: A performance of a Play would be a [[TheaterEvent]] or [[BroadcastEvent]] - the *Play* being the [[workPerformed]].
    """
