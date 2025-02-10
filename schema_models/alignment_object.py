from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class AlignmentObject(Intangible):
    """
    An intangible item that describes an alignment between a learning resource and a node in an educational framework.

    Should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.
    """

    alignmentType: Optional[Union[str, List[str]]] = None
    targetUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    targetDescription: Optional[Union[str, List[str]]] = None
    educationalFramework: Optional[Union[str, List[str]]] = None
    targetName: Optional[Union[str, List[str]]] = None
