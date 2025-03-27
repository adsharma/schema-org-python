from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class MeasurementTypeEnumeration(Enumeration):
    """
    Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles.
    """
