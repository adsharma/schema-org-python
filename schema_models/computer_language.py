from dataclasses import dataclass

from schema_models.intangible import Intangible


@dataclass
class ComputerLanguage(Intangible):
    """
    This type covers computer programming languages such as Scheme and Lisp, as well as other language-like computer representations. Natural languages are best represented with the [[Language]] type.
    """
