import pytest


@pytest.mark.smoke
@pytest.mark.regression
class TestStrings:
    test_data = 555

    def test_upper(self):
        s = "lemon"
        assert s.upper() == "LEMON"

    @pytest.mark.skip(reason="Waiting for implementation on dev")
    def test_lower(self):
        s = "BANANA"
        assert s.lower() == "banana"

    def test_lower_2(self):
        test_data: str = None
        with pytest.raises(AttributeError):
            result = test_data.lower()