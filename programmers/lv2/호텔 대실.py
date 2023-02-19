# https://school.programmers.co.kr/learn/courses/30/lessons/155651
import heapq
def convert_minute(start, end):
    start = int(start[:2]) * 60 + int(start[-2:])
    end = int(end[:2]) * 60 + int(end[-2:])
    return (start, end)
def solution(book_time):
    answer = 1
    for idx, item in enumerate(book_time):
        book_time[idx] = convert_minute(item[0], item[1])
    book_time.sort()
    heap = []
    for s, e, in book_time:
        if not heap:
            heapq.heappush(heap, e + 10)
            continue
        if heap[0] <= s:
            heapq.heappop(heap)
        else:
            answer += 1
        heapq.heappush(heap, e+10)
    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))