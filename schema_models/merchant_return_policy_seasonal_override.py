from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.intangible import Intangible


@dataclass
class MerchantReturnPolicySeasonalOverride(Intangible):
    """
    A seasonal override of a return policy, for example used for holidays.
    """

    endDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    merchantReturnDays: Optional[
        Union[date, List[date], datetime, List[datetime], int, List[int]]
    ] = None
    refundType: Optional[
        Union["RefundTypeEnumeration", List["RefundTypeEnumeration"]]
    ] = None
    restockingFee: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"], float, List[float]]
    ] = None
    returnFees: Optional[
        Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]
    ] = None
    returnMethod: Optional[
        Union["ReturnMethodEnumeration", List["ReturnMethodEnumeration"]]
    ] = None
    returnPolicyCategory: Optional[
        Union["MerchantReturnEnumeration", List["MerchantReturnEnumeration"]]
    ] = None
    returnShippingFeesAmount: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"]]
    ] = None
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
