from schemas.trip import Trip


def test_trip_schema():

    print("\nCreating Trip...")

    trip = Trip(
        purpose="Tourism",
        travel_date="2026-08-01",
        duration_days=14,
        accommodation="Hotel",
        sponsor=None,
    )

    print(trip)

    assert trip.purpose == "Tourism"
    assert trip.duration_days == 14

    print("\nTrip Schema Test Passed.")