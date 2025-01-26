def captains_room(k, room_numbers):
    count = {}
    for room in room_numbers:
        if room in count:
            count[room] += 1
        else:
            count[room] = 1
    for room in count:
        if count[room] == 1:
            return room

k = int(input())
room_numbers = list(map(int, input().split()))
room_number = captains_room(k, room_numbers)
print(room_number)