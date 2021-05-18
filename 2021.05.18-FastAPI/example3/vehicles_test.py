from .vehicles import Vehicle


# A (verbose) pytest naming convention:
# test__{class}__{function}__{state}__{result}


def test__vehicle__validate_year__less_than_minimum__throws_error():
    try:
        Vehicle(
            id = 1,
            make = 'Mitsubishi',
            model = 'Montero Sport',
            year = 1200,
        )
    except ValueError:
        assert True
    else:
        assert False


def test__vehicle__validate_make__invalid_make__throws_error():
    try:
        Vehicle(
            id = 1,
            make = 'Ford',
            model = 'F150',
            year = 2020,
        )
    except ValueError:
        assert True
    else:
        assert False
