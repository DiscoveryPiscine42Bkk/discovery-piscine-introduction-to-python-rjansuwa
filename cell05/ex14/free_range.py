import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("none")
        return
    if start <= end:
        free = list(range(start, end + 1))
    else:
        free = list(range(start, end -1, -1))
        print("free")

if __name__ =="__main__":
    main()