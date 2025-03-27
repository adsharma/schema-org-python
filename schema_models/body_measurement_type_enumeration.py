from dataclasses import dataclass

from schema_models.measurement_type_enumeration import MeasurementTypeEnumeration


@dataclass
class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """
    Enumerates types (or dimensions) of a person's body measurements, for example for fitting of clothes.
    """
