#!/usr/bin/env python3

import os

print("Hello from Docker\n")
print("Printing environmental variable that is set in DokcerFile")
print(f"VERSION: {os.environ['VERSION']}")
print("Whatever you write here will be written in a file inside docker container.")
text = input("Write your text: ")
with open('test.txt', 'w') as file:
	file.write(text)

print(f"A new text.txt file is created. Which contains \"{text} \". \n You can copy that file using docker cp command.")
print("For example: sudo docker cp [container_name]:/test.txt .")