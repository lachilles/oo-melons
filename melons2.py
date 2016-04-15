"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Default melon order """


    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False
        self.flat_rate = 0
        self.passed_inspection = False

    def get_total(self):
        """Calculate price."""

        if self.species == "Christmas":
            base_price = (5 * 1.5)
        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price
        
        if self.order_type == "international" and self.qty < 10:
            total += 3
        
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

class GovernmentMelonOrder(AbstractMelonOrder):
    
    def __init__(self, species, qty, passed_inspection):

        super(GovernmentMelonOrder, self).__init__(species, qty)
        
        self.passed_inspection = passed_inspection

    order_type = "government"
    tax = 0


    def mark_inspections(self, passed):

        self.passed_inspection = True






