import sys

# Check for arguments
if len(sys.argv) > 1:
    print("You gave me an argument")
    print("Print argument with index 0:", sys.argv[0])
    print("Print argument with index 1:", sys.argv[1])
else:
    print("You gave me no argument")
    print("Print argument with index 0:", sys.argv[0])
