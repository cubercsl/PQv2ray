import json
import logging
import re
from os import path
from typing import List, Tuple, Dict, Set, Union, Optional
from textwrap import dedent
from copy import deepcopy
from traceback import format_exc
import subprocess as subp
import shlex
from shutil import copy as copy_file

import psutil

logging.basicConfig(
    format="[%(module)s: %(lineno)d] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger('utils')


file_encoding = 'UTF-8'

def load_json(file :str):
    return json.loads(read_text_file(file))

def dump_json(obj, file :str):
    write_text_file(file, json.dumps(obj, ensure_ascii=False, indent=4))

def dump_jsons(obj):
    return json.dumps(obj, ensure_ascii=False, indent=4)

def read_text_file(file :str):
    try:
        with open(file, 'rt', encoding=file_encoding) as f:
            return f.read()
    except Exception as e:
        logger.error('Error opening file: \n' + repr(e))
        return ''

def write_text_file(file :str, text :str):
    with open(file, 'wt', encoding=file_encoding) as f:
        f.write(text)

def get_repr_mapping(node :'Node', **more):
    d = node.get_format_dict()
    d.update(more)
    # {
    #     "node.id": "udjeisuydjfk",
    #     "node.name": "Lv2. 香港01",
    #     "port": 3001,
    #     
    # }
    return d

# def format_repr(repr_str, d :dict):
#     result = repr_str
#     for k, v in d.items():
#         result = result.replace('{' + k + '}', str(v))
#     return result

def format_repr(repr_str, d :dict) -> str:
    result = repr_str
    for k, v in d.items():
        if '{' + k + '}' == repr_str:
            return v
        else:
            result = result.replace('{' + k + '}', str(v))
    return result

def format_json_obj(repr_obj, d):
    # print(repr_obj)
    if isinstance(repr_obj, list):
        return [format_json_obj(o, d) for o in repr_obj]
    elif isinstance(repr_obj, dict):
        return {format_repr(k, d): 
        format_json_obj(v, d) for k, v in repr_obj.items()}
    elif isinstance(repr_obj, str):
        return format_repr(repr_obj, d)
    else:
        return repr_obj

def deduplicate(l):
    return list(dict.fromkeys(l))


def process_exists(name :str):
    return name in (p.name() for p in psutil.process_iter())


def start_process(cmd :str):
    subp.Popen(
        args=shlex.split(cmd),
        start_new_session=True,
        creationflags=subp.CREATE_NEW_PROCESS_GROUP
    )

def kill_process(name):
    # TODO
    pass


if __name__ == '__main__':

    o = {
        "{port}": {
            'a': [
                {
                    "port": "{port}",
                    "node_group": "{node.group}",
                    "node_id": "{node.id}",
                }
            ]
        },
        "node_name": "{node.name}"
    }
    print(o)

    o = format_json_obj(o, {
        'port' : 3306,
        'node.id': 'ID\"123',
        'node.name': 'name\"123',
        'node.group': 'group\"123',
    })
    print(o)
