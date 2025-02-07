from typing import List, Optional, Union

from schema_models.boolean import Boolean
from schema_models.date import Date
from schema_models.text import Text
from schema_models.thing import Thing
from schema_models.url import URL


class Product(Thing):
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
    countryOfAssembly: Optional[Union[Text, List[Text]]] = None
    negativeNotes: Optional[Union["WebContent", List["WebContent"]]] = None
    negativeNotes: Optional[Union["ItemList", List["ItemList"]]] = None
    negativeNotes: Optional[Union["ListItem", List["ListItem"]]] = None
    negativeNotes: Optional[Union[Text, List[Text]]] = None
    height: Optional[Union["Distance", List["Distance"]]] = None
    height: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    pattern: Optional[Union[Text, List[Text]]] = None
    pattern: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    countryOfLastProcessing: Optional[Union[Text, List[Text]]] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    color: Optional[Union[Text, List[Text]]] = None
    reviews: Optional[Union["Review", List["Review"]]] = None
    awards: Optional[Union[Text, List[Text]]] = None
    material: Optional[Union[URL, List[URL]]] = None
    material: Optional[Union["Product", List["Product"]]] = None
    material: Optional[Union[Text, List[Text]]] = None
    purchaseDate: Optional[Union[Date, List[Date]]] = None
    productID: Optional[Union[Text, List[Text]]] = None
    manufacturer: Optional[Union["Organization", List["Organization"]]] = None
    award: Optional[Union[Text, List[Text]]] = None
    hasProductReturnPolicy: Optional[
        Union["ProductReturnPolicy", List["ProductReturnPolicy"]]
    ] = None
    logo: Optional[Union[URL, List[URL]]] = None
    logo: Optional[Union["ImageObject", List["ImageObject"]]] = None
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    isAccessoryOrSparePartFor: Optional[Union["Product", List["Product"]]] = None
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    keywords: Optional[Union[URL, List[URL]]] = None
    keywords: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    keywords: Optional[Union[Text, List[Text]]] = None
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
    gtin13: Optional[Union[Text, List[Text]]] = None
    asin: Optional[Union[Text, List[Text]]] = None
    asin: Optional[Union[URL, List[URL]]] = None
    model: Optional[Union[Text, List[Text]]] = None
    model: Optional[Union["ProductModel", List["ProductModel"]]] = None
    isConsumableFor: Optional[Union["Product", List["Product"]]] = None
    isVariantOf: Optional[Union["ProductModel", List["ProductModel"]]] = None
    isVariantOf: Optional[Union["ProductGroup", List["ProductGroup"]]] = None
    inProductGroupWithID: Optional[Union[Text, List[Text]]] = None
    depth: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    depth: Optional[Union["Distance", List["Distance"]]] = None
    isRelatedTo: Optional[Union["Product", List["Product"]]] = None
    isRelatedTo: Optional[Union["Service", List["Service"]]] = None
    mobileUrl: Optional[Union[Text, List[Text]]] = None
    weight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    sku: Optional[Union[Text, List[Text]]] = None
    gtin: Optional[Union[Text, List[Text]]] = None
    gtin: Optional[Union[URL, List[URL]]] = None
    isFamilyFriendly: Optional[Union[Boolean, List[Boolean]]] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    productionDate: Optional[Union[Date, List[Date]]] = None
    size: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    size: Optional[Union["SizeSpecification", List["SizeSpecification"]]] = None
    size: Optional[Union[Text, List[Text]]] = None
    size: Optional[Union["DefinedTerm", List["DefinedTerm"]]] = None
    mpn: Optional[Union[Text, List[Text]]] = None
    slogan: Optional[Union[Text, List[Text]]] = None
    gtin14: Optional[Union[Text, List[Text]]] = None
    gtin12: Optional[Union[Text, List[Text]]] = None
    isSimilarTo: Optional[Union["Product", List["Product"]]] = None
    isSimilarTo: Optional[Union["Service", List["Service"]]] = None
    releaseDate: Optional[Union[Date, List[Date]]] = None
    brand: Optional[Union["Organization", List["Organization"]]] = None
    brand: Optional[Union["Brand", List["Brand"]]] = None
    category: Optional[Union[Thing, List[Thing]]] = None
    category: Optional[
        Union["PhysicalActivityCategory", List["PhysicalActivityCategory"]]
    ] = None
    category: Optional[Union["CategoryCode", List["CategoryCode"]]] = None
    category: Optional[Union[Text, List[Text]]] = None
    category: Optional[Union[URL, List[URL]]] = None
    positiveNotes: Optional[Union["ItemList", List["ItemList"]]] = None
    positiveNotes: Optional[Union["WebContent", List["WebContent"]]] = None
    positiveNotes: Optional[Union["ListItem", List["ListItem"]]] = None
    positiveNotes: Optional[Union[Text, List[Text]]] = None
    hasGS1DigitalLink: Optional[Union[URL, List[URL]]] = None
    colorSwatch: Optional[Union["ImageObject", List["ImageObject"]]] = None
    colorSwatch: Optional[Union[URL, List[URL]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    nsn: Optional[Union[Text, List[Text]]] = None
    gtin8: Optional[Union[Text, List[Text]]] = None
