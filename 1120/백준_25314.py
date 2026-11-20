# long 한번에 4 바이트
# long N번에 4 * N 바이트
# N = 20이면 long이 5번에 int
N = int(input())

print('long '*(N//4) + 'int')