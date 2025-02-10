from schema_models.item_list import ItemList


class OfferCatalog(ItemList):
    """
    An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.
    """
