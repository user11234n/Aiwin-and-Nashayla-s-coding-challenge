from fractions import Fraction
def is_curious_fraction(numerator, denominator):
    # Convert numbers to strings for easy digit manipulation
    num_str = str(numerator)
    den_str = str(denominator)
    
    for digit in num_str: 
        if digit in den_str and digit != '0':
            new_num = int(num_str.replace(digit, '', 1))
            new_den = int(den_str.replace(digit, '', 1))
            if new_den != 0 and new_num / new_den == numerator / denominator:
                return True 
    return False
curious_fractions = []
for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        if is_curious_fraction(numerator, denominator):
            curious_fractions.append(Fraction(numerator, denominator))
product = Fraction(1,1)
for fraction in curious_fractions:
    product *= fraction
print(product.denominator)

