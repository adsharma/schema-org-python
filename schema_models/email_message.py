from dataclasses import dataclass

from schema_models.message import Message


@dataclass
class EmailMessage(Message):
    """
    An email message.
    """
