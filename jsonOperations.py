import json as __json
import os as __os
from typing import Any as __Any

__JOall__ = ['jsonFileRead', 'jsonFileWrite']

def jsonFileRead(fileName: __os.PathLike) -> dict:

    '''
    Open and read a JSON file
    '''
    if __os.path.exists(fileName):
        fileObject = open(fileName, 'r')
        return __json.load(fileObject)
    else:
        raise FileNotFoundError(f'No such file or directory: {fileName}')

def jsonFileWrite(fileName: __os.PathLike, data: __Any) -> None:

    '''
    Open and write in a JSON file, If file doesn't exist then creates new file and writes into it
    '''

    try:
        fileObject = open(fileName, 'w')
        __json.dump(data, fileObject)
    except Exception as e:
        raise e