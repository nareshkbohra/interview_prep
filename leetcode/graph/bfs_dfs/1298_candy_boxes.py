from typing import List
from collections import deque


class Solution:
	def maxCandies(
		self,
		status: List[int],
		candies: List[int],
		keys: List[List[int]],
		containedBoxes: List[List[int]],
		initialBoxes: List[int],
	) -> int:
		"""
		1. Maintain a queue of all the boxes which can be opened.
		2. Maintain a list of unopened boxes, keys and opened boxes.
		3. Pop queue and get a box, check if it is not already opened, if yes, continue.
		4. Open and count the candies.
		5. Add all the opened boxed into queue.
		6. For all the keys, if unopened box is present, add that to queue. Add remaining keys to key set.
		7. Do the same for boxes opened.
		8. Keep doing till you have boxes to open.
		"""
		boxes_can_be_opened = deque()
		unopened_boxes = set()
		key_set = set()
		opened_boxes = set()

		for box in initialBoxes:
			if status[box] == 1:
				boxes_can_be_opened.append(box)
			else:
				unopened_boxes.add(box)

		total_candies = 0
		while len(boxes_can_be_opened):
			curr_box = boxes_can_be_opened.popleft()

			if curr_box in opened_boxes:
				continue

			total_candies += candies[curr_box]
			opened_boxes.add(curr_box)
			curr_keys = keys[curr_box]
			for key in curr_keys:
				if key in unopened_boxes:
					boxes_can_be_opened.append(key)
				else:
					key_set.add(key)

			curr_boxes = containedBoxes[curr_box]
			for box in curr_boxes:
				if box in opened_boxes:
					continue
				if box in key_set or status[box] == 1:
					boxes_can_be_opened.append(box)
				else:
					unopened_boxes.add(box)

		return total_candies


status = [1, 0, 1, 0]
candies = [7, 5, 4, 100]
keys = [[], [], [1], []]
containedBoxes = [[1, 2], [3], [], []]
initialBoxes = [0]
s = Solution()
res = s.maxCandies(status, candies, keys, containedBoxes, initialBoxes)
print(res)
