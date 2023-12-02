class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.powered_on = False
        self.battery_level = 100

    def power_on(self):
        self.powered_on = True
        print(f"{self.brand} {self.model} is now powered on.")

    def power_off(self):
        self.powered_on = False
        print(f"{self.brand} {self.model} is now powered off.")

    def make_call(self, number):
        if self.powered_on:
            print(f"{self.brand} {self.model} is making a call to {number}.")
        else:
            print("Cannot make a call. Phone is powered off.")

    def charge(self, percentage):
        if 0 <= percentage <= 100:
            self.battery_level += percentage
            print(f"{self.brand} {self.model} battery level: {self.battery_level}%")
        else:
            print("Invalid charging percentage. Please provide a value between 0 and 100.")

    def new_feature(self, feature_name):
        print(f"{self.brand} {self.model} has a new feature: {feature_name}")

# Ejemplo de uso
if __name__ == "__main__":
    my_phone = Phone("Samsung", "Galaxy S20")
    
    my_phone.power_on()
    my_phone.make_call("123-456-7890")
    my_phone.charge(30)
    
    # Nuevo método y atributo
    my_phone.new_feature("Facial recognition")  # Agregar un nuevo método
