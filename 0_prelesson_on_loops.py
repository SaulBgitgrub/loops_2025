# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  
#For loops execute a block of code a fixed number of times, you can iterate over a range, string, sequence etc...

# for x in range(1,11): #use (1,11,2) to count by twos
#     print(x)
for x in range(1,11,2):
    print(x)
# print("Happy new year")

# # credit_card = "1234-5678-9012-3456"
for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)