from typing import List
from collections import defaultdict, deque


class Solution:
    def watchedVideosByFriends(
        self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int
    ) -> List[str]:
        video_count = defaultdict(lambda: 0)
        visited = set()
        curr_level = 0
        queue = deque()
        queue.append(id)
        queue.append(-1)
        while len(queue):
            curr_item = queue.popleft()
            print(f"{curr_item} level {curr_level}")
            if curr_item == -1:
                queue.append(-1)
                curr_level += 1
                if curr_level > level:
                    break
                continue

            if curr_item in visited:
                continue
            visited.add(curr_item)

            if curr_level == level:
                for video in watchedVideos[curr_item]:
                    video_count[video] += 1
            for friend in friends[curr_item]:
                queue.append(friend)

        result = [key for key, value in sorted(video_count.items(), key=lambda x: (x[1], x[0]))]
        return result


watchedVideos = [["A", "B"], ["C"], ["B", "C"], ["D"]]
friends = [[1, 2], [0, 3], [0, 3], [1, 2]]
id = 0
level = 1

s = Solution()
res = s.watchedVideosByFriends(watchedVideos, friends, id, level)
print(res)
