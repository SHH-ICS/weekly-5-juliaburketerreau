redo = True
while redo:
  try:
    number_of_digits = int(input())
    if number_of_digits > 0:
      redo = False
    else: 
      number_of_digits < 0
      print("Number must be postive")
      redo = True
  except:
      print("Please enter a positive interger not a letter")
      redo = True
def calculatePi(digits):
  result = 0
  for i in range (number_of_digits):
    result = (result+((-1)**i*4)/(2*i+1))
  return result

print(calculatePi(number_of_digits))
