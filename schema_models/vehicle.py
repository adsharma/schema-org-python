from datetime import date
from typing import List, Optional, Union

from pydantic import HttpUrl

from schema_models.product import Product


class Vehicle(Product):
    numberOfAirbags: Optional[Union[float, List[float]]] = None
    numberOfAirbags: Optional[Union[str, List[str]]] = None
    stupidProperty: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    vehicleSeatingCapacity: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    vehicleSeatingCapacity: Optional[Union[float, List[float]]] = None
    vehicleIdentificationNumber: Optional[Union[str, List[str]]] = None
    vehicleInteriorColor: Optional[Union[str, List[str]]] = None
    speed: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    weightTotal: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    vehicleModelDate: Optional[Union[date, List[date]]] = None
    cargoVolume: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    seatingCapacity: Optional[Union[float, List[float]]] = None
    seatingCapacity: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    tongueWeight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    numberOfPreviousOwners: Optional[Union[float, List[float]]] = None
    numberOfPreviousOwners: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    knownVehicleDamages: Optional[Union[str, List[str]]] = None
    purchaseDate: Optional[Union[date, List[date]]] = None
    callSign: Optional[Union[str, List[str]]] = None
    dateVehicleFirstRegistered: Optional[Union[date, List[date]]] = None
    vehicleEngine: Optional[
        Union["EngineSpecification", List["EngineSpecification"]]
    ] = None
    wheelbase: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    trailerWeight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    fuelType: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    fuelType: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    fuelType: Optional[Union[str, List[str]]] = None
    productionDate: Optional[Union[date, List[date]]] = None
    mileageFromOdometer: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    bodyType: Optional[Union[str, List[str]]] = None
    bodyType: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    bodyType: Optional[Union["QualitativeValue", List["QualitativeValue"]]] = None
    driveWheelConfiguration: Optional[Union[str, List[str]]] = None
    driveWheelConfiguration: Optional[
        Union["DriveWheelConfigurationValue", List["DriveWheelConfigurationValue"]]
    ] = None
    numberOfAxles: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    numberOfAxles: Optional[Union[float, List[float]]] = None
    payload: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    fuelEfficiency: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    modelDate: Optional[Union[date, List[date]]] = None
    fuelConsumption: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    numberOfDoors: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = (
        None
    )
    numberOfDoors: Optional[Union[float, List[float]]] = None
    meetsEmissionStandard: Optional[
        Union["QualitativeValue", List["QualitativeValue"]]
    ] = None
    meetsEmissionStandard: Optional[Union[str, List[str]]] = None
    meetsEmissionStandard: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    vehicleSpecialUsage: Optional[Union["CarUsageType", List["CarUsageType"]]] = None
    vehicleSpecialUsage: Optional[Union[str, List[str]]] = None
    vehicleTransmission: Optional[
        Union["QualitativeValue", List["QualitativeValue"]]
    ] = None
    vehicleTransmission: Optional[Union[str, List[str]]] = None
    vehicleTransmission: Optional[Union[HttpUrl, List[HttpUrl]]] = None
    accelerationTime: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    steeringPosition: Optional[
        Union["SteeringPositionValue", List["SteeringPositionValue"]]
    ] = None
    numberOfForwardGears: Optional[
        Union["QuantitativeValue", List["QuantitativeValue"]]
    ] = None
    numberOfForwardGears: Optional[Union[float, List[float]]] = None
    vehicleInteriorType: Optional[Union[str, List[str]]] = None
    fuelCapacity: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = None
    vehicleConfiguration: Optional[Union[str, List[str]]] = None
    emissionsCO2: Optional[Union[float, List[float]]] = None
