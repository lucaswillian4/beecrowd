X, Y = map(int, input().split())

for i in range(1, Y+1):
    print(i, end=[" ","\n"][i%X == 0])