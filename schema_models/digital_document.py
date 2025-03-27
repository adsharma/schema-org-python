from dataclasses import dataclass
from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.digital_document_permission import DigitalDocumentPermission


@dataclass
class DigitalDocument(CreativeWork):
    """
    An electronic file or document.
    """

    hasDigitalDocumentPermission: Optional[
        Union[DigitalDocumentPermission, List[DigitalDocumentPermission]]
    ] = None
