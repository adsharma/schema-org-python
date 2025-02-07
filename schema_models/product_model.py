from datetime import date, datetime, time
from typing import List, Optional, Union

from pydantic import ConfigDict, Field, HttpUrl, field_validator

from schema_models.product import Product
from schema_models.product_group import ProductGroup
from schema_models.product_model import ProductModel


class ProductModel(Product):
    successorOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
    isVariantOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
    isVariantOf: Optional[Union[ProductGroup, List[ProductGroup]]] = None
    predecessorOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
