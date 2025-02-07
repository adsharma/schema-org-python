from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.creative_work import CreativeWork
from schema_models.digital_document_permission import DigitalDocumentPermission


class DigitalDocument(CreativeWork):
    hasDigitalDocumentPermission: Optional[
        Union[DigitalDocumentPermission, List[DigitalDocumentPermission]]
    ] = None
