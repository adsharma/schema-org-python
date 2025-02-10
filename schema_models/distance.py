from schema_models.quantity import Quantity


class Distance(Quantity):
    """
    Properties that take Distances as values are of the form '&lt;Number&gt; &lt;Length unit of measure&gt;'. E.g., '7 ft'.
    """
