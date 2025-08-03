from typing import List
from collections import defaultdict
import bisect


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_dict = defaultdict(list)
        result = set()
        for [employee, access_time] in access_times:
            if employee in result:
                continue

            employee_times = access_dict[employee]
            time_to_insert = self.convert_to_epoch(access_time)
            index_to_insert = bisect.bisect_left(employee_times, time_to_insert)
            bisect.insort_left(employee_times, time_to_insert)

            # There are three cases where we can have three access.
            # 1. New one is in middle
            # 2. New one is at start of three access.
            # 3. New one is at the end of three access.
            if index_to_insert - 1 >= 0 and index_to_insert + 1 < len(employee_times):
                left = employee_times[index_to_insert - 1]
                right = employee_times[index_to_insert + 1]
                if right - left < 60:
                    result.add(employee)
                    continue

            if index_to_insert - 2 >= 0:
                left = employee_times[index_to_insert - 2]
                right = time_to_insert
                if right - left < 60:
                    result.add(employee)
                    continue

            if index_to_insert + 2 < len(employee_times):
                left = time_to_insert
                right = employee_times[index_to_insert + 2]
                if right - left < 60:
                    result.add(employee)
                    continue

        return list(result)

    def convert_to_epoch(self, time):
        hour, minute = time[:2], time[2:]
        return int(hour) * 60 + int(minute)


s = Solution()
access_times = [["cd", "1025"], ["ab", "1025"], ["cd", "1046"], ["cd", "1055"], ["ab", "1124"], ["ab", "1120"]]
res = s.findHighAccessEmployees(access_times)
print(res)
