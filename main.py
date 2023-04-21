import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("час уик {}: {} с.".format(func.__name__, end_time - start_time))
        return result
    return wrapper
@calculate_time
def sum_list(lst):
    return sum(lst)

def test_sum_list():
    assert sum_list([1, 2, 3, 4, 5]) == 15

test_sum_list()