from dataclasses import dataclass

from schema_models.certification import Certification


@dataclass
class DeclarationOfConformity(Certification):
    """
    A Declaration of Conformity (DoC), a formal document issued by a manufacturer declaring that a product meets specific regulatory requirements.
    """
