from dataclasses import dataclass

from schema_models.publication_event import PublicationEvent


@dataclass
class OnDemandEvent(PublicationEvent):
    """
    A publication event, e.g. catch-up TV or radio podcast, during which a program is available on-demand.
    """
