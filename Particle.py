import numpy as np

class Particle:
    def __init__(self,\
        position=np.array([0, 0, 0], dtype=float),\
        velocity=np.array([0, 0, 0], dtype=float),\
        acceleration=np.array([0, -10, 0], dtype=float),\
        name="Ball",\
        mass=1.0,\
        G = 6.67408e-11):

        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass
        self.G = G
        

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(\
        self.name, self.mass,self.position, self.velocity, self.acceleration
    )

    def update(self, deltaT):
        self.position = self.position + self.velocity * deltaT
        self.velocity = self.velocity + self.acceleration * deltaT

    def updateGravitanionalAcceleration(self, body):
        r = body.position - self.position
        mod_r = (np.dot(r, r))**(1/2)
        unit_r = r/mod_r
        self.acceleration = (self.G * body.mass)/(mod_r**2)*unit_r

    def kineticEnergy(self):
        vel = self.velocity
        mod_vel = (np.dot(vel, vel))**(1/2)       
        return 1/2*self.mass*(mod_vel**2)
