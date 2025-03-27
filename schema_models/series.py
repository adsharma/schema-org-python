from dataclasses import dataclass

from schema_models.intangible import Intangible


@dataclass
class Series(Intangible):
    """
    A Series in schema.org is a group of related items, typically but not necessarily of the same kind. See also [[CreativeWorkSeries]], [[EventSeries]].
    """
