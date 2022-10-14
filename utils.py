from flask_restx import abort


def build_query(cmd, val, file_list):
    try:
        if cmd == 'filter':
            res = filter(lambda x: val in x, file_list)
            return res
    except:
        return abort(400)

    try:
        if cmd == 'map':
            val = int(val)
            res = [x.split()[val] for x in file_list]
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
            res = sorted(file_list, reverse=reverse)
            return res
    except:
        return abort(400)

    try:
        if cmd == 'limit':
            val = int(val)
            res = list(file_list[:val])
            return res
    except:
        return abort(400)
