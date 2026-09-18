from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.product import Product


@dataclass
class Vehicle(Product):
    """
    A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space.
    """

    accelerationTime: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    bodyType: Optional[
        Union[
            "QualitativeValue",
            List["QualitativeValue"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    callSign: Optional[Union[str, List[str]]] = None
    cargoVolume: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    dateVehicleFirstRegistered: Optional[Union[date, List[date]]] = None
    driveWheelConfiguration: Optional[
        Union[
            "DriveWheelConfigurationValue",
            List["DriveWheelConfigurationValue"],
            str,
            List[str],
        ]
    ] = None
    emissionsCO2: Optional[Union[float, List[float]]] = None
    fuelCapacity: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    fuelConsumption: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    fuelEfficiency: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    fuelType: Optional[
        Union[
            "QualitativeValue",
            List["QualitativeValue"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    knownVehicleDamages: Optional[Union[str, List[str]]] = None
    meetsEmissionStandard: Optional[
        Union[
            "QualitativeValue",
            List["QualitativeValue"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    mileageFromOdometer: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    modelDate: Optional[Union[date, List[date]]] = None
    numberOfAirbags: Optional[Union[float, List[float], str, List[str]]] = None
    numberOfAxles: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    numberOfDoors: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    numberOfForwardGears: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    numberOfPreviousOwners: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    payload: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    productionDate: Optional[Union[date, List[date]]] = None
    purchaseDate: Optional[Union[date, List[date]]] = None
    seatingCapacity: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    speed: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    steeringPosition: Optional[
        Union["SteeringPositionValue", List["SteeringPositionValue"]]
    ] = None
    stupidProperty: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    tongueWeight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    trailerWeight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    vehicleConfiguration: Optional[Union[str, List[str]]] = None
    vehicleEngine: Optional[
        Union["EngineSpecification", List["EngineSpecification"]]
    ] = None
    vehicleIdentificationNumber: Optional[Union[str, List[str]]] = None
    vehicleInteriorColor: Optional[Union[str, List[str]]] = None
    vehicleInteriorType: Optional[Union[str, List[str]]] = None
    vehicleModelDate: Optional[Union[date, List[date]]] = None
    vehicleSeatingCapacity: Optional[
        Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    vehicleSpecialUsage: Optional[
        Union["CarUsageType", List["CarUsageType"], str, List[str]]
    ] = None
    vehicleTransmission: Optional[
        Union[
            "QualitativeValue",
            List["QualitativeValue"],
            str,
            List[str],
            HttpUrl,
            List[HttpUrl],
        ]
    ] = None
    weightTotal: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    wheelbase: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
