import unittest
from src.main import BusinessAutomationSystem


class TestBusinessAutomationSystem(unittest.TestCase):

    def setUp(self):
        self.system = BusinessAutomationSystem()

    def test_add_customer(self):
        customer = self.system.add_customer(
            "John Banda",
            "+265991234567"
        )

        self.assertEqual(customer["name"], "John Banda")
        self.assertEqual(customer["phone"], "+265991234567")
        self.assertEqual(len(self.system.customers), 1)

    def test_create_booking(self):
        self.system.add_customer(
            "John Banda",
            "+265991234567"
        )

        booking = self.system.create_booking(
            "John Banda",
            "Business Consultation",
            "2026-10-05"
        )

        self.assertEqual(booking["customer"], "John Banda")
        self.assertEqual(booking["service"], "Business Consultation")
        self.assertEqual(booking["status"], "Pending")
        self.assertEqual(len(self.system.bookings), 1)


if __name__ == "__main__":
    unittest.main()
