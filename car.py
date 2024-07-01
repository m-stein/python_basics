class Car:
    def __init__(self, vendor, brand):
        self.vendor = vendor
        self.brand = brand

    def print_label(self):
        print(f"VENDOR: {self.vendor}, BRAND: {self.brand}")


class CarWithOdometer(Car):
    def __init__(self, vendor, brand):
        super().__init__(vendor, brand)
        self.odometer_reading = 0

    def raise_odometer(self, by):
        self.odometer_reading += by
