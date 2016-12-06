import math
import time
from ctypes import *
class Solution(object):
    def sqrt1(self, n):
        r = n
        while r > n / r:
            r = (r + n / r)*1.0 / 2
        return r

    def sqrt2(self, n):
        threehalfs = 1.5
        x2 = n * 0.5
        y = n
        i = id(id(long(y)))
        print(i)
        i = 0x5f3759df - (i >> 1)
        print(i)
        y = id(id(long(i)))
        print(y)
        y = y * (threehalfs - (x2 * y * y))
        y = y * (threehalfs - (x2 * y * y))

        return y

# start = time.time()
# print(Solution().sqrt1(5))
# end = time.time()
# print((end - start)* 10**9)

# start = time.time()
# print(math.sqrt(5))
# end = time.time()
# print((end - start)* 10**9)

start = time.time()
print(Solution().sqrt2(5))
end = time.time()
print((end - start)* 10**9)
#       float Q_rsqrt( float number )
# {
#   long i;
#   float x2, y;
#   const float threehalfs = 1.5F;

#   x2 = number * 0.5F;
#   y  = number;
#   i  = * ( long * ) &y;                       // evil floating point bit level hacking
#   i  = 0x5f3759df - ( i >> 1 );               // what the fuck? 
#   y  = * ( float * ) &i;
#   y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
# //    y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

#   return y;
# }


# var buf = new ArrayBuffer(4),
#     f32=new Float32Array(buf),
#     u32=new Uint32Array(buf);
# function q2(x) {
#   var x2 = 0.5 * (f32[0] = x);
#   u32[0] = (0x5f3759df - (u32[0] >> 1));
#   var y = f32[0];
#   y  = y * ( 1.5 - ( x2 * y * y ) );   // 1st iteration
#   return y;
# }


class Solution(object):
    def mySqrt(self, n):
        if n == 0:
            return 0
        r = n
        while r > n / r:
            r = (r + n / r)*1.0 / 2
        return r