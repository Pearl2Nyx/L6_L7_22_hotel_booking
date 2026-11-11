def _is_digits(s):
    return isinstance(s, str) and s.isascii() and s.isdigit()


def nights_stayed(days):
    if not isinstance(days, str):
        return None
    parts = days.split('-')
    if len(parts) != 2:
        return None
    check_in, check_out = parts[0].strip(), parts[1].strip()
    if not (_is_digits(check_in) and _is_digits(check_out)):
        return None
    try:
        nights = int(check_out) - int(check_in)
    except ValueError:
        return None
    return nights if nights >= 0 else None

def room_floor(room_code):
    if not isinstance(room_code, str):
        return None
    parts = room_code.split('-')
    if len(parts) != 2:
        return None
    number = parts[1].strip()
    if not _is_digits(number):
        return None
    return int(number[0])


def booking_label(names_csv):
    if not isinstance(names_csv, str):
        return None
    names = [n.strip() for n in names_csv.split(',') if n.strip()]
    if not names:
        return None
    lead = names[0]
    return lead[0].upper() + lead[1:] + " +" + str(len(names) - 1)


def main():
    print("==== Running nights_stayed ====")
    user_input = input("Enter check-in and check-out day (e.g. 12-15): ")
    result = nights_stayed(user_input)
    print("Nights:", result)

    print("\n==== Running room_floor ====")
    user_input = input("Enter a room code (e.g. D-305): ")
    result = room_floor(user_input)
    print("Floor:", result)

    print("\n==== Running booking_label ====")
    user_input = input("Enter guest names as CSV (e.g. ravi, priya): ")
    result = booking_label(user_input)
    print("Booking Label:", result)

if __name__ == "__main__":
    main()
