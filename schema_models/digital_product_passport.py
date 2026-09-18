from dataclasses import dataclass

from schema_models.certification import Certification


@dataclass
class DigitalProductPassport(Certification):
    """
    A digital product passport (DPP), a record containing information about a product's lifecycle, sustainability, and compliance.
    """
