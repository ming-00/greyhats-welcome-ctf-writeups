# open-gates.py

# var gate1 = (key) => {
#     if (key == "1ts") return true;
#     return false;
# }
key_1 = "1ts"
print(key_1)

# var gate2 = (key) => {
#     if (key.length != 6)  return false;
#     if ((key.charCodeAt(0) ^ "Chicken".charCodeAt(0)) != 0x20) return false;
#     if ((key.charCodeAt(1) ^ "Doughnut".charCodeAt(4)) != 0x58) return false;
#     if ((key.charCodeAt(2) ^ "Fruit".charCodeAt(3)) != 0x04) return false;
#     if ((key.charCodeAt(3) ^ "Icecream".charCodeAt(5)) != 0x54) return false;
#     if ((key.charCodeAt(4) ^ "Sausage".charCodeAt(3)) != 0x1d) return false;
#     if ((key.charCodeAt(5) ^ "Durian".charCodeAt(4)) != 0x06) return false;
#     return true;
# }
key_2 = ""
key_2 += chr(ord("Chicken"[0]) ^ 0x20)
key_2 += chr(ord("Doughnut"[4]) ^ 0x58)
key_2 += chr(ord("Fruit"[3]) ^ 0x04)
key_2 += chr(ord("Icecream"[5]) ^ 0x54)
key_2 += chr(ord("Sausage"[3]) ^ 0x1d)
key_2 += chr(ord("Durian"[4]) ^ 0x06)
print(key_2) # key_2 = "c0m1ng"

# var gate3 = (key) => {
#     if (key.length != 2) return false;
#     var c0 = key.charCodeAt(0);
#     var c1 = key.charCodeAt(1);
#     if (c0 > c1 && c0 + c1 == 164 && c0 * c1 == 5568) return true;
#     return false;
# }
def generate_3():
    for i in range(32, 126): # only valid ascii characters
        for j in range(32, 126):
            if (i > j and i + j == 164  and i * j == 5568):
                return chr(i) + chr(j)
key_3 = generate_3()
print(key_3) # key_3 = "t0"

# var gate4 = (key) => {
#     if (key.length != 4) return false;
#     var rs = [2, 3, 4, 5];
#     var target = [201, 129, 214, 102];
#     for (var i = 0; i < 4; ++i) {
#         var r = rs[i];
#         var c = key.charCodeAt(i);
#         if ((((c << r) & 0xff) | (c >> (8 - r))) != target[i]) return false;
#     }
#     return true;
# }
key_4 = ""
def generate_4() :
    key = ""
    rs = [2, 3, 4, 5]
    target = [201, 129, 214, 102]
    for i in range(4):
        for digit in range(33, 126): # only valid ascii characters
            r = rs[i]
            c = digit
            if (((c << r) & 0xff) | (c >> (8 - r))) != target[i]:
                continue
            else:
                key += chr(digit)
                break
    return key
key_4 = generate_4()
print(key_4) # key_4 = "r0m3"