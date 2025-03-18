from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.intangible import Intangible


class MerchantReturnPolicySeasonalOverride(Intangible):
    """
    A seasonal override of a return policy, for example used for holidays.
    """

    returnFees: Optional[
        Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]
    ] = None
    restockingFee: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"], float, List[float]]
    ] = None
    returnShippingFeesAmount: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"]]
    ] = None
    returnMethod: Optional[
        Union["ReturnMethodEnumeration", List["ReturnMethodEnumeration"]]
    ] = None
    startDate: Optional[Union[datetime, List[datetime], date, List[date]]] = None
    returnPolicyCategory: Optional[
        Union["MerchantReturnEnumeration", List["MerchantReturnEnumeration"]]
    ] = None
    endDate: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    merchantReturnDays: Optional[
        Union[date, List[date], int, List[int], datetime, List[datetime]]
    ] = None
    refundType: Optional[
        Union["RefundTypeEnumeration", List["RefundTypeEnumeration"]]
    ] = None
