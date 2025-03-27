from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class RsvpResponseType(Enumeration):
    """
    RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.
    """
