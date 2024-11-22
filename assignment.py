number_of_digits = int(input())
def calculatePi(digits):
  result = 0
  for i in range (number_of_digits):
    result = (result+((-1)**i)/(2*i+1)*4)
  return result

print(calculatePi(number_of_digits))
