from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class BusinessFunction(Enumeration):
    """
    The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.
    """
