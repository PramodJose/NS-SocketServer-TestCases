# NS-SocketServer-TestCases

### How to use grader.py
1) **Prerequisites**:\
Download the files _grader.py_, _testCases.txt_ and _expectedOutput.txt_. These files must be in the same directory. Ensure that you have Python2 installed on your system.
2) **Verifying your code**:\
Open a terminal, navigate to the folder where you have saved your server program and start it by typing:-

   `python server.py port-number`\
   Eg: `python server.py 64000`
      
   Open a second terminal, navigate to the directory where you have downloaded _grader.py_, _testCases.txt_ and _expectedOutput.txt_. Start it by typing:-
      
   `python grader.py port-number`\
Note: The _"port-number"_ should be the same as the one you mentioned when you started your server program. In our example, your command would be:-

    `python grader.py 64000`
    
    After this, both _grader.py_ and your server program should exit cleanly. The grader would show a message mentioning whether your code successfully passed all the test cases or not. If you get a message saying `The code failed for the following test cases:-`, then you would also be shown the test case numbers which your program failed.\
	The first test case is on the first line of the file _testCases.txt_, the second test case on the second line and so on. Try debugging your code with the test case(s) for which your solution failed.


NOTE:-
1) These are sir's test cases and hence are pretty long.
2) You may face a problem while copy-pasting these test cases in your terminal. The strings are so long that for some weird reason, the entire string is not passed to the server; because of which you may get the following error on your server terminal:-\
`ValueError: No JSON object could be decoded`
Hence, it is recommended that you use _grader.py_ to verify your output.
3) Since the JSON string is a dictionary, your output may differ in the order of the keys. The output is correct as long as the value corresponding to each key is correct. The order does not matter.
4) __TIP__ : A good way to manually compare outputs is to pick a key from the expected output, and check whether you have the same key-value pair in your output. Doing this the other way round may result in you overlooking any key-value pairs that maybe missing in your output.
5) __DISCLAIMER__: These are not all the test cases that the autograder passes to your code. These are just 16 of the 50 test cases that my code had failed; and I could thus see them. Passing these test cases does not necessarily guarantee a 5/5; but there are high chances that you'll pass all the test cases if you pass all of these 16 test cases.
