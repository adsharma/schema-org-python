from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.intangible import Intangible


class ConstraintNode(Intangible):
    """
    The ConstraintNode type is provided to support usecases in which a node in a structured data graph is described with properties which appear to describe a single entity, but are being used in a situation where they serve a more abstract purpose. A [[ConstraintNode]] can be described using [[constraintProperty]] and [[numConstraints]]. These constraint properties can serve a
        variety of purposes, and their values may sometimes be understood to indicate sets of possible values rather than single, exact and specific values.
    """

    numConstraints: Optional[Union[int, List[int]]] = None
    constraintProperty: Optional[
        Union["Property", List["Property"], HttpUrl, List[HttpUrl]]
    ] = None
