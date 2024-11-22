number_of_digits = int(input())
def calculatePi(digits):
  result = 0
  for i in range (number_of_digits):
    result = ((-1)**number_of_digits)/(2*number_of_digits + 1)
  return result

print(calculatePi(number_of_digits))
