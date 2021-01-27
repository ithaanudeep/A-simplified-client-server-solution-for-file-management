""" Client is connected to server here"""
import asyncio

def login():
    """Method for login"""
    print("****Login****")
    u_name = input('Enter username: ')
    password = input('Enter password: ')
    details = str(f'l {u_name} {password}')
    return details

def register():
    """Method for user registration"""
    print("****Register****")
    u_name = input('Enter username: ')
    password = input('Enter password: ')
    details = str(f'r {u_name} {password}')
    print(details)
    return details


async def tcp_echo_client(message):
    """Here, the connction will be established"""
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    # writer.write(message.encode())
    #await writer.drain()
    while True:
        print("Enter your choice")
        print("1 for register")
        print("2 for login")
        try:
            input_val = int(input('Enter your choice:'))
        except ValueError:
            print("enter only integer number")
            continue
        if input_val == 1:
            goto = register()
            writer.write(goto.encode())
        elif input_val == 2:
            goto = login()
            writer.write(goto.encode())
        else:
            print("invalid input")
            continue
        data = await reader.read(10000)
        message1 = data.decode()
        #print(message1)
        if message1 == 'success':
            print('user registered successfully')
            break
        if message1 == 'successfully logedin':
            print('user logedin successfully')
            break
        if message1 == 'Invalid credentials':
            print('Error: login failed due to Invalid credentials')
            continue
        if message1 == 'exist':
            print('user already exists')
            continue
        if message1 == 'user already logedin':
            print('user already logedin')
            continue
        if message1 == 'invalid command':
            print('invalid command')

    while True:
        ans = input('enter your request:')
        if ans == 'quit':
            writer.write(ans.encode())
            break
        elif ans == 'commands':
            files = open("commands.txt", "r")
            print(files.read())
            files.close()
            continue
        elif ans == '':
            continue
        else:
            writer.write(ans.encode())
            data1 = await reader.read(10000)
            print(f'{data1.decode()}')
            continue
    print('close the connection')
    writer.close()

        #await writer.drain()

    # data = await reader.read(100)
    # print(f'Received: {data.decode()!r}')

    #print('Close the connection')
    #writer.close()
    await writer.wait_closed()
try:
    asyncio.run(tcp_echo_client('connection successful'))
except ConnectionRefusedError:
    print("Connection failed")
