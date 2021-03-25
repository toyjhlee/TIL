"""
어떤 수 N이 1이 될때가지 다음 두 과정 중 하나를 반복적으로 선택 수행하려고 한다.
단ㄷ, 두번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

ex) N = 17, K =4
1번 : 17-1 = 16
2번 : 16/4 = 4
3번 : 4/4 = 1

N과 K가 주어질 떄 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 최소 횟수 구하기

입력조건
- 첫째줄에 N(2<= N <= 100,000), K(2<= K <= 100,000) 가 공백으로 구분되며 각각 자연수로 주어진다.
  이때 N은 항상 K보다 크거나 같다. ( N >= K)

출력조건
- 첫째줄에 ㅜdl 1이 될때까지 1번혹은 2번의 과정을 수행해야하는 횟수의 최솟값 출력
"""
n, k = map(int, input().split())
cnt = 0


while(True):
    if n==1:
        break
    if n%k > 0:
        n-=1
        cnt+=1
    else:
        n //= k
        cnt += 1

print(cnt)

# n이 100억이상의 큰 수가 되는 경우

n, k = map(int, input().split())
cnt = 0


while(True):
    if n==1:
        break
    if n%k > 0:
        n-=1
        cnt+=1
    else:
        n //= k
        cnt += 1

print(cnt)
