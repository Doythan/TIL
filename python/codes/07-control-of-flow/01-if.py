dust = int(input())

if dust > 150:
    if dust > 300:
        print('위험해요! 나가지 마세요!')
    else:
        print('매우 나쁨')

elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')