from datetime import datetime
​
def check_coupon(entered_code, correct_code, current_date: str, expiration_date: str) -> bool:
    return (
        type(entered_code) is type(correct_code)
        and entered_code == correct_code
        and datetime.strptime(current_date, "%B %d, %Y") <= datetime.strptime(expiration_date, "%B %d, %Y")
    )
​