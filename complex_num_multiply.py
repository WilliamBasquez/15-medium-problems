#create a list inside store the values of the multiplications
#at the end 
def complexNumberMultiply(a, b):
	answer = [] #[8,+,4i,-,4i,-,2i^2] - > [8,+,0,-,2i^2] -> [8,+,0,-,-2] -> [8,+,0,+2] -> 8+0+2 = 10
	n1 = 0
	n2 = 0
	while n1 < len(a) and n2 < len(b):
		answer.append(a[n1] * b[n2])
		n2+=1
	#1 + i^2 + 2 * i or 1 + i + i -1 = 0-2i
	#1) (1) * (1) = 1
	#2) (1) * (i) = i
	#3) (i) * (1) = i
	#4) (i) * (i) = i^2 = -1
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#(2-i) * (4+2i)
	#1) 2 * 4 = 8
	#2) 2 * 2i = 4i
	#3)-i * 4 = -4i
	#4)-i * 2i = -2i^2
	
	#8 + 4i - 4i - 2i^2 = 8 +0i - 2(-1) = 8 + 2 = 10