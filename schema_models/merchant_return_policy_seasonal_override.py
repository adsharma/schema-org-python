from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.intangible import Intangible


class MerchantReturnPolicySeasonalOverride(Intangible):
    returnFees: Optional[
        Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]
    ] = None
    restockingFee: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    restockingFee: Optional[Union[float, List[float]]] = None
    returnShippingFeesAmount: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"]]
    ] = None
    returnMethod: Optional[
        Union["ReturnMethodEnumeration", List["ReturnMethodEnumeration"]]
    ] = None
    startDate: Optional[Union[datetime, List[datetime]]] = None
    startDate: Optional[Union[date, List[date]]] = None
    returnPolicyCategory: Optional[
        Union["MerchantReturnEnumeration", List["MerchantReturnEnumeration"]]
    ] = None
    endDate: Optional[Union[date, List[date]]] = None
    endDate: Optional[Union[datetime, List[datetime]]] = None
    merchantReturnDays: Optional[Union[date, List[date]]] = None
    merchantReturnDays: Optional[Union[int, List[int]]] = None
    merchantReturnDays: Optional[Union[datetime, List[datetime]]] = None
    refundType: Optional[
        Union["RefundTypeEnumeration", List["RefundTypeEnumeration"]]
    ] = None
