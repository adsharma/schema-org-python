from dataclasses import dataclass

from schema_models.reservation import Reservation


@dataclass
class TrainReservation(Reservation):
    """
    A reservation for train travel.

    Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use [[Offer]].
    """
