
#Task 1
#flag given by them
#flag = crypto{y0ur_f1rst_fl4g}

#Task 2
#I found flag when i run the program provided by them
#flag = crypto{z3n_0f_pyth0n}

# Task 3
lst = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
for i in lst:
    print(chr(i),end="")
# flag = crypto{ASCII_pr1nt4bl3}

#Task 4
dec = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(dec))
# flag = crypto{You_will_be_working_with_hex_strings_a_lot}

#Task 5
import base64
hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bin = bytes.fromhex(hex)
b64 = base64.b64encode(bin)
print(b64)
# flag = crypto/Base+64+Encoding+is+Web+Safe/

#Task 6
decimal = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
hexadecimal = hex(decimal)[2:]  
binary = bytes.fromhex(hexadecimal)
message = binary.decode('utf-8')
print(message)
# flag = crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}

#Task 7
a = "label"
b= 13
for i in a:
    c = ord(i)
    e = c ^ b
    g = chr(e)
    print(g,end="")
# flag = crypto{aloha}

#Task 8
key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_k1_k2_k3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
a = int(key1, 16)                   #changes to decimal
b = int(key2_key3, 16)
inter = a ^ b                       #xor's the two keys
c = int(flag_k1_k2_k3, 16)
final = inter ^ c                   #xoring we obtain hexa of flag
final_res = hex(final)[2:]
bytes_of = bytes.fromhex(final_res)
ascii_ = bytes_of.decode("ASCII")
print(ascii_)
# flag = crypto{x0r_i5_ass0c1at1v3}

#Task 9
from pwn import xor
given = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
python = bytes.fromhex(given)
for i in range(256):
    y=xor(python,i).decode()
    if "crypto" in y:
        print(y)
flag = crypto{0x10_15_my_f4v0ur173_by7e}

#Task 10
from pwn import xor
given = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
givenbytes = bytes.fromhex(given)
start = "crypto{"                               #to determine first part of the key(first 7 charecters)
last = "}"                                      #to determine last part of the key(last 1 charecter)
result = xor(givenbytes,start)                      
print(result.decode())
res = xor(givenbytes,last).decode()
print(res)                                      #therefore key is myXORKey
final = xor(givenbytes,"myXORkey").decode()
print(final)

outputs = myXORke+y_QHOMe$~seG8bGURNDFWg)a|TM!an
          sv\B[yc5v[\ZISj szwA&mCX[\ZISj sz[I,h|y
          crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
flag = crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
