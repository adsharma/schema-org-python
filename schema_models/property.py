from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.enumeration import Enumeration
from schema_models.intangible import Intangible


@dataclass
class Property(Intangible):
    """
    A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.
    """

    domainIncludes: Optional[Union["_Class", List["_Class"]]] = None
    inverseOf: Optional[Union["Property", List["Property"]]] = None
    rangeIncludes: Optional[Union["_Class", List["_Class"]]] = None
    supersededBy: Optional[
        Union[
            "_Class",
            List["_Class"],
            Enumeration,
            List[Enumeration],
            "Property",
            List["Property"],
        ]
    ] = None
