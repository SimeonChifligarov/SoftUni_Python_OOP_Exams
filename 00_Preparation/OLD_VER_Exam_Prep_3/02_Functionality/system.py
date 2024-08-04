from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        current_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(current_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        current_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(current_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        current_hardware = [h for h in System._hardware if h.name == hardware_name]
        if not current_hardware:
            return "Hardware does not exist"
        current_hardware = current_hardware[0]
        current_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            current_hardware.install(current_software)
            System._software.append(current_software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        current_hardware = [h for h in System._hardware if h.name == hardware_name]
        if not current_hardware:
            return "Hardware does not exist"
        current_hardware = current_hardware[0]
        current_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            current_hardware.install(current_software)
            System._software.append(current_software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        current_hardware = [h for h in System._hardware if h.name == hardware_name]
        current_software = [s for s in System._software if s.name == software_name]
        if not current_hardware or not current_software:
            return "Some of the components do not exist"

        current_hardware = current_hardware[0]
        current_software = current_software[0]
        current_hardware.uninstall(current_software)
        System._software.remove(current_software)

    @staticmethod
    def analyze():
        analyze_info = ["System Analysis", f"Hardware Components: {len(System._hardware)}",
                        f"Software Components: {len(System._software)}"]

        total_used_memory = 0
        total_memory = 0
        total_used_capacity = 0
        total_capacity = 0
        for h in System._hardware:
            # total_used_memory += h.memory - h.current_memory
            total_memory += h.memory
            # total_used_capacity += h.capacity - h.current_capacity
            total_capacity += h.capacity

        for s in System._software:
            total_used_memory += s.memory_consumption
            total_used_capacity += s.capacity_consumption

        analyze_info.append(f"Total Operational Memory: {total_used_memory} / {total_memory}")
        analyze_info.append(f"Total Capacity Taken: {total_used_capacity} / {total_capacity}")

        return "\n".join(analyze_info)

    @staticmethod
    def system_split():
        system_split_info = []

        for h in System._hardware:
            system_split_info.append(f"Hardware Component - {h.name}")

            es_s = 0
            ls_s = 0
            total_used_memory = 0
            total_used_capacity = 0

            for s in h.software_components:
                if type(s).__name__ == "ExpressSoftware":
                    es_s += 1
                elif type(s).__name__ == "LightSoftware":
                    ls_s += 1
                total_used_memory += s.memory_consumption
                total_used_capacity += s.capacity_consumption

            system_split_info.append(f"Express Software Components: {es_s}")
            system_split_info.append(f"Light Software Components: {ls_s}")
            system_split_info.append(f"Memory Usage: {total_used_memory} / {h.memory}")
            system_split_info.append(f"Capacity Usage: {total_used_capacity} / {h.capacity}")
            system_split_info.append(f"Type: {h.type}")

            software_components = [s.name for s in h.software_components]
            if software_components:
                system_split_info.append(f"Software Components: {', '.join(software_components)}")
            else:
                system_split_info.append("Software Components: None")

        return "\n".join(system_split_info)
