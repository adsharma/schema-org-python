from typing import List, Optional, Union

from schema_models.intangible import Intangible


class BedDetails(Intangible):
    """
    An entity holding detailed information about the available bed types, e.g. the quantity of twin beds for a hotel room. For the single case of just one bed of a certain type, you can use bed directly with a text. See also [[BedType]] (under development).
    """

    numberOfBeds: Optional[Union[float, List[float]]] = None
    typeOfBed: Optional[Union["BedType", List["BedType"], str, List[str]]] = None
