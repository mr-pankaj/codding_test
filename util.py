import datetime

def get_start_time():
    return datetime.datetime.now()
def print_end_time(start_time):
    delta = datetime.datetime.now() - start_time
    print(f"{delta.total_seconds() * 1000} milliseconds")
