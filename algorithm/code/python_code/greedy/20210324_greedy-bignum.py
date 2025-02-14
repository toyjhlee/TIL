"""
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더해 가장 큰 수를 만드는 법칙
단, 배열의 특정 인덱스에 해당하는 수가 연속해서 K번 초과해 더해질 수 없다.

ex) 2,4,5,4,6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정
수가 가장 큰 결과는 6 + 6 + 6 + 5 + 6+ 6+ 6+ 5 =46

단 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른것으로 간주
ex) arr = [3, 4, 3, 4, 3], M = 7, K = 2
ans = 4 + 4 + 4 + 4 + 4 + 4 + 4 = 28

입력조건
- 첫째 줄에 N(2<= N <= 1000), M(1<=M<=10000), K(1<=K<=10000) 자연수가 주여지며, 각 자연수는 공백으로 구분
- 둘째 줄에 N개의 자연수가 주어지며, 각 자연수는 공백으로 구분, 단 각 자연수는 1이상 10000이하의 수
- K<=M

출력 조건
- 큰 수의 법칙에 따른 답
"""

# 공백 구분하여 입력 받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

if len(data) != n:
	print("입력값 오류")

data.sort()
first = data[n-1]
second = data[n-2]

# 내가 작성한 풀이 방법
# result = 0
# result += first * k * (m//k) # int(m/k)와 m//k 동일
# result += second * (m%k)

# 큰 수가 더해지는 수
cnt = m // (k+1) * k
cnt += m % (k+1)

result = 0
result += first * cnt
result += second * (m-cnt)

print(result)
