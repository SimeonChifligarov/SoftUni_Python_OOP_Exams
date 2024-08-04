from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, hardware_type="Heavy", capacity=2*capacity, memory=int(0.75*memory))
