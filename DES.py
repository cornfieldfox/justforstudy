IP = [  [58, 50, 42, 34, 26, 18, 10, 2], 
        [60, 52, 44, 36, 28, 20, 12, 4],
        [62, 54, 46, 38, 30, 22, 14, 6],
        [64, 56, 48, 40, 32, 24, 16, 8],
        [57, 49, 41, 33, 25, 17, 9, 1],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [61, 53, 45, 37, 29, 21, 13, 5],
        [63, 55, 47, 39, 31, 23, 15, 7]]

IP_R = [[40, 8, 48, 16, 56, 24, 64, 32],
        [39, 7, 47, 15, 55, 23, 63, 31],
        [38, 6, 46, 14, 54, 22, 62, 30],
        [37, 5, 45, 13, 53, 21, 61, 29],
        [36, 4, 44, 12, 52, 20, 60, 28],
        [35, 3, 43, 11, 51, 19, 59, 27],
        [34, 2, 42, 10, 50, 18, 58, 26],
        [33, 1, 41, 9, 49, 17, 57, 25]]
E = [	[32,1,2,3,4,5],
	 	[4,5,6,7,8,9],
	 	[8,9,10,11,12,13],
	 	[12,13,14,15,16,17],
	 	[16,17,18,19,20,21],
	 	[20,21,22,23,24,25],
	 	[24,25,26,27,28,29],
	 	[28,29,30,31,32,1]]
PC_1 = [[57,49,41,33,25,17,9],
		[1,58,50,42,34,26,18],
		[10,2,59,51,43,35,27],
		[19,11,3,60,52,44,36],
		[63,55,47,39,31,23,15],
		[7,62,54,46,38,30,22],
		[14,6,61,53,45,37,29],
		[21,13,5,28,20,12,4]]

