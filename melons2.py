"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Default melon order """


    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False


    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08
    #order_type and tax are the class attributes

class InternationalMelonOrder(AbstractMelonOrder):
    #InternationalMelonOrder subclasses AbstractMelonOrder
    """An international (non-US) melon order."""
    

    def __init__(self, species, qty, country_code):
        #Defined the initialization method with attributes species, qty, country_code
        super(InternationalMelonOrder, self).__init__(species, qty)
        #Calling the initialization method of the super
        self.country_code = country_code
        #country_code is the instance attribute
    
    order_type = "international"
    tax = 0.17
    #order_type and tax are the class attributes

    def get_country_code(self):
        """Return the country code."""
        
        return self.country_code
