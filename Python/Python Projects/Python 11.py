#Reverse bit xor
def reverse_bits_xor(n, bit_size=8):
    
    for i in range(bit_size // 2):
        
        left_bit = (n >> (bit_size - 1 - i)) & 1
        right_bit = (n >> i) & 1

        
        if left_bit != right_bit:
            
            n ^= (1 << (bit_size - 1 - i))
            n ^= (1 << i)
    return n

x = 13
print(reverse_bits_xor(x, 8))  