class 참치선물세트:
    일반 = 0
    야채 = 0
    고추 = 0
    def 총합(self, 이름):
        내용물갯수 = self.일반 + self.야채 + self.고추
        return 이름 + "\n" + str(내용물갯수)

참치3호세트 = 참치선물세트()

참치3호세트.일반 = 12
참치3호세트.야채 = 3
참치3호세트.고추 = 3
print(참치3호세트.총합("배경진 뭐야?"))