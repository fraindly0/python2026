# omd=int(input())
# total=0
# for i in range(omd):
#     a = int(input())
#     if a<29 and a>9:
#         total+=a
# print(total)

# gogll=int(input())
# total=0
# for i in range(gogll):
#     a=int(input())
#     if a>9 and a<100 and a//10!=a%10:
#         total+=1
# print(total)

# kolymbia=int(input())
# total=0
# for i in range(kolymbia):
#     a=int(input())
#     if a>9 and a<100 a//10!=a%10:
#         total+=1
# print(total)

# chuwi=int(input())
# total=0
# for i in range(chuwi):
#     a=int(input())
#     if a>9 and a<100 and a//10>=a%10:
#         total+=1
# print(total)

# asdasd=int(input())
# total=0
# for i in range(asdasd):
#     a=int(input())
#     if a%10==4:
#         total+=a
# print(total)

# sdsaasf=int(input())
# m=30001
# for i in range(sdsaasf):
#     a=int(input())
#     if a%3==0 and m>a:
#         m=a
# print(m)



num = int(input())
total = 0
for i in range(num):
    a = int(input())
    if a // 3 % 3 == 1 :
        total += a
print(total)
