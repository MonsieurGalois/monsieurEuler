t=2
for a in range(2):
	t1=200-a*100
	for b in range(0,t1/50+1):
		t2=t1-50*b
		if t2<0:
			break
		for c in range(0,t2/20+1):
			t3=t2-20*c
			if t3<0:
				break
			for d in range(0,t3/10+1):
				t4=t3-10*d
				if t4<0:
					break
				for e in range(0,t4/5+1):
					t5=t4-5*e
					if t5<0:
						break
					for f in range(0,t5/2+1):
						t6=t5-2*f
						if t6>=0:
							t+=1
						if t6<0:
							break
print t
