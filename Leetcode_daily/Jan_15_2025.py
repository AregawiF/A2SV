class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = 0

        target_set_bits_count = bin(num2).count("1")
        set_bits_count = 0
        current_bit = 31  
        while set_bits_count < target_set_bits_count:
            if self._is_set(num1, current_bit) or (
                target_set_bits_count - set_bits_count > current_bit
            ):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            current_bit -= 1 
        return result

    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)