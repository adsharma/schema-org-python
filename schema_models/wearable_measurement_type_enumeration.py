from dataclasses import dataclass

from schema_models.measurement_type_enumeration import MeasurementTypeEnumeration


@dataclass
class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """
    Enumerates common types of measurement for wearables products.
    """
