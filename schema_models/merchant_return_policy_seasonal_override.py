from typing import List, Optional, Union

from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.intangible import Intangible
from schema_models.integer import Integer
from schema_models.merchant_return_enumeration import MerchantReturnEnumeration
from schema_models.monetary_amount import MonetaryAmount
from schema_models.number import Number
from schema_models.refund_type_enumeration import RefundTypeEnumeration
from schema_models.return_fees_enumeration import ReturnFeesEnumeration
from schema_models.return_method_enumeration import ReturnMethodEnumeration


class MerchantReturnPolicySeasonalOverride(Intangible):
    returnFees: Optional[Union[ReturnFeesEnumeration, List[ReturnFeesEnumeration]]] = (
        None
    )
    restockingFee: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    restockingFee: Optional[Union[Number, List[Number]]] = None
    returnShippingFeesAmount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = (
        None
    )
    returnMethod: Optional[
        Union[ReturnMethodEnumeration, List[ReturnMethodEnumeration]]
    ] = None
    startDate: Optional[Union[DateTime, List[DateTime]]] = None
    startDate: Optional[Union[Date, List[Date]]] = None
    returnPolicyCategory: Optional[
        Union[MerchantReturnEnumeration, List[MerchantReturnEnumeration]]
    ] = None
    endDate: Optional[Union[Date, List[Date]]] = None
    endDate: Optional[Union[DateTime, List[DateTime]]] = None
    merchantReturnDays: Optional[Union[Date, List[Date]]] = None
    merchantReturnDays: Optional[Union[Integer, List[Integer]]] = None
    merchantReturnDays: Optional[Union[DateTime, List[DateTime]]] = None
    refundType: Optional[Union[RefundTypeEnumeration, List[RefundTypeEnumeration]]] = (
        None
    )
