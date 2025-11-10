#!/usr/bin/env python3
"""
Task 4: Contiguous Memory Allocation Simulation
- First-fit, Best-fit, and Worst-fit strategies
"""

def allocate_memory(strategy, partitions, processes):
    """Allocate memory using specified strategy"""
    print(f"\n{strategy.upper()}-FIT STRATEGY:")
    print("-" * 40)
    
    # Create copies to avoid modifying original lists
    part_copy = partitions.copy()
    proc_copy = processes.copy()
    allocation = [-1] * len(proc_copy)
    
    print(f"Partitions: {part_copy}")
    print(f"Processes: {proc_copy}")
    print()
    
    for i, psize in enumerate(proc_copy):
        idx = -1
        
        if strategy == "first":
            # First-fit: allocate in first available partition that fits
            for j, part_size in enumerate(part_copy):
                if part_size >= psize:
                    idx = j
                    break
                    
        elif strategy == "best":
            # Best-fit: allocate in smallest sufficient partition
            best_fit = float("inf")
            for j, part_size in enumerate(part_copy):
                if part_size >= psize and part_size < best_fit:
                    best_fit = part_size
                    idx = j
                    
        elif strategy == "worst":
            # Worst-fit: allocate in largest sufficient partition
            worst_fit = -1
            for j, part_size in enumerate(part_copy):
                if part_size >= psize and part_size > worst_fit:
                    worst_fit = part_size
                    idx = j
        
        # Allocate if suitable partition found
        if idx != -1:
            allocation[i] = idx
            part_copy[idx] -= psize
            print(f"Process {i+1} (size {psize}) -> Allocated in Partition {idx+1}")
            print(f"  Remaining partition sizes: {part_copy}")
        else:
            print(f"Process {i+1} (size {psize}) -> Cannot be allocated")
    
    return allocation

def main():
    """Main function for memory allocation simulation"""
    print("=" * 50)
    print("CONTIGUOUS MEMORY ALLOCATION SIMULATION")
    print("=" * 50)
    
    # Input partitions
    partitions = list(map(int, input("Enter partition sizes (space-separated): ").split()))
    
    # Input processes
    processes = list(map(int, input("Enter process sizes (space-separated): ").split()))
    
    print(f"\nInitial Configuration:")
    print(f"Partitions: {partitions}")
    print(f"Processes: {processes}")
    
    # Run all three strategies
    strategies = ["first", "best", "worst"]
    
    for strategy in strategies:
        allocate_memory(strategy, partitions, processes)

# Standalone execution
if __name__ == "__main__":
    main()

