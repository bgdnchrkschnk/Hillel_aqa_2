class LandTransport:

    def __init__(self, land_wheels, land_volume):
        self.wheels = land_wheels
        self.volume = land_volume

    def drive(self):
        print('Driving Land....')

    def horn(self):
        print('Horning like a car...')

class WaterTransport:

    def __init__(self, water_engine, water_volume):
        self.engine = water_engine
        self.volume = water_volume

    def drive(self):
        print('Driving Water...')

    def horn(self):
        print('Horning like a boat...')

class AirTransport:

    def __init__(self, airline, air_volume):
        self.airline = airline
        self.volume = air_volume

    def fly(self):
        print('Flying...')

class AmphibiousTransport(LandTransport, WaterTransport):

    def __init__(self, amphibious_version, land_wheels, land_volume, water_engine, water_volume):
        LandTransport.__init__(self, land_wheels, land_volume)
        WaterTransport.__init__(self, water_engine, water_volume)
        self.amphibious_version = amphibious_version

    def drive(self):
        LandTransport.drive(self)
        WaterTransport.drive(self)

class AirWaterTransport(AirTransport, WaterTransport):

    def __init__(self, water_engine, water_volume, airwater_version, airline, air_volume):
        AirTransport.__init__(self, airline, air_volume)
        WaterTransport.__init__(self, water_engine, water_volume)
        self.airwater_version = airwater_version

class HybridTransport(AmphibiousTransport, AirWaterTransport):

    def __init__(self, amphibious_version, land_wheels, land_volume, water_engine, water_volume, airwater_version, airline, air_volume, hybrid_model):
        super().__init__(amphibious_version=amphibious_version, land_wheels=land_wheels, land_volume=land_volume, water_engine=water_engine, water_volume=water_volume)
        AirWaterTransport.__init__(self, airline=airline, air_volume=air_volume, airwater_version=airwater_version, water_engine=water_engine, water_volume=water_volume)
        self.hybrid_model = hybrid_model

    def __setattr__(self, key, value):
        if key == 'wheels_setattr':
            return object.__setattr__(self, key, value*2)


# amphibious = AmphibiousTransport(amphibious_version=1.0, land_wheels=6, land_volume=10, water_engine=8.0, water_volume=10)
# airwater = AirWaterTransport(airline="Turkish Airlines", air_volume=500, water_engine=8.0, water_volume=10, airwater_version=2.0)
#
# amphibious.drive()
# print("-"*80)
# airwater.fly()
# airwater.drive()
# print(airwater.))

hybrid = HybridTransport(1.0, 6, 10, 8.0, 10, 2.0, "Turkish Airlines", 500, "Tesla 2100")

hybrid.horn()

print(HybridTransport.mro())


print(
    hasattr(hybrid, "wheels") # bool чи є в обʼєкті певний атрибут
)

# print(
#     getattr(hybrid, "wheels") # hybrid.wheels
# )

setattr(hybrid, "wheels_setattr", "test")

print(hybrid.wheels_setattr)
