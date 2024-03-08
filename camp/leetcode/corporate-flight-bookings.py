class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0] * (n + 1)
        for start, end, seat in bookings:
            arr[start - 1] += seat
            if end < n:
                arr[end] -= seat

        prefix_sum = [0] * n
        prefix_sum[0] = arr[0]
        for i in range(1, len(arr) - 1):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i]

        return prefix_sum
