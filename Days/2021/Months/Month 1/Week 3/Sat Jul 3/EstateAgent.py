#! python3
# Start
# This programm designed to help the estate agent to work with their houses and aparte 
# ments in the way to ake the things faster and more Efficient###

# Propretys the parrent of the Houses and the apartement
class Property:
    """The parrent class of the Houses and the apartement
    designed to manage the both basic infos"""

    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        "Initializing the base infos of the houses and apartements"
        super().__init__(**kwargs)
        self.square_feet =square_feet
        self.beds = beds
        self.baths = baths

    def display(self):
        print('PEROPERTY DETAILS!')
        print('=================')
        print(f'Square Footage : {self.square_feet}')
        print(f'Bedrooms : {self.beds}')
        print(f'Bathrooms : {self.baths}')

    def prompt_init():
        return dict(
            square_feet=input('Enter the Square Feet: '),
            beds=input('Enter the Number of Bedrooms: '),
            baths=input('Enter the number of Baths: ')
        )
    prompt_init = staticmethod(prompt_init)


# A fucniton for checking the validate of the future inputs
def get_valid_input(input_string, valid_options):
    """A Checker funcion to check the validate of the comming inputs
    with the given list than we gave to it as the secend argumant"""
    
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    
    while response.lower() not in valid_options:
        response = input(input_string)
    
    return response

class Apartment(Property):
    """First Part of the estate that shows all the s
    that the estate has/had
    
    take The special argumant about the apartement that a house can not
    have.
    
    Designed to have the abiility to work with the GUI and web applications"""

    valid_balcony = ("yes", "no", "solarium")
    valid_laundry = ("coin", "ensuite", "none")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print('APARTMENT DETAILS')
        print(f'Laundry : {self.laundry}')
        print(f'Balcony : {self.balcony}')
    
    def prompt_init():
        parent_init = Property.prompt_init()
        
        laundry = get_valid_input(
            "What laundy facilities does the apartment have? ",
            Apartment.valid_laundry
            )
        
        balcony = get_valid_input(
            'Does the property has a balcony? ',
            Apartment.valid_balcony
        )

        parent_init.update({
            'balcony' : balcony,
            'laundry' : laundry
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)
        

class House(Property):
    """The secend part of the estate. it will describe the houses of
    the estate and show them
    
    take The special argumant about the house that a apartement can not
    have.
    
    Designed to have the abiility to work with the GUI and web applications"""

    valid_garage = ("attached", "Detached", "none")
    valid_fanced = ('yes', 'no')
    def __init__(self, num_stories='', garage='', fanced='', **kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fanced = fanced

    def display(self):
        "Will show the options the house has"

        super().display()
        print("HOUSE DETAILS")
        print(f'Number of stories : {self.num_stories}')
        print(f'Garage : {self.garage}')
        print(f'Fanced yard : {self.fanced}')

    def prompt_init():
        """Will make it available for working with GUI and 
        web application"""
        parent_init = Property.prompt_init()
        
        num_stories = input('How many Stories? ')
        
        fanced = get_valid_input(
            'Is the yard fanced? ',
            House.valid_fanced
        )
        
        garage = get_valid_input(
            'Is there any garage? ',
            House.valid_garage
        )
        parent_init.update({
            'garage' : garage,
            'fanced' : fanced,
            'num_stories' : num_stories
        })
        
        return parent_init
    prompt_init = staticmethod(prompt_init)

class Purchase:
    """Will declare the price and the tax for the 
    property that gonna discussed about
    
    Take 2 Argumants for the property and has the abillity
    to show them
    
    Able to work with GUI and web applications"""

    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price 
        self.taxes = taxes
    
    def display(self):
        "Show the Price and tax of the property"
        super().display()
        print("PURCHES DETAILS")
        print(f"Selling price : {self.price}")
        print(f'Estimated Tax: {self.taxes}')
    
    def prompt_init():
        "Giving the abillity to work with the GUI and web applications"
        
        return dict(
            price=input('What is the selling price? '),
            taxes=input('What are the estimated taxes? ')
        )
    prompt_init = staticmethod(prompt_init)

class Rental:
    """Will declare the being furnished or not, the utilities 
    of the property and the rent price
    
    Take 3 Argumants for the property and has the abillity
    to show them
    
    Able to work with GUI and web applications"""

    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent
    
    def display(self):
        "Show the Price and tax of the property"

        print('RENTAL DETAILS')
        print(f'Rent : {self.rent}')
        print(f'Furnished : {self.furnished}')
        print(f'Estimated utililties : {self.utilities}')

    def prompt_init():
        return dict(
            utilities=input('What are the estimated utilities? '),
            rent=input('What is the rent price? '),
            furnished=input('Is the property furnished? ')
        )
    prompt_init = staticmethod(prompt_init)


class HouseRental(House, Rental):
    "Will work for renting the houses"

    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentRental(Rental, Apartment):
    "Will work for renting the apartments"

    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase, House):
    "Will work for Purching the houses"

    def prompt_init():
        init = House.prompt_init()
        init.update(Apartment.prompt_init)
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Purchase, Apartment):
    "Will work for Purching The Apartments"

    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init)
        return init
    prompt_init = staticmethod(prompt_init)

class Agent:
    """Work as the superviser and control the wholl
    propertys
    
    has the abillity to add a property and displayint it"""

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()
    
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        """Will add propertys with the asked inputs!
        
        Ask 2 inputs to check what the user wants"""

        property_type = get_valid_input(
            'What type of property? ',
            ('house', 'apartment')
        ).lower()

        payment_type = get_valid_input(
            'What type of payment? ',
            ('rental', 'purchase')
        ).lower()

        property_class = self.type_map[property_type, payment_type]
        init_args = property_class.prompt_init()
        self.property_list.append(property_class(**init_args))
# End