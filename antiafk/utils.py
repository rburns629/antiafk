from pynput.keyboard import Key


def std_keys() -> list:
    # Return the keys on a standard keyboard using ascii character codes
    try:
        return [chr(i) for i in range(33, 127)]
    except Exception as e:
        raise e

        
def spec_keys() -> dict:
    # Return a dictionary based on whether or not the Key class as the specified attribute
    try:
        return {k: getattr(Key, k) for k in dir(Key)[4:] if getattr(Key, k)}
    except Exception as e:
        raise e


def get_time(span: int, time_type: str) -> int:
    # Calculate and return the integer value of the time specified by the user
    try:
        switch = {
            'second': 1,
            'minute': 60,
            'hour': 3600,
            'day': 86400
        }

        return span * switch[time_type[:-1].lower() if time_type[-1] == 's' else time_type.lower()]
    except Exception as e:
        raise e
