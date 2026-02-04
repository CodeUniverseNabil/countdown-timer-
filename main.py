import time

count=int(input("input the your time"))

while count>0:

    print(f"your sec is     {count}")

    time.sleep(1)

    count-=1

print("time is complete")
