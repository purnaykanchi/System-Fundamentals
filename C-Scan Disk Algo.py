def cscan_disk_scheduling(requests, head_start, direction="left", disk_size=200):
    requests_copy = list(requests)
    requests_copy.sort()
    total_head_movement = 0
    current_head_position = head_start
    if direction == "left":
        head_movement_direction = -1  
    elif direction == "right":
        head_movement_direction = 1  
    else:
        raise ValueError("Invalid direction. Use 'left' or 'right'.")
    while requests_copy:
        for request in range(current_head_position, -1, -1):
            if request in requests_copy:
                head_movement = abs(current_head_position - request)
                total_head_movement += head_movement
                current_head_position = request
                requests_copy.remove(request)
        if requests_copy:
            total_head_movement += abs(current_head_position - disk_size)
            current_head_position = 0
    return total_head_movement
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    initial_head_position = 53
    total_movement = cscan_disk_scheduling(requests, initial_head_position, direction="left", disk_size=200)
    print(f"Total head movement: {total_movement}")