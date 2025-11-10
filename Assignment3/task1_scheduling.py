"""
Task 1: CPU Scheduling Simulation
- Priority Scheduling
- Round Robin Scheduling
"""

def priority_scheduling():
    """Simulate Priority Scheduling Algorithm"""
    print("=" * 50)
    print("PRIORITY SCHEDULING SIMULATION")
    print("=" * 50)
    
    processes = []
    n = int(input("Enter number of processes: "))
    
    # Input process details
    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        pr = int(input(f"Enter Priority (lower number = higher priority) for P{i+1}: "))
        processes.append((f"P{i+1}", bt, pr))
    
    # Sort by priority (lower number = higher priority)
    processes.sort(key=lambda x: x[2])
    
    # Calculate waiting and turnaround times
    wt = 0
    total_wt = 0
    total_tt = 0
    
    print("\n" + "=" * 50)
    print("Priority Scheduling Results:")
    print("=" * 50)
    print("PID\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    print("-" * 70)
    
    gantt_chart = []
    current_time = 0
    
    for pid, bt, pr in processes:
        wt = current_time
        tat = wt + bt
        gantt_chart.append((pid, current_time, current_time + bt))
        
        print(f"{pid}\t{bt}\t\t{pr}\t\t{wt}\t\t{tat}")
        
        total_wt += wt
        total_tt += tat
        current_time += bt
    
    # Display Gantt Chart
    print("\nGantt Chart:")
    print("Time: ", end="")
    for pid, start, end in gantt_chart:
        print(f" [{start}-{pid}-{end}] ", end="")
    print()
    
    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tt / n:.2f}")

def round_robin_scheduling():
    """Simulate Round Robin Scheduling Algorithm"""
    print("\n" + "=" * 50)
    print("ROUND ROBIN SCHEDULING SIMULATION")
    print("=" * 50)
    
    n = int(input("Enter number of processes: "))
    time_quantum = int(input("Enter time quantum: "))
    
    processes = []
    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        processes.append([f"P{i+1}", bt, 0, bt])  # [PID, Burst Time, Waiting Time, Remaining Time]
    
    current_time = 0
    completed = 0
    gantt_chart = []
    
    while completed < n:
        for i in range(n):
            pid, bt, wt, remaining = processes[i]
            
            if remaining > 0:
                if remaining > time_quantum:
                    # Process executes for time quantum
                    gantt_chart.append((pid, current_time, current_time + time_quantum))
                    current_time += time_quantum
                    processes[i][3] = remaining - time_quantum
                else:
                    # Process completes execution
                    gantt_chart.append((pid, current_time, current_time + remaining))
                    processes[i][2] = current_time - bt + remaining  # Waiting time calculation
                    current_time += remaining
                    processes[i][3] = 0
                    completed += 1
    
    # Calculate and display results
    total_wt = 0
    total_tt = 0
    
    print("\n" + "=" * 50)
    print("Round Robin Scheduling Results:")
    print("=" * 50)
    print("PID\tBurst Time\tWaiting Time\tTurnaround Time")
    print("-" * 60)
    
    for pid, bt, wt, remaining in processes:
        tat = wt + bt
        total_wt += wt
        total_tt += tat
        print(f"{pid}\t{bt}\t\t{wt}\t\t{tat}")
    
    # Display Gantt Chart
    print("\nGantt Chart:")
    print("Time: ", end="")
    for pid, start, end in gantt_chart:
        print(f" [{start}-{pid}-{end}] ", end="")
    print()
    
    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tt / n:.2f}")

# Standalone execution
if __name__ == "__main__":
    print("CPU SCHEDULING ALGORITHMS SIMULATION")
    print("1. Priority Scheduling")
    print("2. Round Robin Scheduling")
    print("3. Both Algorithms")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == '1':
        priority_scheduling()
    elif choice == '2':
        round_robin_scheduling()
    elif choice == '3':
        priority_scheduling()
        round_robin_scheduling()
    else:
        print("Invalid choice!")

