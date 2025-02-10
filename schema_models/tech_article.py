from typing import List, Optional, Union

from schema_models.article import Article


class TechArticle(Article):
    """
    A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.
    """

    proficiencyLevel: Optional[Union[str, List[str]]] = None
    dependencies: Optional[Union[str, List[str]]] = None
