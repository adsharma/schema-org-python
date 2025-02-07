from typing import List, Optional, Union

from schema_models.reservation import Reservation


class ReservationPackage(Reservation):
    subReservation: Optional[Union[Reservation, List[Reservation]]] = None
