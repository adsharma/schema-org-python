from typing import List, Optional, Union

from schema_models.monetary_amount import MonetaryAmount
from schema_models.organization_role import OrganizationRole
from schema_models.price_specification import PriceSpecification


class EmployeeRole(OrganizationRole):
    """
    A subclass of OrganizationRole used to describe employee relationships.
    """

    baseSalary: Optional[Union[PriceSpecification, List[PriceSpecification]]] = None
    baseSalary: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    baseSalary: Optional[Union[float, List[float]]] = None
    salaryCurrency: Optional[Union[str, List[str]]] = None
