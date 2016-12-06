class Solution(object):
    def minMeetingRooms(self, intervals):
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        mts = []
        i = j = 0
        while i < len(start) or j < len(end):
            if i >= len(start):
                mts.append((end[j], 'e'))
                j += 1
            elif j >= len(end):
                mts.append((start[i], 's'))
                i += 1
            elif start[i] < end[j]:
                mts.append((start[i],'s'))
                i += 1
            elif start[i] < end[j]:
                mts.append((end[j],'e'))
                j += 1
            else:
                i += 1
                j += 1
        print(mts)
        r = []
        a = 0
        for m in mts:
            if m[1] == 's':
                if a > 0:
                    a -= 1
                else:
                    r.append(m)
            if m[1] == 'e':
                a += 1
        return r
mts = [[0, 30],[5, 10],[15, 20]]

# mts= [[13,15],[1,13]]
print(Solution().minMeetingRooms(mts))