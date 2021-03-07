import pytest
from outbreak_location import location_filter


def test_outbreak_location_basecase():
    assert len(location_filter('China')) > 0

