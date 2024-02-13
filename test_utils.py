
def decorate_test(f):
    def wrapper(*args, **kwargs):
        try:
            print(f'\nTest Start: {f.__name__}')
            return_value = f(*args, **kwargs)

            return return_value
        except Exception as e:
            print(f'\nTest {f.__name__} Failed, Exception: {e}\n')
            raise
        finally:
            print(f'\nTest End: {f.__name__}')
    return wrapper
