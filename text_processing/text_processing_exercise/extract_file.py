file_path = input()
folders = [el for el in file_path.split('\\')]
filename_and_ext = folders[len(folders) - 1]
ext = filename_and_ext[filename_and_ext.find('.') + 1::]
filename = filename_and_ext[:filename_and_ext.find('.'):]
print(f"File name: {filename}")
print(f"File extension: {ext}")


'''
TASK:
Write a program which reads the path to a file and subtracts the file name and its extension.
'''