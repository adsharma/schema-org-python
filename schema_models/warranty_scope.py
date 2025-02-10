from schema_models.enumeration import Enumeration


class WarrantyScope(Enumeration):
    """
    A range of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.

    Commonly used values:

    * http://purl.org/goodrelations/v1#Labor-BringIn
    * http://purl.org/goodrelations/v1#PartsAndLabor-BringIn
    * http://purl.org/goodrelations/v1#PartsAndLabor-PickUp

    """
