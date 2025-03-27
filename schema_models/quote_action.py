from dataclasses import dataclass

from schema_models.trade_action import TradeAction


@dataclass
class QuoteAction(TradeAction):
    """
    An agent quotes/estimates/appraises an object/product/service with a price at a location/store.
    """
