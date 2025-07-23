import sys

def main():
    if len(sys.argv) != 2:
        print("none")

    text = sys.argv[1]
    countA = text.count('A')

    if countA == 0:
        print("none")
    else:
        print('A' * countA)

if __name__ == "__main__":
    main()