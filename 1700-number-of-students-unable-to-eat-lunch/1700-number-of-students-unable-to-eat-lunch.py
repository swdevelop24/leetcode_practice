class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 학생들의 선호도를 카운트
        cnt = {}
        for s in students:
            if s not in cnt:
                cnt[s] = 0
            cnt[s] += 1

        # 초기 학생 수
        res = len(students)

        # 샌드위치를 처리
        for s in sandwiches:
            if cnt.get(s, 0)> 0:  # 샌드위치를 원하는 학생이 있는 경우
                res -= 1
                cnt[s] -= 1
            else:  # 샌드위치를 원하는 학생이 없는 경우
                return res

        return res