from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.distance import Distance
from schema_models.mass import Mass
from schema_models.organization import Organization
from schema_models.person import Person
from schema_models.place import Place
from schema_models.thing import Thing


@dataclass
class Product(Thing):
    """
    Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.
    """

    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = None
    asin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    audience: Optional[Union["Audience", List["Audience"]]] = None
    authorizedRepresentative: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    award: Optional[Union[str, List[str]]] = None
    awards: Optional[Union[str, List[str]]] = None
    brand: Optional[Union["Brand", List["Brand"], Organization, List[Organization]]] = (
        None
    )
    category: Optional[
        Union[
            "CategoryCode",
            List["CategoryCode"],
            "PhysicalActivityCategory",
            List["PhysicalActivityCategory"],
            str,
            List[str],
            Thing,
            List[Thing],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    color: Optional[Union[str, List[str]]] = None
    colorSwatch: Optional[
        Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]
    ] = None
    consumerNotice: Optional[
        Union[
            str,
            List[str],
            "TextObject",
            List["TextObject"],
            HttpUrl,
            List[HttpUrl],
            "WebContent",
            List["WebContent"],
        ]
    ] = None
    countryOfAssembly: Optional[Union[str, List[str]]] = None
    countryOfLastProcessing: Optional[Union[str, List[str]]] = None
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = None
    depth: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    displayLocation: Optional[Union[Place, List[Place]]] = None
    funding: Optional[Union["Grant", List["Grant"]]] = None
    gtin12: Optional[Union[str, List[str]]] = None
    gtin13: Optional[Union[str, List[str]]] = None
    gtin14: Optional[Union[str, List[str]]] = None
    gtin8: Optional[Union[str, List[str]]] = None
    gtin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = None
    hasAdultConsideration: Optional[
        Union["AdultOrientedEnumeration", List["AdultOrientedEnumeration"]]
    ] = None
    hasCertification: Optional[Union["Certification", List["Certification"]]] = None
    hasDigitalProductPassport: Optional[
        Union[
            "DigitalProductPassport",
            List["DigitalProductPassport"],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    hasEnergyConsumptionDetails: Optional[
        Union["EnergyConsumptionDetails", List["EnergyConsumptionDetails"]]
    ] = None
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    hasMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    hasMerchantReturnPolicy: Optional[
        Union["MerchantReturnPolicy", List["MerchantReturnPolicy"]]
    ] = None
    hasProductReturnPolicy: Optional[
        Union["ProductReturnPolicy", List["ProductReturnPolicy"]]
    ] = None
    height: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    importer: Optional[
        Union[Organization, List[Organization], Person, List[Person]]
    ] = None
    inProductGroupWithID: Optional[Union[str, List[str]]] = None
    isAccessoryOrSparePartFor: Optional[Union["Product", List["Product"]]] = None
    isConsumableFor: Optional[Union["Product", List["Product"]]] = None
    isFamilyFriendly: Optional[Union[bool, List[bool]]] = None
    isOftenBoughtWith: Optional[Union["Product", List["Product"]]] = None
    isRelatedTo: Optional[
        Union["Product", List["Product"], "Service", List["Service"]]
    ] = None
    isSimilarTo: Optional[
        Union["Product", List["Product"], "Service", List["Service"]]
    ] = None
    isVariantOf: Optional[
        Union[
            "ProductGroup", List["ProductGroup"], "ProductModel", List["ProductModel"]
        ]
    ] = None
    itemCondition: Optional[Union["OfferItemCondition", List["OfferItemCondition"]]] = (
        None
    )
    keywords: Optional[
        Union[
            "DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]
        ]
    ] = None
    logo: Optional[
        Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]
    ] = None
    manufacturer: Optional[Union[Organization, List[Organization]]] = None
    material: Optional[
        Union["Product", List["Product"], str, List[str], HttpUrl, List[HttpUrl]]
    ] = None
    mobileUrl: Optional[Union[str, List[str]]] = None
    model: Optional[Union["ProductModel", List["ProductModel"], str, List[str]]] = None
    mpn: Optional[Union[str, List[str]]] = None
    negativeNotes: Optional[
        Union[
            "ItemList",
            List["ItemList"],
            "ListItem",
            List["ListItem"],
            str,
            List[str],
            "WebContent",
            List["WebContent"],
        ]
    ] = None
    nsn: Optional[Union[str, List[str]]] = None
    offers: Optional[Union["Demand", List["Demand"], "Offer", List["Offer"]]] = None
    pattern: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = None
    positiveNotes: Optional[
        Union[
            "ItemList",
            List["ItemList"],
            "ListItem",
            List["ListItem"],
            str,
            List[str],
            "WebContent",
            List["WebContent"],
        ]
    ] = None
    productID: Optional[Union[str, List[str]]] = None
    productionDate: Optional[Union[date, List[date]]] = None
    purchaseDate: Optional[Union[date, List[date]]] = None
    recycledContentPercentage: Optional[Union[float, List[float]]] = None
    releaseDate: Optional[Union[date, List[date]]] = None
    review: Optional[Union["Review", List["Review"]]] = None
    reviews: Optional[Union["Review", List["Review"]]] = None
    size: Optional[
        Union[
            "DefinedTerm",
            List["DefinedTerm"],
            "QuantitativeValue",
            List["QuantitativeValue"],
            "SizeSpecification",
            List["SizeSpecification"],
            str,
            List[str],
        ]
    ] = None
    sku: Optional[Union[str, List[str]]] = None
    slogan: Optional[Union[str, List[str]]] = None
    specification: Optional[Union["PropertyValue", List["PropertyValue"]]] = None
    substanceOfConcern: Optional[
        Union[
            "ChemicalSubstance",
            List["ChemicalSubstance"],
            "DefinedTerm",
            List["DefinedTerm"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    weight: Optional[
        Union[Mass, List[Mass], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    width: Optional[
        Union[Distance, List[Distance], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
