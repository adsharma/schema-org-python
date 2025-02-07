from typing import List, Optional, Union

from schema_models.car_usage_type import CarUsageType
from schema_models.date import Date
from schema_models.drive_wheel_configuration_value import DriveWheelConfigurationValue
from schema_models.engine_specification import EngineSpecification
from schema_models.number import Number
from schema_models.product import Product
from schema_models.qualitative_value import QualitativeValue
from schema_models.quantitative_value import QuantitativeValue
from schema_models.steering_position_value import SteeringPositionValue
from schema_models.text import Text
from schema_models.url import URL


class Vehicle(Product):
    numberOfAirbags: Optional[Union[Number, List[Number]]] = None
    numberOfAirbags: Optional[Union[Text, List[Text]]] = None
    stupidProperty: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    vehicleSeatingCapacity: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    vehicleSeatingCapacity: Optional[Union[Number, List[Number]]] = None
    vehicleIdentificationNumber: Optional[Union[Text, List[Text]]] = None
    vehicleInteriorColor: Optional[Union[Text, List[Text]]] = None
    speed: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    weightTotal: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    vehicleModelDate: Optional[Union[Date, List[Date]]] = None
    cargoVolume: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    seatingCapacity: Optional[Union[Number, List[Number]]] = None
    seatingCapacity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    tongueWeight: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfPreviousOwners: Optional[Union[Number, List[Number]]] = None
    numberOfPreviousOwners: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    knownVehicleDamages: Optional[Union[Text, List[Text]]] = None
    purchaseDate: Optional[Union[Date, List[Date]]] = None
    callSign: Optional[Union[Text, List[Text]]] = None
    dateVehicleFirstRegistered: Optional[Union[Date, List[Date]]] = None
    vehicleEngine: Optional[Union[EngineSpecification, List[EngineSpecification]]] = (
        None
    )
    wheelbase: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    trailerWeight: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    fuelType: Optional[Union[URL, List[URL]]] = None
    fuelType: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    fuelType: Optional[Union[Text, List[Text]]] = None
    productionDate: Optional[Union[Date, List[Date]]] = None
    mileageFromOdometer: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = (
        None
    )
    bodyType: Optional[Union[Text, List[Text]]] = None
    bodyType: Optional[Union[URL, List[URL]]] = None
    bodyType: Optional[Union[QualitativeValue, List[QualitativeValue]]] = None
    driveWheelConfiguration: Optional[Union[Text, List[Text]]] = None
    driveWheelConfiguration: Optional[
        Union[DriveWheelConfigurationValue, List[DriveWheelConfigurationValue]]
    ] = None
    numberOfAxles: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfAxles: Optional[Union[Number, List[Number]]] = None
    payload: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    fuelEfficiency: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    modelDate: Optional[Union[Date, List[Date]]] = None
    fuelConsumption: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfDoors: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    numberOfDoors: Optional[Union[Number, List[Number]]] = None
    meetsEmissionStandard: Optional[Union[QualitativeValue, List[QualitativeValue]]] = (
        None
    )
    meetsEmissionStandard: Optional[Union[Text, List[Text]]] = None
    meetsEmissionStandard: Optional[Union[URL, List[URL]]] = None
    vehicleSpecialUsage: Optional[Union[CarUsageType, List[CarUsageType]]] = None
    vehicleSpecialUsage: Optional[Union[Text, List[Text]]] = None
    vehicleTransmission: Optional[Union[QualitativeValue, List[QualitativeValue]]] = (
        None
    )
    vehicleTransmission: Optional[Union[Text, List[Text]]] = None
    vehicleTransmission: Optional[Union[URL, List[URL]]] = None
    accelerationTime: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    steeringPosition: Optional[
        Union[SteeringPositionValue, List[SteeringPositionValue]]
    ] = None
    numberOfForwardGears: Optional[
        Union[QuantitativeValue, List[QuantitativeValue]]
    ] = None
    numberOfForwardGears: Optional[Union[Number, List[Number]]] = None
    vehicleInteriorType: Optional[Union[Text, List[Text]]] = None
    fuelCapacity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = None
    vehicleConfiguration: Optional[Union[Text, List[Text]]] = None
    emissionsCO2: Optional[Union[Number, List[Number]]] = None
