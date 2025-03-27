from dataclasses import dataclass

from schema_models.item_list import ItemList


@dataclass
class OfferCatalog(ItemList):
    """
    An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.
    """
