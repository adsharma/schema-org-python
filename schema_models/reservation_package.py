from typing import List, Optional, Union

from schema_models.reservation import Reservation


class ReservationPackage(Reservation):
    """
    A group of multiple reservations with common values for all sub-reservations.
    """

    subReservation: Optional[Union[Reservation, List[Reservation]]] = None
