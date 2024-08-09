#####vehicles, car, BMW

class vehicles:
    def vehicles_info(self):
        print("""Vehicles are the one of the modes of transportation.
In vehicles, there are many types based on wheels i.e, two wheeler, four wheeler, heavy vehicles and etc..
Now let us know about the car.""")

class cars(vehicles):
    def car_info(self):
        print("""\n1) Car is a type of vehicle which has four wheels. 
2) Every car will be having a same characteristics which will be like
- braking system
- accelerator
- gearing system
- headlights
- stearing
- roofing
3) But the attributes of the car depends on the model of the car.
4) Amongst many cars I like BMW very much, now let me brief about BMW.""")

class BMW(cars):
    def bmw_info(self):
        print("""\nBMW is a Luxuary sport car.

Certainly! Here’s a brief overview of BMW cars:

- History: Founded in 1916, BMW (Bayerische Motoren Werke) originally manufactured aircraft engines before shifting to automobiles.
- Brand Identity: Known for its "Ultimate Driving Machine" slogan, emphasizing performance, luxury, and driving pleasure.
- Models: Offers a wide range of vehicles including sedans (e.g., 3 Series, 5 Series), SUVs (e.g., X5, X7), and sports cars (e.g., M3, Z4).
- Innovation: Renowned for incorporating advanced technology such as iDrive infotainment systems, adaptive cruise control, and dynamic handling.
- Performance: The M Series models are particularly celebrated for their high performance and sporty driving dynamics.
- Design: Features distinctive design elements like the kidney grille and a driver-focused interior layout.
- Global Presence: BMW is a major player in the luxury car market worldwide, with manufacturing facilities in various countries.

Feel free to ask if you’d like more details on any specific aspect!""")
res = BMW()
res.vehicles_info()
res.car_info()
res.bmw_info()
