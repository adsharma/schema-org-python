from typing import List, Optional, Union

from schema_models.bio_chem_entity import BioChemEntity


class Protein(BioChemEntity):
    hasBioPolymerSequence: Optional[Union[str, List[str]]] = None
