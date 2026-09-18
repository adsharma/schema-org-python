from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.monetary_amount import MonetaryAmount
from schema_models.organization_role import OrganizationRole
from schema_models.price_specification import PriceSpecification


@dataclass
class EmployeeRole(OrganizationRole):
    """
    A subclass of OrganizationRole used to describe employee relationships.
    """

    baseSalary: Optional[
        Union[
            MonetaryAmount,
            List[MonetaryAmount],
            float,
            List[float],
            PriceSpecification,
            List[PriceSpecification],
        ]
    ] = None
    salaryCurrency: Optional[Union[str, List[str]]] = None
