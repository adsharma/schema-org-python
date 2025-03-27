from dataclasses import dataclass

from schema_models.enumeration import Enumeration


@dataclass
class MediaEnumeration(Enumeration):
    """
    MediaEnumeration enumerations are lists of codes, labels etc. useful for describing media objects. They may be reflections of externally developed lists, or created at schema.org, or a combination.
    """
