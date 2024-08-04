class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.current_capacity = capacity
        self.current_memory = memory

    def install(self, software):
        if self.current_capacity < software.capacity_consumption or self.current_memory < software.memory_consumption:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)
        self.current_capacity -= software.capacity_consumption
        self.current_memory -= software.memory_consumption

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)
            self.current_capacity += software.capacity_consumption
            self.current_memory += software.memory_consumption
