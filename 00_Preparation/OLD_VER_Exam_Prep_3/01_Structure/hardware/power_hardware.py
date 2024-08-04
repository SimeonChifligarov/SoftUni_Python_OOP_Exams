from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, hardware_type="Power", capacity=int(0.25*capacity), memory=int(1.75*memory))
