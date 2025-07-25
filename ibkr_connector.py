
# Stub: à connecter avec ib_insync pour envoyer les ordres à IBKR
def send_market_order(side, price):
    print(f"[IBKR] Ordre marché {side} à {price}")

def send_limit_order(side, price):
    print(f"[IBKR] Ordre limite {side} à {price}")

def send_trailing_stop(side, price, offset):
    print(f"[IBKR] Ordre trailing {side} à {price} (offset: {offset})")
