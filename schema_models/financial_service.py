from typing import List, Optional, Union

from schema_models.local_business import LocalBusiness
from schema_models.text import Text
from schema_models.url import URL


class FinancialService(LocalBusiness):
    feesAndCommissionsSpecification: Optional[Union[Text, List[Text]]] = None
    feesAndCommissionsSpecification: Optional[Union[URL, List[URL]]] = None
