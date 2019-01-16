from common.tools import get_spiders_by_type, get_sx_info_by_year, get_list_tm_bingo_by_id_and_cc
from common._XXX_ import all_number
import time


def get_list_every_number_by_type(types, year, month):
    re = []
    if len(types) < 2:
        _single_list = get_spiders_by_type(types, year, month)
        _single_dict = {}
        for x in _single_list:
            _single_dict[x.id] = x.cc.split(',')
        re.append(_single_dict)
        return re

    if '0' in types:
        _30m_list = get_spiders_by_type('0', year, month)
        _30m_num_dict = {}
        for x in _30m_list:
            _30m_num_dict[x.id] = x.cc.split(',')
        re.append(_30m_num_dict)
    if '1' in types:
        _ws_list = get_spiders_by_type('1', year, month)
        _ws_num_dict = {}
        for x in _ws_list:
            _ws_num_dict[x.id] = get_list_number_by_ws(x.cc)
        re.append(_ws_num_dict)
    if '2' in types:
        _bs_list = get_spiders_by_type('2', year, month)
        _bs_num_dict = {}
        for x in _bs_list:
            _bs_num_dict[x.id] = get_list_number_by_bs(x.cc, x.sx_card)
        re.append(_bs_num_dict)
    if '3' in types:
        _7x_list = get_spiders_by_type('3', year, month)
        _7x_num_dict = {}
        for x in _7x_list:
            _7x_num_dict[x.id] = get_list_number_by_7x(x.cc, x.sx_card)
        re.append(_7x_num_dict)
    if '4' in types:
        _3t_list = get_spiders_by_type('4', year, month)
        _3t_num_dict = {}
        for x in _3t_list:
            _3t_num_dict[x.id] = get_list_number_by_3t(x.cc)
        re.append(_3t_num_dict)
    return re


def get_list_number_by_ws(cc):
    re = []
    for x in all_number:
        _yu = int(x) % 10
        if str(_yu) in cc:
            re.append(x)
    return re


def get_list_number_by_bs(cc, year):
    re = []
    for x in get_sx_info_by_year(year):
        if x.bs in cc:
            re.append(x.hm)
    return re


def get_list_number_by_7x(cc, year):
    re = []
    for x in get_sx_info_by_year(year):
        if x.sx in cc:
            re.append(x.hm)
    return re


def get_list_number_by_3t(cc):
    re = []
    for x in all_number:
        if x[0] in cc:
            re.append(x)
    return re


def get_list_same_num_by_type(types, year, month):
    re = []
    _every_number_list = get_list_every_number_by_type(types, year, month)
    _cur_list_size = len(_every_number_list)
    rightSize = 0
    for _id in _every_number_list[0].keys():
        ps_result = []
        for x in _every_number_list[0].get(_id):
            is_set = True
            for xx in range(1, _cur_list_size):
                if _every_number_list[xx].get(_id):
                    if x not in _every_number_list[xx].get(_id):
                        is_set = False
                        break
                else:
                    is_set = False
                    break
            if is_set:
                ps_result.append(x)
        if ps_result:
            tmp = get_list_tm_bingo_by_id_and_cc(_id, ps_result)
            re.append({'id': _id, 'cc': ps_result, 'tm': tmp[0], 'bingo': tmp[1], 'info': tmp[2]})
            if tmp[1]:
                rightSize += 1

    if not re[0]['tm']:
        re[0]['tm'] = round(rightSize/len(re)*100, 2)
    return re


if __name__ == '__main__':
    start_time = time.time()
    t = '1'
    print(get_list_same_num_by_type(t))

    print("used time: {}s".format(round(time.time() - start_time, 2)))
    pass

