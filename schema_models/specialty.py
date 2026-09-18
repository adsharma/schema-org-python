from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class Specialty(Enumeration):
    """
    One of the domain specialities to which this web page's content applies.
    """
