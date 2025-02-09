from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.member_program_tier import MemberProgramTier
from schema_models.merchant_return_policy_seasonal_override import (
    MerchantReturnPolicySeasonalOverride,
)


class MerchantReturnPolicy(Intangible):
    restockingFee: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    restockingFee: Optional[Union[float, List[float]]] = None
    returnShippingFeesAmount: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"]]
    ] = None
    returnPolicySeasonalOverride: Optional[
        Union[
            MerchantReturnPolicySeasonalOverride,
            List[MerchantReturnPolicySeasonalOverride],
        ]
    ] = None
    returnMethod: Optional[
        Union["ReturnMethodEnumeration", List["ReturnMethodEnumeration"]]
    ] = None
    merchantReturnLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    returnPolicyCountry: Optional[Union["Country", List["Country"]]] = None
    returnPolicyCountry: Optional[Union[str, List[str]]] = None
    itemDefectReturnFees: Optional[
        Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]
    ] = None
    customerRemorseReturnLabelSource: Optional[
        Union["ReturnLabelSourceEnumeration", List["ReturnLabelSourceEnumeration"]]
    ] = None
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
    returnLabelSource: Optional[
        Union["ReturnLabelSourceEnumeration", List["ReturnLabelSourceEnumeration"]]
    ] = None
    itemCondition: Optional[Union["OfferItemCondition", List["OfferItemCondition"]]] = (
        None
    )
    returnPolicyCategory: Optional[
        Union["MerchantReturnEnumeration", List["MerchantReturnEnumeration"]]
    ] = None
    itemDefectReturnShippingFeesAmount: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"]]
    ] = None
    customerRemorseReturnFees: Optional[
        Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]
    ] = None
    refundType: Optional[
        Union["RefundTypeEnumeration", List["RefundTypeEnumeration"]]
    ] = None
    applicableCountry: Optional[Union[str, List[str]]] = None
    applicableCountry: Optional[Union["Country", List["Country"]]] = None
    returnFees: Optional[
        Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]
    ] = None
    merchantReturnDays: Optional[Union[date, List[date]]] = None
    merchantReturnDays: Optional[Union[int, List[int]]] = None
    merchantReturnDays: Optional[Union[datetime, List[datetime]]] = None
    inStoreReturnsOffered: Optional[Union[bool, List[bool]]] = None
    itemDefectReturnLabelSource: Optional[
        Union["ReturnLabelSourceEnumeration", List["ReturnLabelSourceEnumeration"]]
    ] = None
    customerRemorseReturnShippingFeesAmount: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"]]
    ] = None
