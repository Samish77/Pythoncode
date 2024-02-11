# display result of student

sub1 = int(input("Enter first subject marks"))
sub2 = int(input("Enter first subject marks"))
sub3 = int(input("Enter first subject marks"))

if(sub1<35 or sub2<35 or sub3<35):
    print("You are fail because you have less than 40 mark in one subject")
elif((sub1+sub2+sub3)/3 <40):
    print("you are fail due to percent less than 40")
else:
    print('conguralation you are pass')       