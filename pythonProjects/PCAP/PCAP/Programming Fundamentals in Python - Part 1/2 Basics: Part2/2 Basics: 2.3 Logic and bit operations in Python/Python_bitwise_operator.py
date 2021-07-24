flagRegister = 0x1234

print(flagRegister)

var = 17
varRight = var >> 1  # 17 // 2 -> 8 (shifting to the right by one bit is the same as integer division by 2)
varLeft = var << 2  # 17 * 4 -> 68 (shifting to the left by two bits is the same as integer multiplication by 4)

print(var, varLeft, varRight, end=' ')
