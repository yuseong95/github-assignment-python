def fibonacci(position):
    if position < 0:
        return None
    elif position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)
