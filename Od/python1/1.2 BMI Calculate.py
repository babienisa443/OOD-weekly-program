h, w = list(map(float, input('Enter your High and Weight : ').split()))
BMI = w / (h**2)
if BMI < 18.50:
    print('Less Weight')

elif 18.50 <= BMI and BMI < 23:
    print('Normal Weight')

elif 23 <= BMI and BMI < 25:
    print('More than Normal Weight')

elif 25 <= BMI and BMI < 30:
    print('Getting Fat')

elif BMI >= 30:
    print('Fat')
