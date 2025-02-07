from typing import List, Optional, Union

from schema_models.monetary_amount import MonetaryAmount
from schema_models.number import Number
from schema_models.organization_role import OrganizationRole
from schema_models.price_specification import PriceSpecification
from schema_models.text import Text


class EmployeeRole(OrganizationRole):
    baseSalary: Optional[Union[PriceSpecification, List[PriceSpecification]]] = None
    baseSalary: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = None
    baseSalary: Optional[Union[Number, List[Number]]] = None
    salaryCurrency: Optional[Union[Text, List[Text]]] = None
