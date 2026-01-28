
## Class Diagram

```mermaid
classDiagram
    Attr <|-- StrAttr
    Attr <|-- DateAttr
    Attr <|-- NumberAttr
    NumberAttr <|-- LengthAttr
    NumberAttr <|-- MassAttr
    NumberAttr <|-- TempAttr
    NumberAttr <|-- VolumetricFlowAttr
    NumberAttr <|-- PowerAttr
    NumberAttr <|-- EnergyAttr
    NumberAttr <|-- PressureAttr
    PowerAttr <|-- AirPowerAttr
    AirPowerAttr <|-- AirThermalPowerAttr
    AirThermalPowerAttr <|-- AirCoolingThermalPowerAttr
    AirCoolingThermalPowerAttr <|-- AirRatedCoolingThermalPowerAttr
    AirCoolingThermalPowerAttr <|-- AirDesignCoolingThermalPowerAttr
    AirThermalPowerAttr <|-- AirHeatingThermalPowerAttr
    AirHeatingThermalPowerAttr <|-- AirRatedHeatingThermalPowerAttr
    AirHeatingThermalPowerAttr <|-- AirDesignHeatingThermalPowerAttr
    AirPowerAttr <|-- AirMechanicalPowerAttr
    AirMechanicalPowerAttr <|-- AirFanMechanicalPowerAttr
    AirFanMechanicalPowerAttr <|-- AirDesignFanMechanicalPowerAttr
    AirDesignFanMechanicalPowerAttr <|-- AirDischargeDesignFanMechanicalPowerAttr
    AirDesignFanMechanicalPowerAttr <|-- AirReturnDesignFanMechanicalPowerAttr
    AirFanMechanicalPowerAttr <|-- AirRatedFanMechanicalPowerAttr
    AirRatedFanMechanicalPowerAttr <|-- AirDischargeRatedFanMechanicalPowerAttr
    AirRatedFanMechanicalPowerAttr <|-- AirReturnRatedFanMechanicalPowerAttr
    PowerAttr <|-- WaterPowerAttr
    WaterPowerAttr <|-- WaterThermalPowerAttr
    WaterThermalPowerAttr <|-- WaterCoolingThermalPowerAttr
    WaterCoolingThermalPowerAttr <|-- WaterRatedCoolingThermalPowerAttr
    WaterCoolingThermalPowerAttr <|-- WaterDesignCoolingThermalPowerAttr
    WaterThermalPowerAttr <|-- WaterHeatingThermalPowerAttr
    WaterHeatingThermalPowerAttr <|-- WaterRatedHeatingThermalPowerAttr
    WaterHeatingThermalPowerAttr <|-- WaterDesignHeatingThermalPowerAttr
    WaterPowerAttr <|-- WaterMechanicalPowerAttr
    WaterMechanicalPowerAttr <|-- WaterPumpMechanicalPowerAttr
    WaterPumpMechanicalPowerAttr <|-- WaterDesignPumpMechanicalPowerAttr
    WaterPumpMechanicalPowerAttr <|-- WaterRatedPumpMechanicalPowerAttr
    PowerAttr <|-- ElecPowerAttr
    ElecPowerAttr <|-- ElecMotorPowerAttr
    ElecMotorPowerAttr <|-- ElecFanMotorPowerAttr
    ElecMotorPowerAttr <|-- ElecPumpMotorPowerAttr
    ElecFanMotorPowerAttr <|-- ElecDesignFanMotorPowerAttr
    ElecDesignFanMotorPowerAttr <|-- ElecDischargeDesignFanMotorPowerAttr
    ElecDesignFanMotorPowerAttr <|-- ElecReturnDesignFanMotorPowerAttr
    ElecPumpMotorPowerAttr <|-- ElecDesignPumpMotorPowerAttr
    ElecFanMotorPowerAttr <|-- ElecRatedFanMotorPowerAttr
    ElecRatedFanMotorPowerAttr <|-- ElecDischargeRatedFanMotorPowerAttr
    ElecRatedFanMotorPowerAttr <|-- ElecReturnRatedFanMotorPowerAttr
    ElecPumpMotorPowerAttr <|-- ElecRatedPumpMotorPowerAttr
    PowerAttr <|-- NaturalGasPowerAttr
    NaturalGasPowerAttr <|-- NaturalGasInputPowerAttr
    NaturalGasInputPowerAttr <|-- NaturalGasRatedInputPowerAttr
    NaturalGasInputPowerAttr <|-- NaturalGasDesignInputPowerAttr
    PowerAttr <|-- FuelOilPowerAttr
    FuelOilPowerAttr <|-- FuelOilInputPowerAttr
    FuelOilInputPowerAttr <|-- FuelOilRatedInputPowerAttr
    FuelOilInputPowerAttr <|-- FuelOilDesignInputPowerAttr
    PowerAttr <|-- PropanePowerAttr
    PropanePowerAttr <|-- PropaneInputPowerAttr
    PropaneInputPowerAttr <|-- PropaneRatedInputPowerAttr
    PropaneInputPowerAttr <|-- PropaneDesignInputPowerAttr
    PowerAttr <|-- DieselPowerAttr
    DieselPowerAttr <|-- DieselInputPowerAttr
    DieselInputPowerAttr <|-- DieselRatedInputPowerAttr
    DieselInputPowerAttr <|-- DieselDesignInputPowerAttr
    TempAttr <|-- AirTempAttr
    AirTempAttr <|-- AirOperatingTempAttr
    AirOperatingTempAttr <|-- AirRatedOperatingTempAttr
    AirRatedOperatingTempAttr <|-- AirMinRatedOperatingTempAttr
    AirRatedOperatingTempAttr <|-- AirMaxRatedOperatingTempAttr
    AirTempAttr <|-- AirDesignTempAttr
    AirDesignTempAttr <|-- AirDischargeDesignTempAttr
    TempAttr <|-- WaterTempAttr
    WaterTempAttr <|-- WaterOperatingTempAttr
    WaterOperatingTempAttr <|-- WaterRatedOperatingTempAttr
    WaterRatedOperatingTempAttr <|-- WaterMinRatedOperatingTempAttr
    WaterRatedOperatingTempAttr <|-- WaterMaxRatedOperatingTempAttr
    WaterTempAttr <|-- WaterDesignTempAttr
    WaterDesignTempAttr <|-- WaterEnteringDesignTempAttr
    WaterEnteringDesignTempAttr <|-- WaterChilledEnteringDesignTempAttr
    WaterEnteringDesignTempAttr <|-- WaterHotEnteringDesignTempAttr
    WaterDesignTempAttr <|-- WaterLeavingDesignTempAttr
    WaterLeavingDesignTempAttr <|-- WaterChilledLeavingDesignTempAttr
    WaterLeavingDesignTempAttr <|-- WaterHotLeavingDesignTempAttr
    PressureAttr <|-- AirPressureAttr
    AirPressureAttr <|-- AirDesignPressureAttr
    AirDesignPressureAttr <|-- AirDesignFanPressureAttr
    AirPressureAttr <|-- AirRatedPressureAttr
    AirRatedPressureAttr <|-- AirRatedFanPressureAttr
    PressureAttr <|-- WaterPressureAttr
    WaterPressureAttr <|-- WaterDesignPressureAttr
    WaterDesignPressureAttr <|-- WaterDesignPumpPressureAttr
    WaterDesignPressureAttr <|-- WaterDesignChillerPressureAttr
    WaterPressureAttr <|-- WaterRatedPressureAttr
    WaterRatedPressureAttr <|-- WaterChillerMinRatedPressureAttr
    VolumetricFlowAttr <|-- AirFlowAttr
    AirFlowAttr <|-- AirDesignFlowAttr
    AirDesignFlowAttr <|-- AirMaxDesignFlowAttr
    AirMaxDesignFlowAttr <|-- AirDischargeMaxDesignFlowAttr
    AirDischargeMaxDesignFlowAttr <|-- AirCoolingDischargeMaxDesignFlowAttr
    AirDischargeMaxDesignFlowAttr <|-- AirHeatingDischargeMaxDesignFlowAttr
    AirMaxDesignFlowAttr <|-- AirOutdoorMaxDesignFlowAttr
    AirDesignFlowAttr <|-- AirMinDesignFlowAttr
    AirMinDesignFlowAttr <|-- AirDischargeMinDesignFlowAttr
    AirDischargeMinDesignFlowAttr <|-- AirCoolingDischargeMinDesignFlowAttr
    AirDischargeMinDesignFlowAttr <|-- AirHeatingDischargeMinDesignFlowAttr
    AirMinDesignFlowAttr <|-- AirOutdoorMinDesignFlowAttr
    AirFlowAttr <|-- AirRatedFlowAttr
    AirRatedFlowAttr <|-- AirMaxRatedFlowAttr
    AirMaxRatedFlowAttr <|-- AirDischargeMaxRatedFlowAttr
    AirDischargeMaxRatedFlowAttr <|-- AirCoolingDischargeMaxRatedFlowAttr
    AirDischargeMaxRatedFlowAttr <|-- AirHeatingDischargeMaxRatedFlowAttr
    AirMaxRatedFlowAttr <|-- AirOutdoorMaxRatedFlowAttr
    AirRatedFlowAttr <|-- AirMinRatedFlowAttr
    AirMinRatedFlowAttr <|-- AirDischargeMinRatedFlowAttr
    VolumetricFlowAttr <|-- WaterFlowAttr
    WaterFlowAttr <|-- WaterDesignFlowAttr
    WaterFlowAttr <|-- WaterRatedFlowAttr
    WaterDesignFlowAttr <|-- WaterMaxDesignFlowAttr
    WaterMaxDesignFlowAttr <|-- WaterChilledMaxDesignFlowAttr
    WaterMaxDesignFlowAttr <|-- WaterHotMaxDesignFlowAttr
    WaterDesignFlowAttr <|-- WaterMinDesignFlowAttr
    WaterRatedFlowAttr <|-- WaterMaxRatedFlowAttr
    WaterRatedFlowAttr <|-- WaterMinRatedFlowAttr
    NumberAttr <|-- ElecCurrentAttr
    ElecCurrentAttr <|-- ElecAcCurrentAttr
    ElecAcCurrentAttr <|-- ElecRatedAcCurrentAttr
    ElecRatedAcCurrentAttr <|-- ElecContinuousCapacityRatedAcCurrentAttr
    ElecRatedAcCurrentAttr <|-- ElecContinuousRatedAcCurrentAttr
    ElecContinuousRatedAcCurrentAttr <|-- ElecMaxContinuousRatedAcCurrentAttr
    ElecRatedAcCurrentAttr <|-- ElecInputRatedAcCurrentAttr
    ElecInputRatedAcCurrentAttr <|-- ElecMaxInputRatedAcCurrentAttr
    NumberAttr <|-- ElecVoltAttr
    ElecVoltAttr <|-- ElecAcVoltAttr
    ElecAcVoltAttr <|-- ElecRatedAcVoltAttr
    ElecRatedAcVoltAttr <|-- ElecInputRatedAcVoltAttr
    ElecInputRatedAcVoltAttr <|-- ElecNominalInputRatedAcVoltAttr
    ElecNominalInputRatedAcVoltAttr <|-- ElecLineToLineNominalInputRatedAcVoltAttr
    ElecNominalInputRatedAcVoltAttr <|-- ElecLineToNeutralNominalInputRatedAcVoltAttr
    ElecInputRatedAcVoltAttr <|-- ElecMinInputRatedAcVoltAttr
    ElecMinInputRatedAcVoltAttr <|-- ElecLineToLineMinInputRatedAcVoltAttr
    ElecInputRatedAcVoltAttr <|-- ElecMaxInputRatedAcVoltAttr
    ElecMaxInputRatedAcVoltAttr <|-- ElecLineToLineMaxInputRatedAcVoltAttr
    StrAttr <|-- ManufacturerAttr
    StrAttr <|-- ModelSeriesAttr
    StrAttr <|-- ModelNumberAttr
    StrAttr <|-- SerialNumberAttr
    DateAttr <|-- ManufactureDateAttr
    LengthAttr <|-- DimensionLengthAttr
    LengthAttr <|-- DimensionWidthAttr
    LengthAttr <|-- DimensionHeightAttr
    MassAttr <|-- WeightAttr

    class StrAttr {
        <<abstract>>
    }
    class DateAttr {
        <<abstract>>
    }
    class NumberAttr {
        <<abstract>>
    }
    class LengthAttr {
        <<abstract>>
    }
    class MassAttr {
        <<abstract>>
    }
    class TempAttr {
        <<abstract>>
    }
    class VolumetricFlowAttr {
        <<abstract>>
    }
    class PowerAttr {
        <<abstract>>
    }
    class EnergyAttr {
        <<abstract>>
    }
    class PressureAttr {
        <<abstract>>
    }
    class AirPowerAttr {
        <<abstract>>
        +air
    }
    class AirThermalPowerAttr {
        <<abstract>>
        +thermal
    }
    class AirCoolingThermalPowerAttr {
        <<abstract>>
        +cooling
    }
    class AirRatedCoolingThermalPowerAttr {
        +rated
    }
    class AirDesignCoolingThermalPowerAttr {
        +design
    }
    class AirHeatingThermalPowerAttr {
        <<abstract>>
        +heating
    }
    class AirRatedHeatingThermalPowerAttr {
        +rated
    }
    class AirDesignHeatingThermalPowerAttr {
        +design
    }
    class AirMechanicalPowerAttr {
        <<abstract>>
        +mechanical
    }
    class AirFanMechanicalPowerAttr {
        <<abstract>>
        +fan
    }
    class AirDesignFanMechanicalPowerAttr {
        <<abstract>>
        +design
    }
    class AirDischargeDesignFanMechanicalPowerAttr {
        +discharge
    }
    class AirReturnDesignFanMechanicalPowerAttr {
        +return
    }
    class AirRatedFanMechanicalPowerAttr {
        <<abstract>>
        +rated
    }
    class AirDischargeRatedFanMechanicalPowerAttr {
        +discharge
    }
    class AirReturnRatedFanMechanicalPowerAttr {
        +return
    }
    class WaterPowerAttr {
        <<abstract>>
        +water
    }
    class WaterThermalPowerAttr {
        <<abstract>>
        +thermal
    }
    class WaterCoolingThermalPowerAttr {
        <<abstract>>
        +cooling
    }
    class WaterRatedCoolingThermalPowerAttr {
        +rated
    }
    class WaterDesignCoolingThermalPowerAttr {
        +design
    }
    class WaterHeatingThermalPowerAttr {
        <<abstract>>
        +heating
    }
    class WaterRatedHeatingThermalPowerAttr {
        +rated
    }
    class WaterDesignHeatingThermalPowerAttr {
        +design
    }
    class WaterMechanicalPowerAttr {
        <<abstract>>
        +mechanical
    }
    class WaterPumpMechanicalPowerAttr {
        <<abstract>>
        +pump
    }
    class WaterDesignPumpMechanicalPowerAttr {
        +design
    }
    class WaterRatedPumpMechanicalPowerAttr {
        +rated
    }
    class ElecPowerAttr {
        <<abstract>>
        +elec
    }
    class ElecMotorPowerAttr {
        <<abstract>>
        +motor
    }
    class ElecFanMotorPowerAttr {
        <<abstract>>
        +fan
    }
    class ElecPumpMotorPowerAttr {
        <<abstract>>
        +pump
    }
    class ElecDesignFanMotorPowerAttr {
        <<abstract>>
        +design
    }
    class ElecDischargeDesignFanMotorPowerAttr {
        +discharge
    }
    class ElecReturnDesignFanMotorPowerAttr {
        +return
    }
    class ElecDesignPumpMotorPowerAttr {
        +design
    }
    class ElecRatedFanMotorPowerAttr {
        <<abstract>>
        +rated
    }
    class ElecDischargeRatedFanMotorPowerAttr {
        +discharge
    }
    class ElecReturnRatedFanMotorPowerAttr {
        +return
    }
    class ElecRatedPumpMotorPowerAttr {
        +rated
    }
    class NaturalGasPowerAttr {
        <<abstract>>
        +naturalGas
    }
    class NaturalGasInputPowerAttr {
        <<abstract>>
        +input
    }
    class NaturalGasRatedInputPowerAttr {
        +rated
    }
    class NaturalGasDesignInputPowerAttr {
        +design
    }
    class FuelOilPowerAttr {
        <<abstract>>
        +fuelOil
    }
    class FuelOilInputPowerAttr {
        <<abstract>>
        +input
    }
    class FuelOilRatedInputPowerAttr {
        +rated
    }
    class FuelOilDesignInputPowerAttr {
        +design
    }
    class PropanePowerAttr {
        <<abstract>>
        +propane
    }
    class PropaneInputPowerAttr {
        <<abstract>>
        +input
    }
    class PropaneRatedInputPowerAttr {
        +rated
    }
    class PropaneDesignInputPowerAttr {
        +design
    }
    class DieselPowerAttr {
        <<abstract>>
        +diesel
    }
    class DieselInputPowerAttr {
        <<abstract>>
        +input
    }
    class DieselRatedInputPowerAttr {
        +rated
    }
    class DieselDesignInputPowerAttr {
        +design
    }
    class AirTempAttr {
        <<abstract>>
        +air
    }
    class AirOperatingTempAttr {
        <<abstract>>
        +operating
    }
    class AirRatedOperatingTempAttr {
        <<abstract>>
        +rated
    }
    class AirMinRatedOperatingTempAttr {
        +min
    }
    class AirMaxRatedOperatingTempAttr {
        +max
    }
    class AirDesignTempAttr {
        <<abstract>>
        +design
    }
    class AirDischargeDesignTempAttr {
        +discharge
    }
    class WaterTempAttr {
        <<abstract>>
        +water
    }
    class WaterOperatingTempAttr {
        <<abstract>>
        +operating
    }
    class WaterRatedOperatingTempAttr {
        <<abstract>>
        +rated
    }
    class WaterMinRatedOperatingTempAttr {
        +min
    }
    class WaterMaxRatedOperatingTempAttr {
        +max
    }
    class WaterDesignTempAttr {
        <<abstract>>
        +design
    }
    class WaterEnteringDesignTempAttr {
        <<abstract>>
        +entering
    }
    class WaterChilledEnteringDesignTempAttr {
        +chilled
    }
    class WaterHotEnteringDesignTempAttr {
        +hot
    }
    class WaterLeavingDesignTempAttr {
        <<abstract>>
        +leaving
    }
    class WaterChilledLeavingDesignTempAttr {
        +chilled
    }
    class WaterHotLeavingDesignTempAttr {
        +hot
    }
    class AirPressureAttr {
        <<abstract>>
        +air
    }
    class AirDesignPressureAttr {
        <<abstract>>
        +design
    }
    class AirDesignFanPressureAttr {
        +fan
    }
    class AirRatedPressureAttr {
        <<abstract>>
        +rated
    }
    class AirRatedFanPressureAttr {
        +fan
    }
    class WaterPressureAttr {
        <<abstract>>
        +water
    }
    class WaterDesignPressureAttr {
        <<abstract>>
        +design
    }
    class WaterDesignPumpPressureAttr {
        +pump
    }
    class WaterDesignChillerPressureAttr {
        +chiller
    }
    class WaterRatedPressureAttr {
        <<abstract>>
        +rated
    }
    class WaterChillerMinRatedPressureAttr {
        +chiller, min
    }
    class AirFlowAttr {
        <<abstract>>
        +air
    }
    class AirDesignFlowAttr {
        <<abstract>>
        +design
    }
    class AirMaxDesignFlowAttr {
        <<abstract>>
        +max
    }
    class AirDischargeMaxDesignFlowAttr {
        +discharge
    }
    class AirCoolingDischargeMaxDesignFlowAttr {
        +cooling
    }
    class AirHeatingDischargeMaxDesignFlowAttr {
        +heating
    }
    class AirOutdoorMaxDesignFlowAttr {
        +outdoor
    }
    class AirMinDesignFlowAttr {
        <<abstract>>
        +min
    }
    class AirDischargeMinDesignFlowAttr {
        +discharge
    }
    class AirCoolingDischargeMinDesignFlowAttr {
        +cooling
    }
    class AirHeatingDischargeMinDesignFlowAttr {
        +heating
    }
    class AirOutdoorMinDesignFlowAttr {
        +outdoor
    }
    class AirRatedFlowAttr {
        <<abstract>>
        +rated
    }
    class AirMaxRatedFlowAttr {
        <<abstract>>
        +max
    }
    class AirDischargeMaxRatedFlowAttr {
        +discharge
    }
    class AirCoolingDischargeMaxRatedFlowAttr {
        +cooling
    }
    class AirHeatingDischargeMaxRatedFlowAttr {
        +heating
    }
    class AirOutdoorMaxRatedFlowAttr {
        +outdoor
    }
    class AirMinRatedFlowAttr {
        <<abstract>>
        +min
    }
    class AirDischargeMinRatedFlowAttr {
        +discharge
    }
    class WaterFlowAttr {
        <<abstract>>
        +water
    }
    class WaterDesignFlowAttr {
        <<abstract>>
        +design
    }
    class WaterRatedFlowAttr {
        <<abstract>>
        +rated
    }
    class WaterMaxDesignFlowAttr {
        <<abstract>>
        +max
    }
    class WaterChilledMaxDesignFlowAttr {
        +chilled
    }
    class WaterHotMaxDesignFlowAttr {
        +hot
    }
    class WaterMinDesignFlowAttr {
        +min
    }
    class WaterMaxRatedFlowAttr {
        +max
    }
    class WaterMinRatedFlowAttr {
        +min
    }
    class ElecCurrentAttr {
        <<abstract>>
        +elec, current
    }
    class ElecAcCurrentAttr {
        <<abstract>>
        +ac
    }
    class ElecRatedAcCurrentAttr {
        <<abstract>>
        +rated
    }
    class ElecContinuousCapacityRatedAcCurrentAttr {
        +currentContinuousCapacity
    }
    class ElecContinuousRatedAcCurrentAttr {
        <<abstract>>
        +currentContinuous
    }
    class ElecMaxContinuousRatedAcCurrentAttr {
        +max
    }
    class ElecInputRatedAcCurrentAttr {
        <<abstract>>
        +input
    }
    class ElecMaxInputRatedAcCurrentAttr {
        +max
    }
    class ElecVoltAttr {
        <<abstract>>
        +elec, volt
    }
    class ElecAcVoltAttr {
        <<abstract>>
        +ac
    }
    class ElecRatedAcVoltAttr {
        <<abstract>>
        +rated
    }
    class ElecInputRatedAcVoltAttr {
        <<abstract>>
        +input
    }
    class ElecNominalInputRatedAcVoltAttr {
        <<abstract>>
        +nominal
    }
    class ElecLineToLineNominalInputRatedAcVoltAttr {
        +voltLineToLine
    }
    class ElecLineToNeutralNominalInputRatedAcVoltAttr {
        +voltLineToNeutral
    }
    class ElecMinInputRatedAcVoltAttr {
        <<abstract>>
        +min
    }
    class ElecLineToLineMinInputRatedAcVoltAttr {
        +voltLineToLine
    }
    class ElecMaxInputRatedAcVoltAttr {
        <<abstract>>
        +max
    }
    class ElecLineToLineMaxInputRatedAcVoltAttr {
        +voltLineToLine
    }
    class ManufacturerAttr {
        +manufacturer
    }
    class ModelSeriesAttr {
        +modelSeries
    }
    class ModelNumberAttr {
        +modelNumber
    }
    class SerialNumberAttr {
        +serialNum
    }
    class ManufactureDateAttr {
        +manufactureDate
    }
    class DimensionLengthAttr {
        +length
    }
    class DimensionWidthAttr {
        +width
    }
    class DimensionHeightAttr {
        +height
    }
    class WeightAttr {
        +weight
    }
```
