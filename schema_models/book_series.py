from dataclasses import dataclass

from schema_models.creative_work_series import CreativeWorkSeries


@dataclass
class BookSeries(CreativeWorkSeries):
    """
    A series of books. Included books can be indicated with the hasPart property.
    """
