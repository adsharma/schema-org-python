from typing import List, Optional, Union

from schema_models.creative_work import CreativeWork
from schema_models.digital_document_permission import DigitalDocumentPermission


class DigitalDocument(CreativeWork):
    hasDigitalDocumentPermission: Optional[
        Union[DigitalDocumentPermission, List[DigitalDocumentPermission]]
    ] = None
