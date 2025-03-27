from dataclasses import dataclass

from schema_models.creative_work import CreativeWork


@dataclass
class Conversation(CreativeWork):
    """
    One or more messages between organizations or people on a particular topic. Individual messages can be linked to the conversation with isPartOf or hasPart properties.
    """
