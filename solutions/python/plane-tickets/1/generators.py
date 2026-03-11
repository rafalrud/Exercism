"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    seat_letters = ["A", "B", "C", "D"]
    for seat in range(number):
        yield seat_letters[seat % len(seat_letters)]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    seat_letters = ["A", "B", "C", "D"]
    generated = 0
    row = 1   

    while generated < number:
        if row == 13:
            row += 1
            continue

        for letter in seat_letters:
            if generated >= number:
                break
            yield f"{row}{letter}"
            generated += 1

        row += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    passengers_dict = {}
    seat = generate_seats(len(passengers))
    for passenger in passengers:
        passengers_dict[passenger] = next(seat)

    return passengers_dict

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        ticket_lenght = len(seat + flight_id)
        missing_digets = 12 - ticket_lenght
        yield seat + flight_id + "0" * missing_digets
