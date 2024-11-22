redo = True
while redo:
  try:
    number_of_digits = int(input())
    redo = False
  except:
    print("Please enter a positive interger")
    redo = True
def calculatePi(digits):
  result = 0
  for i in range (number_of_digits):
    result = (result+((-1)**i*4)/(2*i+1))
  return result

print(calculatePi(number_of_digits))
