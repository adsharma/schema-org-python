from dataclasses import dataclass

from schema_models.lodging_business import LodgingBusiness


@dataclass
class Hostel(LodgingBusiness):
    """
    A hostel - cheap accommodation, often in shared dormitories.
    <br /><br />
    See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    """
