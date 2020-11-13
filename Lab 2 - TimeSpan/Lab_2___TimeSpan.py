from time340 import TimeSpan
dur1 = TimeSpan(3.1, 7)
dur2 = TimeSpan(4, -5, 8)
print(dur1)
print(dur2)
print(dur1 + dur2)
dur2 += dur1
print(dur2)
dur3 = -dur2
print(dur3)
dur4 = TimeSpan(6,7,8)
dur5 = TimeSpan()
dur5.setTime(6, 5, 8)
print("dur4: " + str(dur4))
print("dur5: " + str(dur5))
if dur4 >= dur5:
	print("dur4 is >= than dur5")
else:
	print("dur4 is not >= than dur5")
dur6 = TimeSpan(9, 8, -7)
dur6 = -dur6
print(dur6)