C = ["" for a in range(17)]
D = ["" for a in range(17)]
K = ["" for a in range(17)]		#17 subkey
I =[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
PC_2 = [[14,17,11,24,1,5],
		[3,28,15,6,21,10],
		[23,19,12,4,26,8],
		[16,7,27,20,13,2],
		[41,52,31,37,47,55],
		[30,40,51,45,33,48],
		[44,49,39,56,34,53],
		[46,42,50,36,29,32]]
L = ["" for a in range(17)]
R = ["" for a in range(17)]
S=[	   [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
	   [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
	   [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
       [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]] ,
	 
	 	[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
		[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
		[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
		[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],

		[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
		[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
		[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
		[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],

		[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
		[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
		[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
		[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],

	 	[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
		[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
		[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
		[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],

		[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
		[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
		[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
		[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],

	 	[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
		[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
		[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
		[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],

	 	[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
		[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
		[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
		[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]]
P = [[16,7,20,21],
	 [29,12,28,17],
	 [1,15,23,26],
	 [5,18,31,10],
	 [2,8,24,14],
	 [32,27,3,9],
	 [19,13,30,6],
	 [22,11,4,25]]

def DES(string):
	#change to binary
	temp_bin = ""
	for i in range(0,8):
		temp = str(bin(ord(string[i]))[2:].zfill(8))
		temp_bin = temp_bin + temp

	#print temp_bin
	temp_bin = DES_IP(IP,temp_bin)
	L[0] = temp_bin[:32]
	R[0] = temp_bin[32:]
	
	#16 times
	for i in range(1,17):

		#give number to L&R
		L[i] = R[i-1]
		R[i] = DES_E(R[i-1])

		# xor with sub key
		temp = ""
		for t in range(0,48):
			temp = temp + str(int(R[i][t])^int(K[i][t]))
		
		R[i] = temp
		# S 
		B = [R[i][t:t+6] for t in range(0,len( R[ i ] ),6 ) ]
		
		temp = ""
		for t in range(0, 8):
			temp = temp + DES_S(S[t],B[t])
		R[i] = temp
		#P
		R[i] = DES_P(R[i])
		#xor with L_i-1
		temp = ""
		for t in range(0,32):
			temp = temp + str(int(R[i][t])^int(L[i-1][t]))
		R[i] = temp

	#change the last time
	temp = R[16] + L[16]

	#IP_-1
	return DES_IP(IP_R,temp)
def DES_IP(IP,string):
	k = 0
	Str_IP_arr = [0 for a in range(64)]
	for i in range(0,8):
		for j in range(0,8):
			num = IP[i][j]
			Str_IP_arr[k] = string[num-1]
			k+= 1
	Str_IP = ""
	for i in range(len(Str_IP_arr)):
		Str_IP = Str_IP + Str_IP_arr[i]
	return Str_IP


def DES_E(R_0):
	k = 0
	R_0_str = str(R_0)
	R_E_arr = [0 for a in range(48)]
	for i in range(0,8):
		for j in range (0,6):
			#print "i"+str(i)+":"+"j"+str(j)
			num = E[i][j]
			R_E_arr[k] = R_0_str[num-1]
			k += 1
	R_E=""
	for i in range(len(R_E_arr)):
		R_E = R_E + R_E_arr[i]
	#print R_0_str
	return R_E

def DES_S(S,string):
	row = int(string[0]+string[5],2)
	col = int(string[1]+string[2]+string[3]+string[4],2)
	temp = str( bin( S[row][col] ) [2:] ).zfill(4)
	return temp

def DES_P(string):
	k = 0
	temp_arr = [0 for a in range(len(P) * len(P[1]) )]
	for i in range( 0,len(P) ):
		for j in range( 0, len(P[1]) ): 
			num = P[i][j]
			temp_arr[k] = string[num-1]
			k += 1
	temp = ""
	for i in range( len(temp_arr) ):
		temp = temp + temp_arr[i]
	return temp


def subKey(arrary):
	bin_pwd = ""
	for i in range(len(arrary)):
		bin_pwd = bin_pwd + arrary[i]
	#print bin_pwd
	k = 0
	bin_pwd_str  = str(bin_pwd)
	bin_pwd_arr = [0 for a in range(56)]
	for i in range(0,8):
		for j in range(0,7):
			num = PC_1[i][j]
			bin_pwd_arr[k] = bin_pwd_str[num-1]
			k+=1
	temp = ""
	for i in range(len(bin_pwd_arr)):
		temp  = temp + bin_pwd_arr[i]
	C[0] = C[0]+str(temp[0:28])
	D[0] = str(temp[28:56])

	#generate 16 subkeys
	for i in range(1,17):

		C[i] = C[i-1][I[i-1]:]+C[i-1][:I[i-1]]
		D[i] = D[i-1][I[i-1]:]+D[i-1][:I[i-1]]
		pre_K = C[i]+D[i]

		temp_arr = [0 for a in range(48)]
		k = 0
		for t in range (0,8):
			for j in range (0,6):
				num = PC_2[t][j]
				temp_arr[k] = pre_K[num-1]
				k += 1

		for t in range(len(temp_arr)):
			K[i] = K[i] + temp_arr[t]
 



'''raw_pwd = raw_input("please input a 8 bit password:\n")

while len(str(raw_pwd)) != 8:
	print "the length of password is wrong"
	raw_pwd = raw_input("please input a 8 bit password:\n")'''
raw_pwd = "qipuxuan" #test
bin_pwd = []

#make 64bit cipher
for i in range(0,8):
	temp = str( bin( ord( raw_pwd[i] ) ) [2:] ).zfill((7))		#2^7 = 128 > ord("z") = 122 , 7 bit is OK
	bin_pwd.append(temp + str(temp.count("1") % 2) )	#using even check

subKey(bin_pwd) # generate 17 subkeys


plantext = "".join(open("plantext.txt"))
plant_splite=[""]

for x in range(0,len(plantext),8):
	plant_splite.append(plantext[x:x+8])


f2 = open("cipher.txt","w")
for i in range(1,len(plant_splite)):
	cipher_bin_arr = [0]
	if len(plant_splite[i]) < 8:
		plant_splite[i] = plant_splite[i].ljust(8," ")
 
	ciphertext_bin = DES(plant_splite[i])
	for x in range(0, len(ciphertext_bin) , 8):
		cipher_bin_arr.append(int(ciphertext_bin[x:x+7],2) )

	for i in range(1,9):
		f2.write(chr(cipher_bin_arr[i]))
f2.close()
