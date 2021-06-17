# Descending Order
# .join()

def descending_order(num):
    # Bust a move right here    
    return int("".join(e for e in sorted(str(num), reverse=True)))