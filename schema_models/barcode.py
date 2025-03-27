from dataclasses import dataclass

from schema_models.image_object import ImageObject


@dataclass
class Barcode(ImageObject):
    """
    An image of a visual machine-readable code such as a barcode or QR code.
    """
