from dataclasses import dataclass

from schema_models.quantity import Quantity


@dataclass
class Mass(Quantity):
    """
    Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g., '7 kg'.
    """
