class Movie:
    ticket_price = 100.0

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def display_info(self):
        print("Movie Title: {}, Duration: {} minutes".format(self.title, self.duration))

    @classmethod
    def update_ticket_price(cls, new_price):
        cls.ticket_price = new_price
        print("Updated ticket price to: Rs {:.2f}".format(cls.ticket_price))

    @staticmethod
    def calculate_total_price(number_of_tickets):
        return number_of_tickets * Movie.ticket_price


movie1 = Movie("Inception", 148)
movie2 = Movie("The Matrix", 136)

movie1.display_info()
movie2.display_info()

print("Initial Ticket Price: Rs {:.2f}".format(Movie.ticket_price))

Movie.update_ticket_price(150.0)

number_of_tickets = 5
total_price = Movie.calculate_total_price(number_of_tickets)
print("Total price for {} tickets: Rs {:.2f}".format(number_of_tickets, total_price))
