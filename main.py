def parallel_processing(n, m, data):
    output = []
    thread = [0] * n
    for i in range(m):
        in_thread = thread.index(min(thread))
        output.append((in_thread, thread[in_thread]))
        thread[in_thread] += data[i]
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for thri, start in result:
        print(thri, start)

if __name__ == "__main__":
    main()
