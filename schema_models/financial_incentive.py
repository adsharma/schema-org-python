from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Union

from schema_models.defined_term import DefinedTerm
from schema_models.intangible import Intangible
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place
from schema_models.product import Product


@dataclass
class FinancialIncentive(Intangible):
    """
    <p>Represents financial incentives for goods/services offered by an organization (or individual).</p>

    <p>Typically contains the [[name]] of the incentive, the [[incentivizedItem]], the [[incentiveAmount]], the [[incentiveStatus]], [[incentiveType]], the [[provider]] of the incentive, and [[eligibleWithSupplier]].</p>

    <p>Optionally contains criteria on whether the incentive is limited based on [[purchaseType]], [[purchasePriceLimit]], [[incomeLimit]], and the [[qualifiedExpense]].

    """

    areaServed: Optional[
        Union[
            "AdministrativeArea",
            List["AdministrativeArea"],
            "GeoShape",
            List["GeoShape"],
            Place,
            List[Place],
            str,
            List[str],
        ]
    ] = None
    eligibleWithSupplier: Optional[Union[Organization, List[Organization]]] = None
    incentiveAmount: Optional[
        Union[
            "LoanOrCredit",
            List["LoanOrCredit"],
            "QuantitativeValue",
            List["QuantitativeValue"],
            "UnitPriceSpecification",
            List["UnitPriceSpecification"],
        ]
    ] = None
    incentiveStatus: Optional[Union["IncentiveStatus", List["IncentiveStatus"]]] = None
    incentiveType: Optional[Union["IncentiveType", List["IncentiveType"]]] = None
    incentivizedItem: Optional[
        Union[DefinedTerm, List[DefinedTerm], Product, List[Product]]
    ] = None
    incomeLimit: Optional[
        Union["MonetaryAmount", List["MonetaryAmount"], str, List[str]]
    ] = None
    provider: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    publisher: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    purchasePriceLimit: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = None
    purchaseType: Optional[Union["PurchaseType", List["PurchaseType"]]] = None
    qualifiedExpense: Optional[
        Union["IncentiveQualifiedExpenseType", List["IncentiveQualifiedExpenseType"]]
    ] = None
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = None
    validThrough: Optional[Union[date, List[date], datetime, List[datetime]]] = None
