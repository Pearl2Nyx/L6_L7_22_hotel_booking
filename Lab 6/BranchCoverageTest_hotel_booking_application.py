import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade

#Example test cases:
def test_standard_two_nights():
    assert booking_cost("standard", 2, 2, False) == 4000

def test_full_refund():
    assert cancellation_refund(1000, 10, False) == 1000

#Write the rest of the test cases so that the code is 90- 100% covered.


# ---------- booking_cost ----------
def test_unknown_room_raises():
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost("penthouse", 1, 1, False)

def test_invalid_nights_raises():
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", 0, 1, False)

def test_peak_season_surcharge():
    # 3500 + 875 = 4375
    assert booking_cost("deluxe", 1, 2, True) == 4375

def test_extra_guests_charge():
    # 2000 + (4-2)*500*1 = 3000
    assert booking_cost("standard", 1, 4, False) == 3000

def test_long_stay_discount():
    # 14000 - 1400 = 12600
    assert booking_cost("standard", 7, 2, False) == 12600

# ---------- cancellation_refund ----------
def test_half_refund():
    assert cancellation_refund(1000, 3, False) == 500

def test_no_refund():
    assert cancellation_refund(1000, 1, False) == 0

def test_half_refund_member_bonus():
    # 500 + 250
    assert cancellation_refund(1000, 3, True) == 750

# ---------- room_upgrade ----------
def test_no_rooms_free():
    assert room_upgrade("standard", True, 0) == "standard"

def test_upgrade_standard_member():
    assert room_upgrade("standard", True, 5) == "deluxe"

def test_upgrade_deluxe_member():
    assert room_upgrade("deluxe", True, 5) == "suite"

def test_suite_stays_suite():
    assert room_upgrade("suite", True, 5) == "suite"


# ---------- branch / boundary tests: booking_cost ----------
def test_negative_nights_raises():
    with pytest.raises(ValueError):
        booking_cost("standard", -1, 1, False)

def test_six_nights_no_discount():
    # boundary: nights == 6 -> no 10% discount
    assert booking_cost("standard", 6, 2, False) == 12000

def test_three_guests_boundary():
    # boundary: guests == 3 -> one extra guest
    assert booking_cost("standard", 1, 3, False) == 2500

def test_one_guest_no_extra_charge():
    assert booking_cost("standard", 1, 1, False) == 2000

def test_suite_peak_season():
    # 6000 + 1500 = 7500
    assert booking_cost("suite", 1, 2, True) == 7500

def test_peak_long_stay_extra_guests_combined():
    # rate 2500, total 17500, +(3-2)*500*7=3500 -> 21000, -10% -> 18900
    assert booking_cost("standard", 7, 3, True) == 18900

# ---------- branch / boundary tests: cancellation_refund ----------
def test_refund_exactly_7_days():
    assert cancellation_refund(1000, 7, False) == 1000

def test_refund_6_days_half():
    assert cancellation_refund(1000, 6, False) == 500

def test_refund_exactly_2_days_half():
    assert cancellation_refund(1000, 2, False) == 500

def test_full_refund_member_no_bonus():
    # >=7 days returns amount immediately, no member bonus
    assert cancellation_refund(1000, 10, True) == 1000

def test_zero_days_member_bonus_only():
    assert cancellation_refund(1000, 0, True) == 250

def test_one_day_non_member_zero():
    assert cancellation_refund(1000, 1, False) == 0

# ---------- branch / boundary tests: room_upgrade ----------
def test_standard_non_member_no_upgrade():
    assert room_upgrade("standard", False, 5) == "standard"

def test_deluxe_non_member_no_upgrade():
    assert room_upgrade("deluxe", False, 5) == "deluxe"

def test_suite_non_member_no_upgrade():
    assert room_upgrade("suite", False, 5) == "suite"

def test_deluxe_member_no_rooms_free():
    assert room_upgrade("deluxe", True, 0) == "deluxe"
