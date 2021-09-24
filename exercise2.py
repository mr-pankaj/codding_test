from datetime import datetime
import pytz


class TimeInterval:
    
    start_time = None
    end_time = None
    start_time_utc = None
    end_time_utc = None
    tz = None

    def __init__(self, start_time, end_time, tz) -> None:
        self.tz = pytz.timezone(tz)
        self.start_time = self.__make_time(start_time)
        self.end_time = self.__make_time(end_time)
        self.start_time_utc = self.__make_time(start_time, pytz.utc)
        self.end_time_utc = self.__make_time(end_time, pytz.utc)

    def __make_time(self, time, tz = None):
        time = datetime.strptime(f"{datetime.now().strftime('%Y-%m-%d')} {time}", '%Y-%m-%d %I:%M %p')
        if not tz:
            time = self.tz.localize(time)
        else: 
            time = tz.localize(time)
        return time

class TimeIntersection:

    def get_time_intersection(self, interval_one, interval_two):
        
        intersecting_points = []
        intersection_time = {}

        if (interval_one.start_time_utc >= interval_one.start_time_utc) and (interval_two.start_time_utc <= interval_one.end_time_utc):
            intersecting_points.append('start_time')
        if (interval_two.end_time_utc >= interval_one.start_time_utc) and (interval_two.end_time_utc <= interval_one.end_time_utc):
            intersecting_points.append('end_time')

        # When start is intersecting
        if 'start_time' in intersecting_points and not 'end_time' in intersecting_points:
            intersection_time['start_time_utc'] = interval_two.start_time_utc
            intersection_time['end_time_utc'] = interval_one.end_time_utc

        # When end time is intersecting
        if 'end_time' in intersecting_points and not 'start_time' in intersecting_points:
            intersection_time['start_time_utc'] = interval_one.start_time_utc
            intersection_time['end_time_utc'] = interval_two.end_time_utc

        # When start and end both lies in side the first slot
        if 'start_time' in intersecting_points and 'end_time' in intersecting_points:
            intersection_time['start_time_utc'] = interval_two.start_time_utc
            intersection_time['end_time_utc'] = interval_two.end_time_utc

        # When start and end time of first slot lies inside of the second slot
        if 'start_time' not in intersecting_points and not 'end_time' in intersecting_points:
            if (interval_two.start_time_utc <= interval_one.start_time_utc) and (interval_two.end_time_utc >= interval_one.end_time_utc):
                # print("first slot lies in the second slot")
                intersection_time['start_time_utc'] = interval_one.start_time_utc
                intersection_time['end_time_utc'] = interval_one.end_time_utc
        
        return {
            'intersection_points': intersecting_points,
            'intersection': intersection_time
        }

    def print_single_day_availability(self, points, intersection, interval_one, interval_two):

        if len(points) == 0:
            pass
        
        if intersection:

            date_formate = '%Y-%m-%d %I:%M:%S %p %Z'
            time_formate = '%I:%M:%S %p %Z%z'

            print(intersection['start_time_utc'].strftime(time_formate), '-', intersection['end_time_utc'].strftime(time_formate))

            print(intersection['start_time_utc'].astimezone(interval_one.tz).strftime(time_formate), '-', intersection['end_time_utc'].astimezone(interval_one.tz).strftime(time_formate))
            
            print(intersection['start_time_utc'].astimezone(interval_two.tz).strftime(time_formate), '-', intersection['end_time_utc'].astimezone(interval_two.tz).strftime(time_formate))


    def has_intersection(self, first_slot, second_slot):
        if (second_slot['start_time_utc'] >= first_slot['start_time_utc']) and (second_slot['start_time_utc'] <= first_slot['end_time_utc']):
            return True
        elif (second_slot['end_time_utc'] >= first_slot['start_time_utc']) and (second_slot['end_time_utc'] <= first_slot['end_time_utc']):
            return True
        else:
            return False


time_intersection = TimeIntersection()
# time_interval_one = TimeInterval('10:30 AM', '7:00 PM', 'Asia/Kolkata')
# time_interval_two = TimeInterval('7:30 PM', '7:00 PM', 'Australia/NSW')
# meta = time_intersection.get_time_intersection(time_interval_one, time_interval_two)
# time_intersection.print_single_day_availability(meta['intersection_points'], meta['intersection'], time_interval_one, time_interval_two)

week_intervals_one = [
    TimeInterval('6:30 AM', '3:00 PM', 'Asia/Kolkata'),
    TimeInterval('7:30 AM', '5:00 PM', 'Asia/Kolkata'),
    TimeInterval('2:30 PM', '7:00 PM', 'Asia/Kolkata'),
    TimeInterval('9:30 AM', '8:00 PM', 'Asia/Kolkata'),
    TimeInterval('11:30 AM', '7:00 PM', 'Asia/Kolkata'),
    TimeInterval('10:30 AM', '9:00 PM', 'Asia/Kolkata'),
    TimeInterval('10:45 AM', '6:45 PM', 'Asia/Kolkata'),
]

week_intervals_two = [
    TimeInterval('10:30 AM', '7:00 PM', 'Australia/NSW'),
    TimeInterval('10:30 AM', '7:00 PM', 'Australia/NSW'),
    TimeInterval('10:30 AM', '7:00 PM', 'Australia/NSW'),
    TimeInterval('10:30 AM', '7:00 PM', 'Australia/NSW'),
    TimeInterval('10:30 AM', '7:00 PM', 'Australia/NSW'),
    TimeInterval('10:30 AM', '7:00 PM', 'Australia/NSW'),
    TimeInterval('10:30 AM', '7:00 PM', 'Australia/NSW'),
]


for i in range(1, 7):
    time_interval_one = week_intervals_one[i]
    time_interval_two = week_intervals_two[i]
    meta = time_intersection.get_time_intersection(time_interval_one, time_interval_two)
    time_intersection.print_single_day_availability(meta['intersection_points'], meta['intersection'], time_interval_one, time_interval_two)

class WeekIntersection:

    pass


