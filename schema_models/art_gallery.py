from dataclasses import dataclass

from schema_models.entertainment_business import EntertainmentBusiness


@dataclass
class ArtGallery(EntertainmentBusiness):
    """
    An art gallery.
    """
