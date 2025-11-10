#!/usr/bin/env python3
"""
Task 5: MFT (Fixed Partition) and MVT (Variable Partition) Simulation
"""

def MFT_simulation():
    """MFT - Fixed Partitioning Simulation"""
    print("=" * 50)
    print("MFT (FIXED PARTITIONING) SIMULATION")
    print("=" * 50)
    
    mem_size = int(input("Enter total memory size: "))
    part_size = int(input("Enter partition size: "))
    
    # Calculate number of partitions
    num_partitions = mem_size // part_size
    internal_fragmentation = 0
    allocated_processes = 0
    
    print(f"\nMemory divided into {num_partitions} partitions of size {part_size} each")
    print(f"Total memory: {mem_size}, Usable memory: {num_partitions * part_size}")
    print(f"Memory lost to internal fragmentation: {mem_size - (num_partitions * part_size)}")
    
    n = int(input("\nEnter number of processes: "))
    
    print("\nProcess Allocation:")
    print("-" * 30)
    
    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))
        
        if psize <= part_size:
            print(f"  Process {i+1} (size {psize}) -> ALLOCATED")
            internal_fragmentation += (part_size - psize)
            allocated_processes += 1
        else:
            print(f"  Process {i+1} (size {psize}) -> TOO LARGE (Rejected)")
    
    print(f"\nSummary:")
    print(f"Total processes: {n}")
    print(f"Successfully allocated: {allocated_processes}")
    print(f"Total internal fragmentation: {internal_fragmentation}")
    print(f"Average internal fragmentation per partition: {internal_fragmentation/allocated_processes if allocated_processes > 0 else 0:.2f}")

def MVT_simulation():
    """MVT - Variable Partitioning Simulation"""
    print("\n" + "=" * 50)
    print("MVT (VARIABLE PARTITIONING) SIMULATION")
    print("=" * 50)
    
    mem_size = int(input("Enter total memory size: "))
    available_memory = mem_size
    external_fragmentation = 0
    allocated_processes = 0
    
    print(f"\nInitial available memory: {available_memory}")
    
    n = int(input("\nEnter number of processes: "))
    
    print("\nProcess Allocation:")
    print("-" * 30)
    
    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))
        
        if psize <= available_memory:
            print(f"  Process {i+1} (size {psize}) -> ALLOCATED")
            available_memory -= psize
            allocated_processes += 1
            print(f"    Remaining memory: {available_memory}")
        else:
            print(f"  Process {i+1} (size {psize}) -> INSUFFICIENT MEMORY (Rejected)")
    
    external_fragmentation = available_memory
    
    print(f"\nSummary:")
    print(f"Total processes: {n}")
    print(f"Successfully allocated: {allocated_processes}")
    print(f"Remaining memory (external fragmentation): {external_fragmentation}")
    print(f"Memory utilization: {(mem_size - external_fragmentation)/mem_size*100:.2f}%")

def main():
    """Main function for MFT and MVT simulation"""
    print("MEMORY MANAGEMENT TECHNIQUES SIMULATION")
    print("1. MFT (Fixed Partitioning)")
    print("2. MVT (Variable Partitioning)")
    print("3. Both Techniques")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == '1':
        MFT_simulation()
    elif choice == '2':
        MVT_simulation()
    elif choice == '3':
        MFT_simulation()
        MVT_simulation()
    else:
        print("Invalid choice!")

# Standalone execution
if __name__ == "__main__":
    main()

