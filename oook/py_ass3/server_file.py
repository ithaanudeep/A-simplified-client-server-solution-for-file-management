""" Recieves input from user and performs methods based on input"""
import os
import datetime
import time
from os import scandir

class Server():
    """
    A class to perform all the logic for entered commands by the user

    ...

    Attributes
    ----------
    message : str
        Its stores the user entered command
    user_name : str
        It stores the entered user name by the user
    password : str
        Its tores the user entered password
    root_dir : str
        It stores the root directory
    cur_dir : str
        It stores the current directory. It can be changed when user is regisered
        and if user performs some actions
    start_point : int
        It is the indicator from where the charecters are read from the file when user
        entered read_file command
    end_point : int
        It is the indicator from where the charecters reading stopped from the file when user
        entered read_file command
    val : int
        If val is 0, he needs to login/register. Once he/she logedin/registered
        val becomes 1 and never can be logedin
        again until he quit

    Methods
    -------
    split_details(self, split_list):
    Takes the message and splits them into a list of items. Based on the message
    it moves to another method

    reg_log(self,split_list):
    User gets registered and logedin or just logedin based on their command

    user_folder(self, split_list):
    The directory changes to user folder when he gets registered

    create_folder(self, split_list):
    A new folder is created in this method

    display_list(self, split_list):
    The list of all files and folders present in that directory will be listed here

    read_from_file(self, split_list):
    The contents will be read from file upto 100 charecters

    write_file(self, split_list):
    The given user input will be written over the file which is mentioned by user

    change_folder(self, split_list):
    The directory will be changed to another directory, which is given by the user,
    the folder must be present in the same directory

    welcome_file(self, directory):
    The file is created when a user is registered, inside the user folder,
    with the content of welcoming the user

    new_class(self, split_list):
    Here, the registration is completed and the login details will be sent to reg_log
    method, to log the user.

    get_uname(self, split_list):
    This method checks, whether the username is same or not. If same, returns
    "User is already exists"

    loginlog_class(self, u_name):
    This method checks, whether the current user is previously logedout or not.

    remove_user(self):
    This method removes user from loginlog file, when he entered quit command.
    The user logs out.

    """
    def __init__(self):
        """ Initializes all the rquired attributes for this program
        """
        self.message = ''
        self.user_name = ''
        self.password = ''
        self.root_dir = os.getcwd()
        self.cur_dir = ''
        self.start_point = -100
        self.end_point = 0
        self.val = 0

    def split_details(self, message):
        """
            The messgage is splitted and it will move to next methods based on given
            command by user.
            parameters
            ---------------
            message : The message or command given by the user
        """
        self.message = message
        split_list = self.message.split(' ', 2)
        if self.val == 0:
            if split_list[0] == 'r' or split_list[0] == 'l':
                self.val = 1
                # self.user_name = split_list[1]
                # self.password = split_list[2]
                if split_list[0] == 'r':
                    try:
                        res = self.new_class(split_list)
                        assert res is not None
                    except AssertionError:
                        res = 'Something went wrong'
                    except:
                        res = 'error occured'
                    return res
                if split_list[0] == 'l':
                    try:
                        res = self.reg_log(split_list)
                        assert res is not None
                    except AssertionError:
                        res = 'something went wrong'
                    except:
                        res = 'error occured'
                    return res

        if split_list[0] == 'create_folder':
            try:
                res = self.create_folder(split_list)
                assert res is not None
            except AssertionError:
                res = 'something went wrong'
            except:
                res = 'error occured'
            return res
        if self.message == 'list':
            try:
                res = self.display_list()
                assert res is not None
            except AssertionError:
                res = 'something went wrong'
            except:
                res = 'error occured'
            return res
        if split_list[0] == 'read_file':
            try:
                res = self.read_from_file(split_list)
                assert res is not None
            except AssertionError:
                res = 'something went wrong'
            except:
                res = 'error occured'
            return res
        if split_list[0] == 'write_file':
            try:
                res = self.write_file(split_list)
                assert res is not None
            except AssertionError:
                res = 'something went wrong'
            except:
                res = 'error occured'
            return res
        if split_list[0] == 'change_folder':
            try:
                res = self.change_folder(split_list)
                assert res is not None
            except AssertionError:
                res = 'something went wrong'
            except:
                res = 'error occured'
            return res
        return 'invalid command'

    def reg_log(self, split_list):
        """
            The user gets registered and logedin or just login based on
            command by user.
            parameters
            ---------------
            split_list : The list of containing command that is splitted.
        """
        val = split_list[0]
        try:
            self.user_name = split_list[1]
            self.password = split_list[2]
        except IndexError:
            return 'Enter username and password'
        if val == 'r':
            file_name = str(f'{self.root_dir}\\reglog.txt')
            file = open(file_name, "a+")
            user_data = str(f'\n{split_list[1]},{split_list[2]}')
            file.writelines(user_data)
            file.close()
            self.user_folder()
            return 'success'
        if val == 'l':
            check = str(f'{split_list[1]},{split_list[2]}')
            a_file = open("reglog.txt","r")
            for line in a_file:
                line1 = line.strip()
                if line1 == check:
                    #print('ok11')
                    ans = self.loginlog_class(split_list[1])
                    if ans:
                        self.val = 0
                        return 'user already logedin'
                    file_name = str(f'{self.root_dir}\\loginlog.txt')
                    file = open(file_name, "a+")
                    user_data = str(f'\n{split_list[1]}')
                    file.writelines(user_data)
                    file.close()
                    # self.user_folder(split_list)
                    self.cur_dir = os.path.join(self.root_dir, self.user_name)
                    os.chdir(self.cur_dir)
                    print(os.getcwd())
                    return 'successfully logedin'
            else:
                self.val = 0
                return "Invalid credentials"
            a_file.close()

    def user_folder(self):
        """
            A new folder is created in the name of user that is registered.
            The directory also will be moved.
        """
        directory = os.path.join(self.root_dir, self.user_name)
        os.mkdir(directory)
        self.cur_dir = directory
        self.welcome_file(directory)

    def create_folder(self, split_list):
        """
            A new folder is created in the name that is given by the logedin user.
            The directory also will not be moved.
            parameters
            ---------------
            split_list : The list of containing command that is splitted.
        """
        try:
            folder_dir = os.path.join(self.cur_dir,split_list[1])
            if os.path.exists(folder_dir):
                return 'Folder already exists. Try with another folder name'
            os.mkdir(folder_dir)
            return 'folder created'
        except IndexError:
            return 'Name of the folder must be provided'

    def display_list(self):
        """
            A list of all the files and folders will be displayed in the current directory
            parameters
        """
        path = self.cur_dir
        dire = path
        dir_entries = scandir(dire)
        res = ''
        for entry in dir_entries:
            info = entry.stat()
            cee = datetime.datetime.strptime(time.ctime(info.st_mtime), "%a %b %d %H:%M:%S %Y")
            byte = os.stat(entry).st_size
        # print(f'{entry.name}\t Last Modified: {cee}\t size: {byte} bytes')
            res += str('{:20s}\t {:10} bytes\t {}\n'.format(entry.name, byte, cee))
        return res

    def read_from_file(self, split_list):
        """
           Read data from the file <name> in the current working directory for the user
           issuing the request and return the first hundred characters in it.
           Each subsequent call by the same client is to return the next hundred characters
           in the file, up until all characters are read. If a file with the specified
           <name> does not exist in the current working directory for the user, the request
           is to be denied with a proper message highlighting the error for the user.

            parameters
            ---------------
            split_list : The list of containing command that is splitted.
        """
        try:
            path = os.path.join(self.cur_dir, split_list[1])
        except IndexError:
            self.start_point = -100
            self.end_point = 0
            return 'name of the file should be given'
        except Exception:
            self.start_point = -100
            self.end_point = 0
            return 'name of the file should be given'
        print(path)
        #if split_list[1] != 'None'
        if os.path.exists(path):
            #print('ok')
            # self.start_point = self.start_point + 100
            # self.end_point = self.end_point + 100
            files = open(str(f'{self.cur_dir}\\{split_list[1]}'), 'r')
            val= files.read()
            files.close()
            if len(val) == self.end_point:
                return 'Message:The file is read completely. Nothing more to read from this file'
            if (len(val)-self.end_point) <= 100 :
                self.start_point = self.start_point + 100
                self.end_point = len(val)
                return str(val[self.start_point:len(val)])
            if (len(val)-self.end_point) >100 :
                self.start_point = self.start_point + 100
                self.end_point = self.end_point + 100
                return str(val[self.start_point:self.end_point])
            if len(val) == self.end_point:
                return 'Message:The file is read completely. Nothing more to read from this file'
        return 'The file of name {} doesnot exist'.format(split_list[1])


    def write_file(self, split_list):
        """
            Write the data in <input> to the end of the file <name> in the current working directory
            for the user issuing the request, starting on a new line.  If no file exists with
            the given <name>, a new file is to be created in the current working directory
            for the user.

            parameters
            ---------------
            split_list : The list of containing command that is splitted.
        """
        # try:
        #     if split_list[2] == None:
        #         return "no input given"
        # except Exception:
        #     return 'content in the file is cleared'
        try:
            path = os.path.join(self.cur_dir, split_list[1])
            if os.path.exists(path):
                files = open(str(f'{self.cur_dir}\\{split_list[1]}'), 'a')
                try:
                    u_data = [split_list[2], '\n']
                except IndexError:
                    files.seek(0)
                    files.truncate()
                    return 'contents erased successfully'
                files.writelines(u_data)
                files.close()
                return 'written successfully'
            file_name = str(f'{self.cur_dir}\\{split_list[1]}')
            files = open(file_name, "a+")
            try:
                u_data = [split_list[2], '\n']
            except IndexError:
                files.seek(0)
                files.truncate()
                return 'contents erased successfully'
            files.writelines(u_data)
            files.close()
            return 'file created and written successfully'
            #return 'The file of name {} doesnot exist'.format(split_list[1])
        except IndexError:
            return 'Name of the file must be provided'

    def change_folder(self, split_list):
        """
            Move the current working directory for the current user to the specified folder
            residing in the current folder. If the <name> does not point to a folder in the
            current working directory, the request is to be denied with a proper message
            highlighting the error for the user.

            parameters
            ---------------
            split_list : The list of containing command that is splitted.
        """
        # print('******************************************************')
        # print(self.user_name)
        try:
            if split_list[1] == '..':
                if self.cur_dir == self.root_dir:
                    return 'access denied'
            #change_dir = str(f'../{self.cur_dir}')
                os.chdir('../')
                self.cur_dir = os.getcwd()
                return 'Directory is changed to {}'.format(self.cur_dir)
        except IndexError:
            return 'Name of the folder must be provided'
        try:
            path = os.path.join(self.cur_dir, split_list[1])
            if os.path.exists(path) and self.cur_dir !=self.root_dir:
                self.cur_dir = path
                print(path)
                os.chdir(path)
                return 'Directory is changed to {}'.format(self.cur_dir)
            if os.path.exists(path) and self.cur_dir == self.root_dir:
                # print(split_list[1])
                # print(self.user_name)
                if split_list[1] == self.user_name:
                    self.cur_dir = path
                    print(path)
                    os.chdir(path)
                    return 'Directory is changed to {}'.format(self.cur_dir)
                return 'You cannot go to another User\'s folder'
            return 'folder is not found'
        except IndexError:
            return 'Name of the folder must be provided'

    def welcome_file(self, directory):
        """
            A new file is created in the folder of registered user with the name of log.txt
            parameters
            ---------------
            directory : The current directory of registered user.
        """
        file_open = open(str(f'{directory}\\log.txt'), "w")
        data = self.user_name
        display_data = "welcome {}".format(data)
        user_data = [display_data, "\n"]
        file_open.writelines(user_data)
        file_open.close()


            #stripped_line = line.strip()
    def new_class(self, split_list):
        """
            Here, the registration is completed and the login details will be sent to reg_log
            method, to log the user.
            parameters
            ---------------
            split_list : The list of containing command that is splitted.
        """
        # self.user_name = split_list[1]
        # self.password = split_list[2]
        res = self.get_uname(split_list)
        if res == 'exist':
            return res
        self.reg_log(split_list)
        split_list = ['l', self.user_name, self.password]
        res1 = self.reg_log(split_list)
        return res1

    def get_uname(self,split_list):
        """
            Here, it checks the username is already exists or not
            parameters
            ---------------
            split_list : The list of containing command that is splitted.
        """
        file = open("reglog.txt","r")
        for lines in file:
            line_strip = lines.strip()
            line_list = line_strip.split(',', 1)
            try:
                if line_list[0] == split_list[1]:
                    self.val = 0
                    return 'exist'
            except IndexError:
                return 'enter username and password'
        else:
            return 'ok'

    def loginlog_class(self, u_name):
        """
            Here, it checks whether the user is previously signedout or not.
            parameters
            ---------------
            u_name : The username given by user
        """
        read_file = open("loginlog.txt","r")
        for i in read_file:
            lines = i.strip()
            if lines == u_name:
                return True

    def remove_user(self):
        """
            The user willbe logedout, when he entered quit command
        """
        os.chdir(self.root_dir)
        with open ('loginlog.txt', 'r') as files:
            filedata = files.read()
        filedata = filedata.replace(self.user_name, '')
        with open ('loginlog.txt', 'w') as files:
            files.write(filedata)

        # f= open('loginlog.txt','r+')
        # for l in f:
        #     l1 = l.strip()
        #     print(self.user_name)
        #     if l1 == self.user_name:
        #         print('ok')
        #         l = l.replace(self.user_name, '')
        # # f.close()
