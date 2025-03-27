from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class Poster(CreativeWork):
    """
    A large, usually printed placard, bill, or announcement, often illustrated, that is posted to advertise or publicize something.
    """
