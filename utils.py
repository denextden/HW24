import re
from flask_restx import abort
from typing import Iterator, List, Any


def build_query(cmd: str, val: str, file_list: Iterator) -> List[Any]:
    try:
        if cmd == 'filter':
            res = list(filter(lambda x: val in x, file_list))
            return res
    except:
        return abort(400)

    try:
        if cmd == 'map':
            res = list([x.split()[int(val)] for x in file_list])
            return res
    except:
        return abort(400)

    try:
        if cmd == 'unique':
            res = list(set(file_list))
            return res
    except:
        return abort(400)

    try:
        if cmd == 'sort':
            reverse = val == 'desc'
            res = list(sorted(file_list, reverse=reverse))
            return res
    except:
        return abort(400)

    try:
        if cmd == 'limit':
            res = list(file_list)[:int(val)]
            return res
    except:
        return abort(400)

    if cmd == 'regex':
        regex = re.compile(val)
        res = list(filter(lambda x: regex.search(x), file_list))
        return res
    return []

