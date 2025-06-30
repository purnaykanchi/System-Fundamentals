class PriorityQueue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self, process):
        self.queue.append(process)
        self.queue.sort(key=lambda x: x[2])
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
def preemptive_priority(processes):
    n = len(processes)
    current_time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_time = [process[1] for process in processes]
    priority_queue = PriorityQueue()
    while any(time > 0 for time in remaining_time):
        for process in processes:
            if process[0] <= current_time and process not in priority_queue.queue:
                priority_queue.enqueue(process)
        if not priority_queue.is_empty():
            executing_process = priority_queue.dequeue()
            process_index = processes.index(executing_process)
            if remaining_time[process_index] == executing_process[1]:
                waiting_time[process_index] = current_time - executing_process[0]
            remaining_time[process_index] -= 1
            current_time += 1
            if remaining_time[process_index] == 0:
                turnaround_time[process_index] = current_time - executing_process[0]
        else:
             current_time += 1
    return waiting_time, turnaround_time
processes_preemptive_priority = [(1, 6, 2), (2, 8, 1), (3, 7, 3), (4, 3, 4)]
waiting_time_preemptive_priority, turnaround_time_preemptive_priority = preemptive_priority(processes_preemptive_priority)
print("Preemptive Priority Scheduling:")
print("Process\tWaiting Time\tTurnaround Time")
for i in range(len(processes_preemptive_priority)):
    print(f"{processes_preemptive_priority[i][0]}\t{waiting_time_preemptive_priority[i]}\t\t{turnaround_time_preemptive_priority[i]}")