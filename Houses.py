import json
import numpy as np

class Housing():
    def __init__(self) -> None:
        self.selected_numbers = ()
        self.flag = 0
    
    def read_random_houses(self): # Read Houses Data
        if self.flag == 4:
            self.flag = 0
            self.selected_numbers = ()
        else:
            self.flag += 1

        with open("HargaRumahJabodetabek.json", "r") as file:
            houses = json.load(file)
            if not isinstance(houses, list):
                raise ValueError("Expected a list of houses in the JSON file.")
            
            random_number = str(np.random.randint(1, 3554))
            while random_number in self.selected_numbers:
                random_number = str(np.random.randint(1, 3554))

            self.selected_numbers += (random_number,)
            matching_houses = [house for house in houses if random_number == house['id']]

            for house in matching_houses:
                img_source = house['img_source']
                title = house['title']
                price = house['price_in_rp']
                unique_id = house['id']
                # Do something with the img_source, title, and price
                return img_source, title, price, unique_id
            
    def get_houses(self, unique_id):
        with open("HargaRumahJabodetabek.json", "r") as file:
            houses = json.load(file)
            if not isinstance(houses, list):
                raise ValueError("Expected a list of houses in the JSON file.")
            
            matching_houses = [house for house in houses if unique_id == house['id']]
            if len(matching_houses) == 0:
                raise ValueError("No house found with the given unique ID.")
            
            house = matching_houses[0]
            img_source = house['img_source']
            title = house['title']
            price = house['price_in_rp']
            address = house['address']
            landsize = house['land_size_m2']
            building_size = house['building_size_m2']
            certificate = house['certificate']
            electricity = house['electricity']
            # property_condition = house['property_condition']
            floors = house['floors']
            garages = house['garages']
            bedrooms = house['bedrooms']
            bathrooms = house['bathrooms']
            facilities = house['facilities']
            
            return price, title, address, img_source, landsize, building_size, certificate, electricity, floors, garages, bedrooms, bathrooms, facilities
        