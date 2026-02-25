def process_data(a, b) -> float:
    print("Starting process")
    result = 0 # zero is an impossible value for division
    try:
        result = a / b  # Can throw ZeroDivisionError
    except ZeroDivisionError as div0:
        print(f"error {div0}")
        result = None
    finally:
        print("Process complete")
        return result

