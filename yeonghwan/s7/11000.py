import sys
input = sys.stdin.readline

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures.sort()

# linked_lecture = []
# linked_lecture.append(lectures[0][1])

# for idx in range(1, len(lectures)):
#     if lectures[idx][0] < linked_lecture[0]:
#         # end time
#         linked_lecture.append(lectures[idx][1])
#     else:
#         linked_lecture.pop()
#         linked_lecture.append(lectures[idx][1])

#     linked_lecture.sort(reverse=True)

# print(len(linked_lecture))

lecture_info = []
for lecture in lectures:
    lecture_info.append((lecture[0], 1))
    lecture_info.append((lecture[1], -1))

lecture_info.sort()

result = 0
room = 0

for _, point in lecture_info:
    room += point
    # if room > result:
    #     result = room
    result = max(result, room)

print(result)


