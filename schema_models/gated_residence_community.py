from dataclasses import dataclass

from schema_models.residence import Residence


@dataclass
class GatedResidenceCommunity(Residence):
    """
    Residence type: Gated community.
    """
