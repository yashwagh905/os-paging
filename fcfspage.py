def fifo(incoming_stream, frames):
    page_faults = 0
    page_hits = 0
    pages = len(incoming_stream)
    temp = [-1] * frames
    queue = []
    index = 0
    
    print(" Incoming\t", end="")
    for i in range(frames):
        print(f"Frame {i+1}\t", end="")
    print("Page Hit/Fault")
    
    for m in range(pages):
        if incoming_stream[m] not in temp:
            if len(queue) < frames:
                temp[len(queue)] = incoming_stream[m]
                queue.append(incoming_stream[m])
                page_faults += 1
                page_status = "Page Fault"
            else:
                index %= frames
                index_to_replace = temp.index(queue[index])
                temp[index_to_replace] = incoming_stream[m]
                queue[index] = incoming_stream[m]
                index += 1
                page_faults += 1
                page_status = "Page Fault"
        else:
            page_status = "Page Hit"
            page_hits += 1
        
        print(f"{incoming_stream[m]}\t\t", end="")
        for n in range(frames):
            if temp[n] != -1:
                print(f"{temp[n]}\t\t", end="")
            else:
                print("-\t\t", end="")
        print(f"\t\t{page_status}")

    print(f"Total Page Faults: {page_faults}")
    print(f"Total Page Hits: {page_hits}")

def main():
    reference_string = list(map(int, input("Enter reference string separated by spaces: ").split()))
    frames = int(input("Enter the number of frames: "))
    
    print("\nFIFO Page Replacement Algorithm:")
    
    fifo(reference_string, frames)
    

if __name__ == "__main__":
    main()
