import random
import string
from ctypes import cdll
lib = cdll.LoadLibrary("./libs/lcs.so")

class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]

lib.LCS.argtypes = [c_char_p, c_char_p]

def make_lengths(string, sub):
    return [[0 for i in range(0,len(sub)+1)] for j in range(0,len(string)+1)]

def make_length(N):
    return [[0 for i in range(0, N)] for j in range(0, N)]

g_lengths = make_length(400)


def ran_string(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def my_lcs_new(string, sub):
    return lib.LCS(string.split(), sub.split())

def my_lcs(string, sub):
    if(len(string)< len(sub)):
        sub, string = string, sub

    lengths = make_lengths(string, sub)

    for j in range(1,len(sub)+1):
        for i in range(1,len(string)+1):
            if(string[i-1] == sub[j-1]):
                lengths[i][j] = lengths[i-1][j-1] + 1
            else:
                lengths[i][j] = max(lengths[i-1][j] , lengths[i][j-1])

    return lengths[len(string)][len(sub)]

for i in range(40):
    s = ran_string(300)
    sub = ran_string(200)

    res1 = my_lcs(s, sub)
    res2 = my_lcs_new(s, sub)

    if not res1 == res2:
        print('wrong')
