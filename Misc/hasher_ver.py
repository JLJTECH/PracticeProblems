#!/usr/bin/env python3
'''
Hash generation and dupilcate checker.
'''
from os import listdir, getcwd
from os.path import isfile, join, normpath, basename
import hashlib

#Grab files and file path information
def get_files():
    current_path = normpath(getcwd())
    return [join(current_path, f) for f in listdir(current_path) if isfile(join(current_path, f))]

#Generate file hashes
def get_hashes():
    files = get_files()
    list_of_hashes = []
    for each_file in files:
        hash_sha = hashlib.sha256()
        with open(each_file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha.update(chunk)
        list_of_hashes.append('Filename: {}\tHash: {}\n'.format(basename(each_file), hash_sha.hexdigest()))
    return list_of_hashes

#Write list of hashes to file
def write_hashes():
    hashes = get_hashes()
    
    #Sanity check
    print(hashes)
    """
    with open('list_of_hashes.txt', 'w') as f:
        for sha in hashes:
            f.write(sha)
    """

if __name__ == '__main__':
    write_hashes()
