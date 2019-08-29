def prompt_helper():
    print("Press 'i' to insert new record")
    print("Press 'd' to delete current record")
    print("Press 'u' to update current record")
    print("Press 'f' to find current record")
    print("Press 'q' to quit\n\n")

    input_val = input("Enter your choice: ").lower()
    return input_val