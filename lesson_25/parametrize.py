import pytest

def process_transaction(amount, customer_type):
    """Проста бізнес-логіка: комісія залежить від типу клієнта"""
    if customer_type == "vip":
        fee = 0.01   # 1%
    elif customer_type == "regular":
        fee = 0.02   # 2%
    else:
        fee = 0.05   # 5% для нових
    return amount - amount * fee

@pytest.mark.parametrize("amount, customer_type, expected", [
    (1000, "vip", 990),        # VIP клієнт → мінімальна комісія
    (1000, "regular", 980),    # Regular клієнт → стандартна комісія
    (1000, "new", 950),        # Новий клієнт → максимальна комісія
    (0, "vip", 0),             # Edge case: нульова транзакція
    (10**6, "regular", 980000) # Велика транзакція
])
def test_process_transaction(amount, customer_type, expected):
    assert process_transaction(amount, customer_type) == expected