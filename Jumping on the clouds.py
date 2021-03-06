# https://www.facebook.com/abhi.sensharma/posts/1241788872853419
# Subscribed by Abhishek Sharma

# here I have solved the Jumping on the clouds program of the greedy algorithm

import sys

def jumpingOnClouds(c):
    n = len(c)
    i = 0
    count = 0
    while i < n - 1:
        if i + 2 < n and c[i + 2] == 0:
            i = i + 2
        else:
            i = i + 1
        count = count + 1
    return count

if __name__ == "__main__":
    n = int(input().strip())
    c = list(map(int, input().strip().split()))
    result = jumpingOnClouds(c)
    print(result)
