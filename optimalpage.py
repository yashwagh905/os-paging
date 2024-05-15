def optimal(incoming_stream, frames):
    page_faults = 0
    page_hits = 0
    pages = len(incoming_stream)
    temp = [-1] * frames
    page_indices = {}
    
    print(" Incoming\t", end="")
    for i in range(frames):
        print(f"Frame {i+1}\t", end="")
    print("Page Hit/Fault")
    
    for m in range(pages):
        if incoming_stream[m] not in temp:
            if len(page_indices) < frames:
                temp[len(page_indices)] = incoming_stream[m]
                page_indices[incoming_stream[m]] = [i for i, x in enumerate(incoming_stream) if x == incoming_stream[m]][1:]
                page_faults += 1
                page_status = "Page Fault"
            else:
                max_future_index = -1
                page_to_replace = temp[0]
                for page in temp:
                    if page not in incoming_stream[m:]:
                        page_to_replace = page
                        break
                    elif incoming_stream[m:].index(page) > max_future_index:
                        max_future_index = incoming_stream[m:].index(page)
                        page_to_replace = page
                index_to_replace = temp.index(page_to_replace)
                if page_to_replace in page_indices:
                    del page_indices[page_to_replace]
                temp[index_to_replace] = incoming_stream[m]
                page_indices[incoming_stream[m]] = [i for i, x in enumerate(incoming_stream) if x == incoming_stream[m]][1:]
                page_faults += 1
                page_status = "Page Fault"
        else:
            page_hits += 1
            page_status = "Page Hit"
            page_indices[incoming_stream[m]] = [i for i, x in enumerate(incoming_stream) if x == incoming_stream[m]][1:]
        
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
    
    print("\nOptimal Page Replacement Algorithm:")
    
    optimal(reference_string, frames)
    

if __name__ == "__main__":
    main()
