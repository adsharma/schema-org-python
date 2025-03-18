from typing import List, Optional, Union

from schema_models.price_specification import PriceSpecification
from schema_models.price_type_enumeration import PriceTypeEnumeration


class CompoundPriceSpecification(PriceSpecification):
    """
    A compound price specification is one that bundles multiple prices that all apply in combination for different dimensions of consumption. Use the name property of the attached unit price specification for indicating the dimension of a price component (e.g. "electricity" or "final cleaning").
    """

    priceComponent: Optional[
        Union["UnitPriceSpecification", List["UnitPriceSpecification"]]
    ] = None
    priceType: Optional[
        Union[PriceTypeEnumeration, List[PriceTypeEnumeration], str, List[str]]
    ] = None
