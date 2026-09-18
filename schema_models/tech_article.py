from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.article import Article


@dataclass
class TechArticle(Article):
    """
    A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.
    """

    dependencies: Optional[Union[str, List[str]]] = None
    proficiencyLevel: Optional[Union[str, List[str]]] = None
