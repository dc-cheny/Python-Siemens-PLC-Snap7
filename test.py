import snap7
from snap7.util import *
from snap7.types import *


def read_memory(plc, byte, datatype, db_number=999):
    """ define read memory function
    """
    result = plc.read_area(Areas.DB, db_number, start=byte, size=datatype)
    if datatype == S7WLBit:
        return get_bool(result, 0, 1)
    elif datatype in (S7WLByte, S7WLWord):
        return get_int(result, 0)
    elif datatype == S7WLReal:
        return get_real(result, 0)
    elif datatype == S7WLDWord:
        return get_dword(result, 0)
    else:
        return None


def write_memory(plc, byte, bit, datatype, value, db_number=999):
    """ write memory function
    """
    result = plc.read_area(Areas.DB, db_number, start=byte, size=datatype)
    if datatype == S7WLBit:
        set_bool(result, byte_index=0, bool_index=bit, value=value)
    elif datatype in (S7WLByte, S7WLWord):
        set_int(result, byte_index=0, _int=value)
    elif datatype == S7WLReal:
        set_real(result, byte_index=0, real=value)
    elif datatype == S7WLDWord:
        set_dword(result, byte_index=0, dword=value)

    plc.write_area(Areas.DB, db_number, start=byte, data=result)


def main():
    IP = '192.168.1.10'
    RACK = 0
    SLOT = 1

    # connect
    plc_client = snap7.client.Client()
    plc_client.connect(IP, RACK, SLOT)
    state = plc_client.get_cpu_state()
    print('State: {}'.format(state))

    # test
    a, b, c = 0, 0, 0
    readbit = read_memory(plc_client, 2, S7WLBit)
    print(readbit)


if __name__ == '__main__':
    main()
