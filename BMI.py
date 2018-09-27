def BMI(height, weight):
    index = weight*703/height**2
    if index < 18.5:
        print('Underweight')
    elif bmi < 25:
        print('normal')
    else:
        print('overweight')