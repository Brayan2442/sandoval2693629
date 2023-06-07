class vehicle:
    pass
class LandVehicle(vehicle):
    pass
class TrainVehicle(vehicle):
    pass
for clas1 in [vehicle, LandVehicle, TrainVehicle]:
    for clas2 in [vehicle, LandVehicle, TrainVehicle]:
        print(issubclass(clas1, clas2), end="\t")
        print()
        