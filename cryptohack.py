
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
