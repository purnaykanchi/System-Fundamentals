def fcfs_disk_scheduling(requests, head_start):
    total_head_movement = 0
    current_head_position = head_start
    for request in requests:
        head_movement = abs(current_head_position - request)
        total_head_movement += head_movement
        current_head_position = request
    return total_head_movement
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    initial_head_position = 53
    total_movement = fcfs_disk_scheduling(requests, initial_head_position)
    print(f"Total head movement: {total_movement}")