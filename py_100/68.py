import time

bus_times = input().split()
now_time = input()


# tm = time.localtime()

# if tm.tm_min < 10:
#     minute="0"+str(tm.tm_min)
# else:
#     minute= tm.tm_min

# print(f"{tm.tm_hour}:{minute}")

for bus_time in bus_times:

    bus_time_hour = int(bus_time[0:2])
    now_time_hour = int(now_time[0:2])

    bus_time_min = int(bus_time[3:5])
    now_time_min = int(now_time[3:5])
    
    if bus_time_hour < now_time_hour:
        print("지나갔습니다")
    elif bus_time_hour == now_time_hour:
        if bus_time_min < now_time_min:
            print("지나갔습니다")
        else:
            print(f"{now_time_min - bus_time_min}")
    else:
        print(f"{now_time_hour-bus_time_hour}시간 {now_time_min - bus_time_min }분")
        
            
    