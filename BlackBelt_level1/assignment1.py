Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
date = Sessions_Attended['sessions'].split(",")
while '' in date:
    date.remove('')
number=len(date)
print("I have attended ",number ,"sessions!!")