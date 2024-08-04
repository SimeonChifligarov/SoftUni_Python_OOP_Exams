from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hardware('bozz', 'real_deal', 100, 250)
        self.software = Software('soft', 'zoft', 25, 50)

    def test_init(self):
        new_hardware = Hardware('high_level', 'ai_begai', 150, 375)
        self.assertEqual('high_level', new_hardware.name)
        self.assertEqual('ai_begai', new_hardware.type)
        self.assertEqual(150, new_hardware.capacity)
        self.assertEqual(375, new_hardware.memory)
        self.assertEqual([], new_hardware.software_components)

    def test_install_not_enough_capacity_raises(self):
        self.software.capacity_consumption = 300
        with self.assertRaises(Exception) as ex:
            self.hardware.install(self.software)
        self.assertEqual("Software cannot be installed", str(ex.exception))
        self.assertEqual([], self.hardware.software_components)

    def test_install_not_enough_memory_raises(self):
        self.software.memory_consumption = 300
        with self.assertRaises(Exception) as ex:
            self.hardware.install(self.software)
        self.assertEqual("Software cannot be installed", str(ex.exception))
        self.assertEqual([], self.hardware.software_components)

    def test_install_valid(self):
        self.assertEqual([], self.hardware.software_components)
        self.hardware.install(self.software)
        self.assertEqual([self.software], self.hardware.software_components)

    def test_uninstall_valid(self):
        self.hardware.software_components = [self.software]
        self.assertEqual([self.software], self.hardware.software_components)
        self.hardware.uninstall(self.software)
        self.assertEqual([], self.hardware.software_components)


if __name__ == '__main__':
    main()
