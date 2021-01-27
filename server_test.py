"""All the logic for commands does in this class"""
import os
import unittest
from server_file import Server

class Tester(unittest.TestCase):
    """This class test with given inputs to perform unittest.
    Methods
    -----------
    test_create_folder(self):
        tests the given input with user input and checks for all success and failure cases
        of creating folder.
    test_change_folder(self):
        tests the given input with user input and checks for all success and failure cases
        of changing folder.
    test_read_from_file(self):
        tests the given input with user input and checks for all success and failure cases
        of reading from a file.
    test_write_file(self):
        tests the given input with user input and checks for all success and failure cases
        of writing into text file.
    """
    def test_create_folder(self):
        """tests the given input with user input and checks for all success and failure cases
        of creating folder."""
        test = Server()
        inputs = [['create_folder','oook'],['create_folder','oook']]
        response = ['folder created','Folder already exists. Try with another folder name']
        res = []
        for val in inputs:
            res.append(test.create_folder(val))
        self.assertListEqual(res, response)

    def test_change_folder(self):
        """ tests the given input with user input and checks for all success and failure cases
        of changing folder."""
        test = Server()
        test.user_name = 'andy'
        test.cur_dir = os.getcwd()
        test.root_dir = os.getcwd()
        inputs = [['change_folder', 'andy'], ['change_folder', 'name'],
        ['change_folder', 'name'],['change_folder', 'name'],['change_folder', '..'],
        ['change_folder', '..'],['change_folder', '..'],['change_folder', '..'] ]
        path = os.path.join(os.getcwd(), test.user_name)
        path1 = os.path.join(path, 'name')
        path2 = os.path.join(path1, 'name')
        path0 = os.path.join(path2, 'name')
        path3 = os.path.normpath(path2 + os.sep + os.pardir)
        path4 = os.path.normpath(path3 + os.sep + os.pardir)
        path5 = os.path.normpath(path4 + os.sep + os.pardir)
        paths = [path, path1, path2, path0, path3, path4, path5]
        response = ['Directory is changed to {}'.format(paths[0]),
        'Directory is changed to {}'.format(paths[1]),
        'Directory is changed to {}'.format(paths[2]),
        'folder is not found',
        'Directory is changed to {}'.format(paths[4]),
        'Directory is changed to {}'.format(paths[5]),
        'Directory is changed to {}'.format(paths[6]), 'access denied']
        #print(response)
        res = []
        for val in inputs:
            res.append(test.change_folder(val))
        self.assertListEqual(res, response)

    def test_read_from_file(self):
        """tests the given input with user input and checks for all success and failure cases
        of reading from a file."""
        test = Server()
        test.cur_dir = os.getcwd()
        inputs = [['read_file', 'test_file.txt'],
        ['read_file', 'test_file.txt'],
        ['read_file', None],
        ['read_file', 'test_file.txt'] ]
        response = ['Hello, this is a test file.',
        'Message:The file is read completely. Nothing more to read from this file',
        'name of the file should be given',
        'Hello, this is a test file.']
        res = []
        for val in inputs:
            res.append(test.read_from_file(val))
        # print("****************************************")
        # print(res)
        self.assertListEqual(res, response)

    def test_write_file(self):
        """tests the given input with user input and checks for all success and failure cases
        of writing into text file."""
        test = Server()
        test.cur_dir = os.getcwd()
        inputs = [['write_file', 'test_file1.txt', 'Hello world'],
        ['write_file', 'test_file2.txt', 'Hello world'],
        ['write_file', 'test_file1.txt']]
        response = ['written successfully',
        'file created and written successfully',
        'contents erased successfully']
        res = []
        for val in inputs:
            res.append(test.write_file(val))
        self.assertListEqual(res, response)

if __name__ == '__main__':
    unittest.main()
