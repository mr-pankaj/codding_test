from datetime import datetime
import time
import os
import pytz


class TimeInterval:
    start_time = None
    end_time = None
    def __init__(self, start_time, end_time, tz) -> None:
        self.start_time = start_time
        self.end_time = start_time

class TimeIntersection:

    def intersection(self):
        #Temporary date for timezone and time comparision
        tmp_date = '2021-09-24' 
        date_formate = '%Y-%m-%d %I:%M:%S %p %Z%z'
        time_formate = '%I:%M:%S %p %Z%z'
        time_formate = '%I:%M:%S %p'
        canada_tz = pytz.timezone('Canada/Central')
        india_tz = pytz.timezone('Asia/Kolkata')
        london_tz = pytz.timezone('Europe/London')
        pacific_tz = pytz.timezone('US/Pacific')
        

        # second_datetime = datetime.now(pacific_tz)

        # print("UTC Time", datetime.now(pytz.utc).strftime(date_formate))
        # print("Indian Time", datetime.now(india_tz).strftime(date_formate))
        # print("London Time", first_datetime.strftime(date_formate))
        # print("Pacific Time", second_datetime.strftime(date_formate))

        # print(dir(datetime.time))

        first_start_time = datetime.strptime('2021-09-24 2:30 AM', '%Y-%m-%d %I:%M %p') 
        first_start_time = india_tz.localize(first_start_time)

        first_end_time = datetime.strptime('2021-09-25 08:30 AM', '%Y-%m-%d %I:%M %p')  
        first_end_time = india_tz.localize(first_end_time)

        second_start_time = datetime.strptime('2021-09-24 10:30 AM', '%Y-%m-%d %I:%M %p') 
        second_start_time = canada_tz.localize(second_start_time)

        second_end_time = datetime.strptime('2021-09-24 05:30 PM', '%Y-%m-%d %I:%M %p')  
        second_end_time = canada_tz.localize(second_end_time)

        first_start_time_utc = first_start_time.astimezone(pytz.utc)
        first_end_time_utc = first_end_time.astimezone(pytz.utc)

        second_start_time_utc = second_start_time.astimezone(pytz.utc)
        second_end_time_utc = second_end_time.astimezone(pytz.utc)

        print("UTC Time Start", first_start_time_utc)
        print("UTC Time End", first_end_time_utc)

        print('======================')

        # print("Pacific Time", second_start_time)
        print("UTC Time", second_start_time_utc)
        print("UTC Time End", second_end_time_utc)

            
        first_slot = {
            "start_time": first_start_time,
            "start_time_utc": first_start_time_utc,
            "end_time": first_end_time,
            "end_time_utc": first_end_time_utc
        }

        second_slot = {
            "start_time": second_start_time,
            "start_time_utc": second_start_time_utc,
            "end_time": second_end_time,
            "end_time_utc": second_end_time_utc
        }

        intersecting_points = []

        intersection_time = {}

        if (second_slot['start_time_utc'] >= first_slot['start_time_utc']) and (second_slot['start_time_utc'] <= first_slot['end_time_utc']):
            intersecting_points.append('start_time')
        if (second_slot['end_time_utc'] >= first_slot['start_time_utc']) and (second_slot['end_time_utc'] <= first_slot['end_time_utc']):
            intersecting_points.append('end_time')

        # When start is intersecting
        if 'start_time' in intersecting_points and not 'end_time' in intersecting_points:
            intersection_time['start_time_utc'] = second_slot['start_time_utc']
            intersection_time['end_time_utc'] = first_slot['end_time_utc']

        # When end time is intersecting
        if 'end_time' in intersecting_points and not 'start_time' in intersecting_points:
            intersection_time['start_time_utc'] = first_slot['start_time_utc']
            intersection_time['end_time_utc'] = second_slot['end_time_utc']

        # When start and end both lies in side the first slot
        if 'start_time' in intersecting_points and 'end_time' in intersecting_points:
            intersection_time['start_time_utc'] = second_slot['start_time_utc']
            intersection_time['end_time_utc'] = second_slot['end_time_utc']

        # When start and end time of first slot lies inside of the second slot
        if 'start_time' not in intersecting_points and not 'end_time' in intersecting_points:
            if (second_slot['start_time_utc'] <= first_slot['start_time_utc']) and (second_slot['end_time_utc'] >= first_slot['end_time_utc']):
                # print("first slot lies in the second slot")
                intersection_time['start_time_utc'] = first_slot['start_time_utc']
                intersection_time['end_time_utc'] = first_slot['end_time_utc']
        

        if len(intersecting_points) == 0:
            pass

        
        if intersection_time:
            # print(intersecting_points)
            # print(intersection_time)

            print(intersection_time['start_time_utc'].strftime(time_formate), '-', intersection_time['end_time_utc'].strftime(time_formate), ' UTC')

            print(intersection_time['start_time_utc'].astimezone(india_tz).strftime(time_formate), '-', intersection_time['end_time_utc'].astimezone(india_tz).strftime(time_formate), ' Indian Time')
            
            print(intersection_time['start_time_utc'].astimezone(canada_tz).strftime(time_formate), '-', intersection_time['end_time_utc'].astimezone(canada_tz).strftime(time_formate), 'Canada Time')
        


    def has_intersection(self, first_slot, second_slot):
        if (second_slot['start_time_utc'] >= first_slot['start_time_utc']) and (second_slot['start_time_utc'] <= first_slot['end_time_utc']):
            return True
        elif (second_slot['end_time_utc'] >= first_slot['start_time_utc']) and (second_slot['end_time_utc'] <= first_slot['end_time_utc']):
            return True
        else:
            return False


time_intersection = TimeIntersection()
time_intersection.intersection()





