from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.thing import Thing


class Product(Thing):
    """
    Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.
    """

    hasMerchantReturnPolicy: Optional[
        Union["MerchantReturnPolicy", List["MerchantReturnPolicy"]]
    ] = None
    audience: Optional[Union["Audience", List["Audience"]]] = None
    width: Optional[Union["Distance", List["Distance"]]] = None
    width: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    hasEnergyConsumptionDetails: Optional[
        Union["EnergyConsumptionDetails", List["EnergyConsumptionDetails"]]
    ] = None
    countryOfAssembly: Optional[Union[str, List[str]]] = None
    negativeNotes: Optional[Union["WebContent", List["WebContent"]]] = None
    negativeNotes: Optional[Union["ItemList", List["ItemList"]]] = None
    negativeNotes: Optional[Union["ListItem", List["ListItem"]]] = None
    negativeNotes: Optional[Union[str, List[str]]] = None
    height: Optional[Union["Distance", List["Distance"]]] = None
    height: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    pattern: Optional[Union[str, List[str]]] = None
    pattern: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    countryOfLastProcessing: Optional[Union[str, List[str]]] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    color: Optional[Union[str, List[str]]] = None
    reviews: Optional[Union["Review", List["Review"]]] = None
    awards: Optional[Union[str, List[str]]] = None
    material: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    material: Optional[Union["Product", List["Product"]]] = None
    material: Optional[Union[str, List[str]]] = None
    purchaseDate: Optional[Union[date, List[date]]] = None
    productID: Optional[Union[str, List[str]]] = None
    manufacturer: Optional[Union["Organization", List["Organization"]]] = None
    award: Optional[Union[str, List[str]]] = None
    hasProductReturnPolicy: Optional[
        Union["ProductReturnPolicy", List["ProductReturnPolicy"]]
    ] = None
    logo: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    logo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    isAccessoryOrSparePartFor: Optional[Union["Product", List["Product"]]] = None
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    keywords: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    keywords: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    keywords: Optional[Union[str, List[str]]] = None
    hasAdultConsideration: Optional[
        Union["AdultOrientedEnumeration", List["AdultOrientedEnumeration"]]
    ] = None
    itemCondition: Optional[Union["OfferItemCondition", List["OfferItemCondition"]]] = (
        None
    )
    offers: Optional[Union["Offer", List["Offer"]]] = None
    offers: Optional[Union["Demand", List["Demand"]]] = None
    hasMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    gtin13: Optional[Union[str, List[str]]] = None
    asin: Optional[Union[str, List[str]]] = None
    asin: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    model: Optional[Union[str, List[str]]] = None
    model: Optional[Union["ProductModel", List["ProductModel"]]] = None
    isConsumableFor: Optional[Union["Product", List["Product"]]] = None
    isVariantOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
    isVariantOf: Optional[Union["ProductGroup", List["ProductGroup"]]] = None
    inProductGroupWithID: Optional[Union[str, List[str]]] = None
    depth: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    depth: Optional[Union["Distance", List["Distance"]]] = None
    isRelatedTo: Optional[Union["Product", List["Product"]]] = None
    isRelatedTo: Optional[Union["Service", List["Service"]]] = None
    mobileUrl: Optional[Union[str, List[str]]] = None
    weight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    sku: Optional[Union[str, List[str]]] = None
    gtin: Optional[Union[str, List[str]]] = None
    gtin: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    isFamilyFriendly: Optional[Union[bool, List[bool]]] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    productionDate: Optional[Union[date, List[date]]] = None
    size: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    size: Optional[Union["SizeSpecification", List["SizeSpecification"]]] = None
    size: Optional[Union[str, List[str]]] = None
    size: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    mpn: Optional[Union[str, List[str]]] = None
    slogan: Optional[Union[str, List[str]]] = None
    gtin14: Optional[Union[str, List[str]]] = None
    gtin12: Optional[Union[str, List[str]]] = None
    isSimilarTo: Optional[Union["Product", List["Product"]]] = None
    isSimilarTo: Optional[Union["Service", List["Service"]]] = None
    releaseDate: Optional[Union[date, List[date]]] = None
    brand: Optional[Union["Organization", List["Organization"]]] = None
    brand: Optional[Union["Brand", List["Brand"]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union["PhysicalActivityCategory", List["PhysicalActivityCategory"]]
    ] = None
    category: Optional[Union["CategoryCode", List["CategoryCode"]]] = None
    category: Optional[Union[str, List[str]]] = None
    category: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    positiveNotes: Optional[Union["ItemList", List["ItemList"]]] = None
    positiveNotes: Optional[Union["WebContent", List["WebContent"]]] = None
    positiveNotes: Optional[Union["ListItem", List["ListItem"]]] = None
    positiveNotes: Optional[Union[str, List[str]]] = None
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    colorSwatch: Optional[Union["ImageObject", List["ImageObject"]]] = None
    colorSwatch: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    nsn: Optional[Union[str, List[str]]] = None
    gtin8: Optional[Union[str, List[str]]] = None
