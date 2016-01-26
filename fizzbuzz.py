
import sys

def fizzbuzz(n):
    for i in range(1, 1 + int(n)):
        if i % 6 == 0:
            print "fizzbuzz"
        elif i % 2 == 0:
            print "fizz"
        elif i % 3 == 0:
            print "buzz"
        else:
            print i

def main():
    fizzbuzz(sys.argv[1])

if __name__ == "__main__":
    main()