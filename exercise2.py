from datetime import datetime
import pytz
import pprint


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
        self.start_time_utc = self.convert_to_timezone(
            self.start_time, pytz.utc)
        self.end_time_utc = self.convert_to_timezone(self.end_time, pytz.utc)

    def convert_to_timezone(self, time, tz):
        return time.astimezone(tz)

    def __make_time(self, time):
        time = datetime.strptime(f"{time}", '%Y-%m-%d %I:%M %p')
        time = self.tz.localize(time)
        return time


class TimeIntersection:

    def get_time_intersection(self, interval_one, interval_two):

        intersecting_points = []
        intersection_time = {}

        if (interval_two.start_time_utc >= interval_one.start_time_utc) and (interval_two.start_time_utc <= interval_one.end_time_utc):
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

        time_formate = '%Y-%m-%d %I:%M:%S %p %Z%z'

        if len(points) == 0:
            print("No intersecting time available between Person 1 and Person2")
            print(interval_one.start_time_utc.strftime(time_formate),
                  '-', interval_one.end_time_utc.strftime(time_formate))
            print(interval_two.start_time_utc.strftime(time_formate),
                  '-', interval_two.end_time_utc.strftime(time_formate))

        if intersection:
            print(intersection['start_time_utc'].strftime(
                time_formate), '-', intersection['end_time_utc'].strftime(time_formate))

            print(intersection['start_time_utc'].astimezone(interval_one.tz).strftime(
                time_formate), '-', intersection['end_time_utc'].astimezone(interval_one.tz).strftime(time_formate))

            print(intersection['start_time_utc'].astimezone(interval_two.tz).strftime(
                time_formate), '-', intersection['end_time_utc'].astimezone(interval_two.tz).strftime(time_formate))

    def has_intersection(self, first_slot, second_slot):
        if (second_slot['start_time_utc'] >= first_slot['start_time_utc']) and (second_slot['start_time_utc'] <= first_slot['end_time_utc']):
            return True
        elif (second_slot['end_time_utc'] >= first_slot['start_time_utc']) and (second_slot['end_time_utc'] <= first_slot['end_time_utc']):
            return True
        else:
            return False


class WeekIntersection:

    def print_week_availability(self, week_intervals_one, week_intervals_two):

        time_intersection = TimeIntersection()

        weekDays = ["Sunday", "Monday", "Tuesday",
                    "Wednesday", "Thursday", "Friday", "Saturday"]

        availability_one = ()
        availability_two = ()
        is_same_tz = False

        for i in range(0, 7):
            time_interval_one = week_intervals_one[i]
            time_interval_two = week_intervals_two[i]

            if time_interval_one.tz == time_interval_two.tz:
                is_same_tz = True

            meta = time_intersection.get_time_intersection(
                time_interval_one, time_interval_two)
            if meta['intersection']:
                availability_one = availability_one + \
                    (weekDays[i] + self._make_time(
                        meta, time_interval_one, time_interval_two), )
                availability_two = availability_two + \
                    (weekDays[i] + self._make_time(
                        meta, time_interval_two, time_interval_one), )

        if (is_same_tz):
            print(", ".join(availability_one))
        else:
            print(", ".join(availability_one))
            print(", ".join(availability_two))

    def _make_time(self, meta, interval_one, interval_two):
        date_formate = '%Y-%m-%d %I:%M:%S %p %Z'
        time_formate = '%I:%M:%S %p %Z%z'
        intersection = meta['intersection']
        return f" {intersection['start_time_utc'].astimezone(interval_one.tz).strftime(time_formate)} - {intersection['end_time_utc'].astimezone(interval_one.tz).strftime(time_formate)}"


time_intersection = TimeIntersection()

time_interval_one = TimeInterval(
    '2021-09-29 10:00 AM', '2021-09-29 07:00 PM', 'Pacific/Auckland')
time_interval_two = TimeInterval(
    '2021-09-29 2:00 PM', '2021-09-29 11:00 PM', 'Asia/Kolkata')

meta = time_intersection.get_time_intersection(
    time_interval_one, time_interval_two)
time_intersection.print_single_day_availability(
    meta['intersection_points'], meta['intersection'], time_interval_one, time_interval_two)


week_intervals_one = [
    TimeInterval('2021-09-29 06:30 AM', '2021-09-29 03:00 PM', 'Hongkong'),
    TimeInterval('2021-09-29 07:30 AM', '2021-09-29 05:00 PM', 'Hongkong'),
    TimeInterval('2021-09-29 02:30 PM', '2021-09-29 07:00 PM', 'Hongkong'),
    TimeInterval('2021-09-29 09:30 AM', '2021-09-29 08:00 PM', 'Hongkong'),
    TimeInterval('2021-09-29 11:30 AM', '2021-09-29 07:00 PM', 'Hongkong'),
    TimeInterval('2021-09-29 10:30 AM', '2021-09-29 09:00 PM', 'Hongkong'),
    TimeInterval('2021-09-29 10:45 AM', '2021-09-29 06:45 PM', 'Hongkong'),
]

week_intervals_two = [
    TimeInterval('2021-09-29 10:30 AM', '2021-09-29 07:00 PM', 'Poland'),
    TimeInterval('2021-09-29 10:30 AM', '2021-09-29 07:00 PM', 'Poland'),
    TimeInterval('2021-09-29 10:30 AM', '2021-09-29 07:00 PM', 'Poland'),
    TimeInterval('2021-09-29 10:30 AM', '2021-09-29 07:00 PM', 'Poland'),
    TimeInterval('2021-09-29 10:30 AM', '2021-09-29 07:00 PM', 'Poland'),
    TimeInterval('2021-09-29 10:30 AM', '2021-09-29 11:00 AM', 'Poland'),
    TimeInterval('2021-09-29 10:30 AM', '2021-09-29 11:00 AM', 'Poland'),
]

# WeekIntersection().print_week_availability(week_intervals_one, week_intervals_two)
