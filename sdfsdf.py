a = [1, 2, 3, 4, 5,6]
b = [1, 3, 2, 4, 5,9]

# 일치하는 값의 개수를 세기 위한 변수
match_count = 0

# 두 리스트의 길이가 같다고 가정하고 반복문 실행
for i in a.iterrows():
    if a[i] == b[i]:  # 같은 위치의 값이 같다면
        match_count +=1


print
