from dataclasses import dataclass

from schema_models.certification import Certification


@dataclass
class EnvironmentalProductDeclaration(Certification):
    """
    An Environmental Product Declaration (EPD) that quantifies environmental information on the life cycle of a product.
    """
