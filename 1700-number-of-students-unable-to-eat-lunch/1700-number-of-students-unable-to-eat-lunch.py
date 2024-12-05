from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)  # 학생 선호도 카운트
        
        for s in sandwiches:
            if cnt[s] > 0:  # 현재 샌드위치를 원하는 학생이 있는 경우
                res -= 1
                cnt[s] -= 1
            else:  # 원하는 학생이 없는 경우 종료
                return res
        
        return res
