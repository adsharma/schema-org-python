from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.local_business import LocalBusiness


class FinancialService(LocalBusiness):
    feesAndCommissionsSpecification: Optional[Union[str, List[str]]] = None
    feesAndCommissionsSpecification: Optional[Union[HttpUrl, List[HttpUrl]]] = None
