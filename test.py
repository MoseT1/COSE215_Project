def verify_reg(reg):
    # 주민등록번호 검증
    AB = int(reg[0:2])
    CD = int(reg[2:4])
    EF = int(reg[4:6])
    G = int(reg[7])
    M = int(reg[-1])
    if CD >12:
        return False
    if CD == 1 or CD == 3 or CD == 5 or CD == 7 or CD == 8 or CD == 10 or CD == 12:
        if EF > 31:
            return False
    elif CD == 4 or CD == 6 or CD == 9 or CD == 11:
        if EF > 30:
            return False
    else:
        if EF > 28:
            return False
    
    if AB >= 24 and AB <= 99:
        if G != 1 and G !=2:
            
            return False
    else:
        if G != 3 and G != 4:
            return False
        
    reg = reg.replace('-', '')
    factors = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    sum_of_products = sum(int(a) * b for a, b in zip(reg[:-1], factors))
    checksum = (11 - sum_of_products % 11) % 10
    
    return checksum == M


r = '191217 -3456780'
r2 = r.replace(' ', '')
if verify_reg(r2):
    r='3'
    
print(r)
