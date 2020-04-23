prompt="\nTell me something, and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program. "
message="quite"
while message!='quite':
    message=input(prompt)
    print(message)

prompt="\nTell me something, and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program. "
active=True
while active:
    message=input(prompt)
    if message=='quite':
        active=False
    else:
        print(message)