import sys
import pytest
from . import is_leap_year

sys.path.append(".")


class TestYear:
    def test_some_exception(self):
        with pytest.raises(ValueError) as ex:
            is_leap_year.is_leap_year(-1)
