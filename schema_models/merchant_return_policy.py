from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible
from schema_models.member_program_tier import MemberProgramTier


@dataclass
class MerchantReturnPolicy(Intangible):
    """
    A MerchantReturnPolicy provides information about product return policies associated with an [[Organization]], [[Product]], or [[Offer]].
    """

    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    applicableCountry: Optional[Union["Country", List["Country"], str, List[str]]] = (
        None
    )
    customerRemorseReturnFees: Optional[
        Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]
    ] = None
    customerRemorseReturnLabelSource: Optional[
        Union["ReturnLabelSourceEnumeration", List["ReturnLabelSourceEnumeration"]]
    ] = None
    customerRemorseReturnShippingFeesAmount: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"]]
    ] = None
    inStoreReturnsOffered: Optional[Union[bool, List[bool]]] = None
    itemCondition: Optional[Union["OfferItemCondition", List["OfferItemCondition"]]] = (
        None
    )
    itemDefectReturnFees: Optional[
        Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]
    ] = None
    itemDefectReturnLabelSource: Optional[
        Union["ReturnLabelSourceEnumeration", List["ReturnLabelSourceEnumeration"]]
    ] = None
    itemDefectReturnShippingFeesAmount: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"]]
    ] = None
    merchantReturnDays: Optional[
        Union[date, List[date], datetime, List[datetime], int, List[int]]
    ] = None
    merchantReturnLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    refundType: Optional[
        Union["RefundTypeEnumeration", List["RefundTypeEnumeration"]]
    ] = None
    restockingFee: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"], float, List[float]]
    ] = None
    returnFees: Optional[
        Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]
    ] = None
    returnLabelSource: Optional[
        Union["ReturnLabelSourceEnumeration", List["ReturnLabelSourceEnumeration"]]
    ] = None
    returnMethod: Optional[
        Union["ReturnMethodEnumeration", List["ReturnMethodEnumeration"]]
    ] = None
    returnPolicyCategory: Optional[
        Union["MerchantReturnEnumeration", List["MerchantReturnEnumeration"]]
    ] = None
    returnPolicyCountry: Optional[Union["Country", List["Country"], str, List[str]]] = (
        None
    )
    returnPolicySeasonalOverride: Optional[
        Union[
            "MerchantReturnPolicySeasonalOverride",
            List["MerchantReturnPolicySeasonalOverride"],
        ]
    ] = None
    returnShippingFeesAmount: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"]]
    ] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
