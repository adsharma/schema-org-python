from dataclasses import dataclass

from schema_models.status_enumeration import StatusEnumeration


@dataclass
class ReservationStatusType(StatusEnumeration):
    """
    Enumerated status values for Reservation.
    """
