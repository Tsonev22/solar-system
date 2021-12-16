import numpy as np
from Particle import Particle
import matplotlib as mpl
import matplotlib.pyplot as plt
import copy

sunMass = 1.98847e30    
sunRadius = 6.957 * 1e8  
Sun = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass=sunMass
)



mercuryPosition = sunRadius + (66.724 * 1e6)
mercuryVelocity = np.sqrt(Sun.G * Sun.mass / mercuryPosition)  # from centrifugal force = gravitational force
Mercury = Particle(
    position=np.array([mercuryPosition, 0, 0]),
    velocity=np.array([0, mercuryVelocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Mercury",
    mass=3.285 * 1e23
)

time = 0
D_t = 6
Data = []

for i in range(200000):
    Mercury.updateGravitanionalAcceleration(Sun)
    Sun.updateGravitanionalAcceleration(Mercury)
    Mercury.update(D_t)
    Sun.update(D_t)
    time += D_t

    if i%100 == 0:
        sub_list = [time, copy.deepcopy(Sun), copy.deepcopy(Mercury)]
        Data.append(sub_list)

venusPosition = sunRadius + (107.87 * 1e6)
venusVelocity = np.sqrt(Sun.G * Sun.mass / venusPosition)  # from centrifugal force = gravitational force
Venus = Particle(
    position=np.array([venusPosition, 0, 0]),
    velocity=np.array([0, venusVelocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Venus",
    mass=4.867 * 1e24
)

time = 0
D_t = 6
Data = []

for i in range(200000):
    Venus.updateGravitanionalAcceleration(Sun)
    Sun.updateGravitanionalAcceleration(Venus)
    Venus.update(D_t)
    Sun.update(D_t)
    time += D_t

    if i%100 == 0:
        sub_list = [time, copy.deepcopy(Sun), copy.deepcopy(Venus)]
        Data.append(sub_list)

earthPosition = sunRadius + (147.24 * 1e6)
earthVelocity = np.sqrt(Sun.G * Sun.mass / earthPosition)  # from centrifugal force = gravitational force
Earth = Particle(
    position=np.array([earthPosition, 0, 0]),
    velocity=np.array([0, earthVelocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=5.9722 * 1e24
)

time = 0
D_t = 6
Data = []

for i in range(200000):
    Earth.updateGravitanionalAcceleration(Sun)
    Sun.updateGravitanionalAcceleration(Earth)
    Earth.update(D_t)
    Sun.update(D_t)
    time += D_t

    if i%100 == 0:
        sub_list = [time, copy.deepcopy(Sun), copy.deepcopy(Earth)]
        Data.append(sub_list)

marsPosition = sunRadius + (234.38 * 1e6)
marsVelocity = np.sqrt(Sun.G * Sun.mass / marsPosition)  # from centrifugal force = gravitational force
Mars = Particle(
    position=np.array([marsPosition, 0, 0]),
    velocity=np.array([0, marsVelocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Mars",
    mass=6.39 * 1e23
)

time = 0
D_t = 6
Data = []

for i in range(200000):
    Mars.updateGravitanionalAcceleration(Sun)
    Sun.updateGravitanionalAcceleration(Mars)
    Mars.update(D_t)
    Sun.update(D_t)
    time += D_t

    if i%100 == 0:
        sub_list = [time, copy.deepcopy(Sun), copy.deepcopy(Mars)]
        Data.append(sub_list)


objectss = [Sun, Mercury, Venus, Earth, Mars]


np.save("TwoBodyTest", Data, allow_pickle=True)

print("The Earth and Satellites Location after {0} seconds is:".format((2000*6)))
for particle in [Sun, Mercury, Venus, Earth, Mars]:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!

for obj in objectss:
    plt.plot(obj.position[0], obj.position[1], marker="o")

plt.show()




