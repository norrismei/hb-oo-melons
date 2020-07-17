"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from"""

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        add_fee = 0

        # Fees and price adjustments
        if self.species == 'christmas':
            base_price = 1.5 * base_price
        elif self.order_type == 'international':
            if self.qty < 10:
                add_fee = 3


        total = (1 + self.tax) * self.qty * base_price + add_fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, 'domestic', 0.08)
        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, 'international', 0.17)
        self.country_code = country_code
    

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Govt melon order"""
    passed_inspection = False

    def __init__(self, species, qty):
        super().__init__(species, qty, 'government', 0)


    def marked_inspection(self, passed):
        self.passed_inspection = passed

# Sample melons to instantiate
melon1 = DomesticMelonOrder('crenshaw', 10)                            
melon2 = DomesticMelonOrder('christmas', 10)                           
melon3 = InternationalMelonOrder('crenshaw', 5, 'AUS')                 
melon4 = InternationalMelonOrder('yellow watermelon', 10, 'GB')
melon5 = GovernmentMelonOrder('watermelon', 100)   