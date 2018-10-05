import json
import socket
import sys

MY_TEST_CASES = 8

def clientSide():
    if len(sys.argv) != 2:
        print ("Usage:-\npython2 clientCheck.py <port-number>\n")
        return

    testInFile = open("testCases.txt", "r")
    expectedOutput = open("expectedOutput.txt", "r")

    port = int(sys.argv[1])
    sockt = socket.socket()
    sockt.connect(("localhost", port))
    socktFile = sockt.makefile()

    testNum = 1
    passed = True
    while True:
        testCase = testInFile.readline()

        if len(testCase) < 5:	# each test case is at least 5 characters long; break if not.
            break
        if testCase[-1] != "\n":
        	testCase += "\n"

        exp = json.loads(expectedOutput.readline())
        sockt.sendall(testCase)

        response = json.loads(socktFile.readline())

        if response != exp:
            if passed:
                print("The code failed for the following test cases:-")
                passed = False
            print(testNum)

        if testNum == MY_TEST_CASES:
        	choice = raw_input("The code passed all my test cases.\nDo you want to check with sir's test cases? (Y/N): ")
        	if choice == 'N' or choice == 'n':
        		break
        testNum += 1

    sockt.send(b"0\n")
    testInFile.close()
    expectedOutput.close()
    socktFile.close()
    sockt.close()

    for i in range(2):		# simulate two other clients connecting to the server and then exit.
	    sockt = socket.socket()
	    sockt.connect(("localhost", port))
	    sockt.send(b"0\n")
	    sockt.close()

    if passed:
        print("The code passed all the test cases!\n")

clientSide()
