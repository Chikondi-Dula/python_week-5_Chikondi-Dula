# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def device_info(self):
        return f"{self.brand} {self.model}, priced at ${self.price}"

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

# Subclass: GamingPhone (inherits from Smartphone)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, price, gpu, cooling_system):
        super().__init__(brand, model, price)  # Inherit from Smartphone
        self.gpu = gpu
        self.cooling_system = cooling_system

    # Polymorphism: Override device_info method
    def device_info(self):
        return f"{self.brand} {self.model} (Gaming Phone) with {self.gpu} GPU and {self.cooling_system} cooling, priced at ${self.price}"

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model}...")

# Encapsulation example: private attribute
class PhoneWithBattery(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.__battery_life = battery_life  # private attribute

    def battery_status(self):
        print(f"{self.brand} {self.model} has {self.__battery_life}% battery remaining.")

    # Setter to safely update battery life
    def charge_battery(self, amount):
        self.__battery_life = min(100, self.__battery_life + amount)
        print(f"Battery charged. Current battery: {self.__battery_life}%")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S23", 999)
gaming_phone = GamingPhone("Asus", "ROG Phone 6", 1299, "Adreno 730", "Liquid Cooling")
battery_phone = PhoneWithBattery("Apple", "iPhone 14", 1099, 50)

# Using methods
print(phone1.device_info())
phone1.make_call("123-456-7890")

print(gaming_phone.device_info())
gaming_phone.play_game("PUBG Mobile")

battery_phone.battery_status()
battery_phone.charge_battery(30)
battery_phone.battery_status()
