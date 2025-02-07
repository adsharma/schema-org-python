from typing import List, Optional, Union

from schema_models.bio_chem_entity import BioChemEntity
from schema_models.text import Text


class Protein(BioChemEntity):
    hasBioPolymerSequence: Optional[Union[Text, List[Text]]] = None
