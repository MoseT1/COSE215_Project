import re

## conf
INPUT = "./input.txt"
OUTPUT = "./output.txt"

def verify_reg(reg):
    # 주민등록번호 검증
    
    factors = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    sum_of_products = sum(int(a) * b for a, b in zip(rrn[:-1], factors))
    checksum = (11 - sum_of_products % 11) % 10
    return checksum == int(rrn[-1])

def main():
    fres = open(OUTPUT, 'w', encoding = "UTF-8")
    with open(INPUT, 'r', encoding = "UTF-8") as fp:
        body = ''.join(fp.readlines())
        #print ("** UNPROTECTED INPUT **")
        print (body) # Check the input file.

        ############################
        # Write your own code here #
        for line in fp:
            for reg in re.findall(r'\b\d{6}[-\s]\d{7}\b', line):
                reg = reg.replace(' ', '')
                print(reg)
        ############################

        # Please store the body with protected registration numbers
        protectedBody = ''
        print ("** PROTECTED OUTPUT **")
        print (protectedBody)
        fres.write(protectedBody)
        fres.close()

""" EXECUTE """
if __name__ == "__main__":
	main()


# import re

# INPUT = "./input.txt"
# OUTPUT = "./output.txt"

# def verify_rrn(rrn):
#     # 주민등록번호 검증
#     factors = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
#     sum_of_products = sum(int(a) * b for a, b in zip(rrn[:-1], factors))
#     checksum = (11 - sum_of_products % 11) % 10
#     return checksum == int(rrn[-1])

# def main():
#     with open(INPUT, 'r', encoding="UTF-8") as fin, open(OUTPUT, 'w', encoding="UTF-8") as fout:
#         for line in fin:
#             for rrn in re.findall(r'\b\d{6}[-\s]\d{7}\b', line):
#                 rrn = rrn.replace(' ', '')
#                 if verify_rrn(rrn):
#                     line = line.replace(rrn, '******-*******')
#             fout.write(line)

# if __name__ == "__main__":
#     main()