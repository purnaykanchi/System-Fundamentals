def round_robin(processes, time_quantum):
    n = len(processes)
    remaining_time = [process[1] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0
    queue = []
    while any(time > 0 for time in remaining_time):
        for i in range(n):
            if processes[i][0] <= current_time and i not in queue:
                queue.append(i)
        if queue:
            process_index = queue.pop(0)
            if remaining_time[process_index] == processes[process_index][1]:
                waiting_time[process_index] = current_time - processes[process_index][0]
            execution_time = min(time_quantum, remaining_time[process_index])
            remaining_time[process_index] -= execution_time
            current_time += execution_time
            if remaining_time[process_index] > 0:
                queue.append(process_index)
            else:
               
                turnaround_time[process_index] = current_time - processes[process_index][0]
        else:
             current_time += 1
    return waiting_time, turnaround_time
processes_round_robin = [(0, 10), (4, 4), (8, 3), (15, 7)]
time_quantum = 3
waiting_time_round_robin, turnaround_time_round_robin = round_robin(processes_round_robin, time_quantum)
print("Round Robin Scheduling:")
print("Process\tWaiting Time\tTurnaround Time")
for i in range(len(processes_round_robin)):
    print(f"{i}\t\t{waiting_time_round_robin[i]}\t\t{turnaround_time_round_robin[i]}")