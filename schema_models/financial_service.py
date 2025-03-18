from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.local_business import LocalBusiness


class FinancialService(LocalBusiness):
    """
    Financial services business.
    """

    feesAndCommissionsSpecification: Optional[
        Union[str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
