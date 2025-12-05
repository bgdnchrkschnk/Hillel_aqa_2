import sys

import pytest

@pytest.mark.math_module
@pytest.mark.regression
class TestExampleSuite:

    @pytest.mark.smoke
    def test_sum(self):
        result = sum([1, 2, 3])
        print("Checking a sum...")
        assert result == 6

    @pytest.mark.xfail
    def test_substract(self):
        result = 5 - 4
        print("Checking a substract result...")
        # assert result # bool(result) 0 - False, other - True
        # assert result == 0, "Incorrect result" # Assertion Error

        if result != 0:
            pytest.fail(reason="Incorrect result")

def get_oc() -> bool:
    """
    win - win32
    macos - darwin
    linux - linux
    """
    return sys.platform == "darwin"


@pytest.mark.skipif(condition=get_oc(), reason="MacOS not supported")
def test_tran_creating():
    # creating transactions
    transactions: list[dict] = [
        {"id": 2356, "status": "completed", "amount": 100},
        {"id": 2357, "status": "pending", "amount": 200},
        {"id": 2358, "status": "failed", "amount": 700},
    ]
    for transaction in transactions:
        assert transaction["status"] != "failed", f"Transaction id={transaction['id']} failed"

        # if transaction['status'] == "failed":
        #     pytest.fail(reason="Transaction failed")

