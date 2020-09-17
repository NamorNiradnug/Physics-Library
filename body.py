from typing import Optional, List

from physical import Physical, VectorPhysical, EARTH_GRAVITY
import dimension


class PhysicsBody:
    """Simple body with Newton mechanic laws."""

    def __init__(
        self,
        mass: Optional[Physical] = None,
        volume: Optional[Physical] = None,
        initial_speed: VectorPhysical = VectorPhysical(),
        gravity_acceleration: VectorPhysical = EARTH_GRAVITY
    ):
        self.mass = mass
        self.volume = volume
        self.speed = initial_speed
        self.gravity_acceleration = gravity_acceleration
        self.forces: List[VectorPhysical] = []

    def density(self) -> Optional[Physical]:
        if self.mass is None or self.volume is None:
            return None
        return self.mass / self.volume

    def add_force(self, force: VectorPhysical) -> None:
        self.forces.append(force)

    def force_sum(self) -> VectorPhysical:
        forces_sum = sum(force for force in self.forces)
        if self.mass is not None:
            forces_sum += self.mass * self.gravity_acceleration
        return forces_sum
