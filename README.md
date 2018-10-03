# NS-SocketServer-TestCases
NOTE:-
1) These are sir's test cases and hence are pretty long.
2) You may face a problem while copy-pasting these test cases in your terminal. The strings are so long that for some weird reason, the entire string is not passed to the server; because of which you may get the following error on your server terminal:-\
`ValueError: No JSON object could be decoded`
3) So, you may have to copy-paste each test case to your source file and then check whether your output matches the expected output.
4) A program can be written to automate the whole process of sending the test cases to the server program and then comparing it with the expected output; but I don't have enough time to do so. Maybe one of the others who have already completed can do this.
5) So, you will have to manually compare your output with the expected output.
6) Since the JSON string is a dictionary, your output may differ in the order of the keys. The output is correct as long as the value corresponding to each key is correct. The order does not matter.
7) __TIP__ : A good way to compare outputs is to pick a key from the expected output, and check whether you have the same key-value pair in your output.
8) __DISCLAIMER__: These are not all the test cases that the autograder passes to your code. These are just 16 of the 50 test cases that my code had failed; and I could thus see them. Passing these test cases does not necessarily guarantee a 5/5; but there are high chances that you'll pass all the test cases if you pass all of these 16 test cases.
