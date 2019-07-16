# https://github.com/minsuk-heo/problemsolving/blob/master/coding_interview_2018/dynamic_programming/largest_sum_subarray.py
def largest_sum_subarray(arr):
    lsum = arr[0]
    cur = arr[0]
    for i in range(1, len(arr)):
        if cur > 0:
            cur = cur + arr[i]
        else:
            cur = arr[i]
        lsum = max(lsum, cur)
    return lsum
