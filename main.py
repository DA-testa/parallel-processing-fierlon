def parallel_processing(n, m, data):
    output = []
    thread = [0] * n
    
    for i in range(m):
        in_thread = thread.index(min(thread))
        output.append((in_thread, thread[in_thread]))
        thread[in_thread] += data[i]
        
    return output

def main():
    text = input("F or I: ")

    if "I" in text:
        n, m = map(int, input().split())
        data = list(map(int, input().split()))

    elif "F" in text:
        file_name = input("Enter filename: ").strip()
        file_path='./tests/'
        file_full_name = file_path+file_name
        with open(file_full_name, "r") as f:
            n, m = map(int, f.readline().split())
            data = list(map(int, f.readline().split()))

    result = parallel_processing(n, m, data)
    for thri, start in result:
        print(thri, start)

if __name__ == "__main__":
    main()
