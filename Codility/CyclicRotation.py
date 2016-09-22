#given a zero-indexed array A consisting of N integers and an integer K, returns the array A rotated K times.
def rotate(l, n):
	return l[n:] + l[:n]