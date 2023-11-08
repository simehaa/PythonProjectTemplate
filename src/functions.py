from datetime import datetime


def get_todays_date():
    return datetime.now().date()


if __name__ == "__main__":
    print(f"Today's date is {get_todays_date()}")
