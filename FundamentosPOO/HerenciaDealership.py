class Vehicle:
    def __init__(sefl, brand, model, price):
        sefl.brand = brand
        sefl.model = model
        sefl.price = price
        sefl.is_available = True

    def sell(sefl):
        if sefl.is_available:
            sefl.is_available = False
            print(f'El vehiculo {sefl.brand}. Ha sideo vendido')
        else:
            print(f'El vehiculo {sefl.brand}. No esta disponible')

    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la sub clase')
    
    def stop_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la sub clase')

#creando las clases que ereadan de la super clase 

class Car(Vehicle):
        def start_engine(self):
            if not self.is_available:
                return f'El motor del coche {self.brand} Esta en marcha'
            else:
                return f'El coche {self.brand} no esta disponible'
            
        def stop_engine(sefl):
            if sefl.is_vailable:
                return f'El motor de coche {sefl.brand} se a dtenido'
            else:
                return f'El coche {sefl.brand} no esta disponible'
            
class Bike(Vehicle):
    def start_engine(self):
            if not self.is_available:
                return f'La bicicleta{self.brand} Esta en marcha'
            else:
                return f'La bicicleta {self.brand} no esta disponible'
            
    def stop_engine(sefl):
            if sefl.is_vailable:
                return f'La bicicleta {sefl.brand} se a dtenido'
            else:
                return f'La bicicleta {sefl.brand} no esta disponible'
            
class Truck(Vehicle):
    def start_engine(self):
            if not self.is_available:
                return f'El motor del camion {self.brand} Esta en marcha'
            else:
                return f'El motor del camion {self.brand} no esta disponible'
            
    def stop_engine(sefl):
            if sefl.is_vailable:
                return f'El motor del camion {sefl.brand} se a dtenido'
            else:
                return f'El motor del camion {sefl.brand} no esta disponible' 

#Creando una nueva clase 
class Customer:
    def __init__(self, name) -> None:
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell
            self.purchased_vehicles.append(vehicle)
        else:
             print(f'Lo ciento, {vehicle.brand} no esta disponible') 

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = 'Disponible'
        else:
            availablity  = 'No Disponible'
        print(f'El {vehicle.brand} está {availablity} y cuesta {vehicle.get_price()}') 

class Dealership:
    def __init__(self) -> None:
        self.inventory = []
        self.customers = []
    
    def add_vehicles(self, vehicle: Vehicle):
         self.inventory.append(vehicle)
         print(f'El {vehicle.brand} ha sido añadido al inventario')

    def register_customers(self, customer: Customer):
         self.customers.append(customer)
         print(f'El cliente {customer.name} ha sido añadido')

    def show_available_customers(self):
        print('Vehiculo disponible en la tiendo')
        for vehicle in self.inventory:
             if vehicle.check_available():
                  print(f'-{vehicle.brand} por {vehicle.get_price()}')

car1 = Car('Toyota', 'Corola', 20000)
car1 = Car('Toyota', 'Corolla', 20000)
car2 = Car('Honda', 'Civic', 22000)
car3 = Car('Ford', 'Mustang', 30000)
car4 = Car('BMW', '3 Series', 35000)
car5 = Car('Mercedes', 'C-Class', 40000)

bike1 = Bike('Yamaha', 'MT-07', 7000)
bike2 = Bike('Ducati', 'Monster 821', 12000)
bike3 = Bike('Kawasaki', 'Ninja 400', 5000)
bike4 = Bike('Harley-Davidson', 'Iron 883', 9000)
bike5 = Bike('KTM', 'Duke 390', 6000)

truck1 = Truck('volvo', 'FH16', 800000)
truck2 = Truck('Freightliner', 'Cascadia', 150000)
truck3 = Truck('Kenworth', 'T680', 160000)
truck4 = Truck('Peterbilt', '579', 170000)
truck5 = Truck('Mack', 'Anthem', 180000)

Customer1 = Customer('Nicolas')
Customer2 = Customer('Emanuel')
Customer3 = Customer('Alejandro')
Customer4 = Customer('kevin')
Customer5 = Customer('Sebastian')
Customer6 = Customer('Martin')
Customer7 = Customer('Freddy')

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(car2)
dealership.add_vehicles(car3)
dealership.add_vehicles(car4)
dealership.add_vehicles(car5)
dealership.add_vehicles(bike1)
dealership.add_vehicles(bike2)
dealership.add_vehicles(bike3)
dealership.add_vehicles(bike4)
dealership.add_vehicles(bike5)
dealership.add_vehicles(truck1)
dealership.add_vehicles(truck2)
dealership.add_vehicles(truck3)
dealership.add_vehicles(truck4)
dealership.add_vehicles(truck5)

#Mostra vehiculos disponibles 
dealership.show_available_customers()

#Cliente cosulta vehiculo
Customer1.inquire_vehicle(car2)
Customer2.inquire_vehicle(car3)
Customer3.inquire_vehicle(car4)
Customer4.inquire_vehicle(bike2)
Customer5.inquire_vehicle(bike3)
Customer6.inquire_vehicle(bike5)
Customer7.inquire_vehicle(truck3)
print('#'*100)
Customer7.buy_vehicle(car1)

dealership.show_available_customers()