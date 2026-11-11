from hypothesis import given, strategies as st
from hotel_booking import nights_stayed, room_floor, booking_label

junk = st.one_of(st.text(), st.none(), st.integers(), st.binary())

@given(junk)
def test_nights_stayed_no_crash(s):
    try:
        nights_stayed(s)
    except Exception as e:
        assert False, f"nights_stayed crashed with: {e!r}"

@given(junk)
def test_room_floor_no_crash(s):
    try:
        room_floor(s)
    except Exception as e:
        assert False, f"room_floor crashed with: {e!r}"

@given(junk)
def test_booking_label_no_crash(s):
    try:
        booking_label(s)
    except Exception as e:
        assert False, f"booking_label crashed with: {e!r}"


@given(st.text() | st.none())
def test_nights_stayed_never_negative(s):
    result = nights_stayed(s)
    assert result is None or result >= 0


@given(st.integers(0, 10**6), st.integers(0, 10**6))
def test_nights_stayed_valid_range(a, b):
    if a <= b:
        assert nights_stayed(f"{a}-{b}") == b - a
    else:
        assert nights_stayed(f"{a}-{b}") is None


@given(st.sampled_from("ABCDE"), st.integers(100, 999))
def test_room_floor_valid_room(block, number):
    assert room_floor(f"{block}-{number}") == number // 100



@given(st.text() | st.none())
def test_room_floor_in_range(s):
    result = room_floor(s)
    assert result is None or 0 <= result <= 9


@given(st.lists(st.text(alphabet="abcxyzABCXYZ", min_size=1), min_size=1))
def test_booking_label_valid_names(names):
    label = booking_label(", ".join(names))
    expected = names[0][0].upper() + names[0][1:] + " +" + str(len(names) - 1)
    assert label == expected


