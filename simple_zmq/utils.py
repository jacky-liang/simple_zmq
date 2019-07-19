from pickle import loads, dumps

def msg_to_data(msg):
    msg = eval(msg)
    try:
        data = loads(msg)
    except:
        data = loads(msg.encode('latin1'), encoding='latin1')

    return data

def data_to_msg(data):
    return repr(dumps(data, protocol=2))