from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.country import Country
from schema_models.date import Date
from schema_models.date_time import DateTime
from schema_models.intangible import Intangible
from schema_models.integer import Integer
from schema_models.member_program_tier import MemberProgramTier
from schema_models.merchant_return_enumeration import MerchantReturnEnumeration
from schema_models.merchant_return_policy_seasonal_override import (
    MerchantReturnPolicySeasonalOverride,
)
from schema_models.monetary_amount import MonetaryAmount
from schema_models.number import Number
from schema_models.offer_item_condition import OfferItemCondition
from schema_models.property_value import PropertyValue
from schema_models.refund_type_enumeration import RefundTypeEnumeration
from schema_models.return_fees_enumeration import ReturnFeesEnumeration
from schema_models.return_label_source_enumeration import ReturnLabelSourceEnumeration
from schema_models.return_method_enumeration import ReturnMethodEnumeration
from schema_models.text import Text
from schema_models.url import URL


class MerchantReturnPolicy(Intangible):
    restockingFee: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    restockingFee: Optional[Union[Number, List[Number]]] = None
    returnShippingFeesAmount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = (
        None
    )
    returnPolicySeasonalOverride: Optional[
        Union[
            MerchantReturnPolicySeasonalOverride,
            List[MerchantReturnPolicySeasonalOverride],
        ]
    ] = None
    returnMethod: Optional[
        Union[ReturnMethodEnumeration, List[ReturnMethodEnumeration]]
    ] = None
    merchantReturnLink: Optional[Union[URL, List[URL]]] = None
    returnPolicyCountry: Optional[Union[Country, List[Country]]] = None
    returnPolicyCountry: Optional[Union[Text, List[Text]]] = None
    itemDefectReturnFees: Optional[
        Union[ReturnFeesEnumeration, List[ReturnFeesEnumeration]]
    ] = None
    customerRemorseReturnLabelSource: Optional[
        Union[ReturnLabelSourceEnumeration, List[ReturnLabelSourceEnumeration]]
    ] = None
    additionalProperty: Optional[Union[PropertyValue, List[PropertyValue]]] = None
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = (
        None
    )
    returnLabelSource: Optional[
        Union[ReturnLabelSourceEnumeration, List[ReturnLabelSourceEnumeration]]
    ] = None
    itemCondition: Optional[Union[OfferItemCondition, List[OfferItemCondition]]] = None
    returnPolicyCategory: Optional[
        Union[MerchantReturnEnumeration, List[MerchantReturnEnumeration]]
    ] = None
    itemDefectReturnShippingFeesAmount: Optional[
        Union[MonetaryAmount, List[MonetaryAmount]]
    ] = None
    customerRemorseReturnFees: Optional[
        Union[ReturnFeesEnumeration, List[ReturnFeesEnumeration]]
    ] = None
    refundType: Optional[Union[RefundTypeEnumeration, List[RefundTypeEnumeration]]] = (
        None
    )
    applicableCountry: Optional[Union[Text, List[Text]]] = None
    applicableCountry: Optional[Union[Country, List[Country]]] = None
    returnFees: Optional[Union[ReturnFeesEnumeration, List[ReturnFeesEnumeration]]] = (
        None
    )
    merchantReturnDays: Optional[Union[Date, List[Date]]] = None
    merchantReturnDays: Optional[Union[Integer, List[Integer]]] = None
    merchantReturnDays: Optional[Union[DateTime, List[DateTime]]] = None
    inStoreReturnsOffered: Optional[Union[Boolean, List[Boolean]]] = None
    itemDefectReturnLabelSource: Optional[
        Union[ReturnLabelSourceEnumeration, List[ReturnLabelSourceEnumeration]]
    ] = None
    customerRemorseReturnShippingFeesAmount: Optional[
        Union[MonetaryAmount, List[MonetaryAmount]]
    ] = None
