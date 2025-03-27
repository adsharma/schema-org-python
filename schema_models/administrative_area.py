from dataclasses import dataclass

from schema_models.place import Place


@dataclass
class AdministrativeArea(Place):
    """
    A geographical region, typically under the jurisdiction of a particular government.
    """
