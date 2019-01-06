from moudle.my_study import SxCard, SpidersDate
import pymysql

_sx_card = {}


def get_sx_info_by_year(year):
    if _sx_card.get(year):
        return _sx_card.get(year)
    print('================sx_by_year开始请求%s数据=================' % (year,))
    sql = 'select * from sx_by_year where year = ' + year

    _sx_card[year] = select_turn_class_by_sql(SxCard, sql)
    return _sx_card.get(year)


def get_spiders_by_type(_type):
    print('================spiders_record开始请求%s数据=================' % (_type,))
    sql = 'select * from spiders_record where type = ' + _type + ' order by id DESC'

    return select_turn_class_by_sql(SpidersDate, sql)


def select_turn_class_by_sql(T, sql):
    re = []
    db = pymysql.connect("localhost", "root", "123456", "my_study")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            re.append(T(row))
    except:
        print("Error: unable to fetch data")
    finally:
        db.close()
    return re


def get_list_tm_bingo_by_id_and_cc(id, cc):
    db = pymysql.connect("localhost", "root", "123456", "my_study")
    cursor = db.cursor()
    try:
        cursor.execute('select tm, ws, concat(bs, "波"), sx, tt from lhc_result_record where id = ' + id)
        result = cursor.fetchone()
        # 2波
        if len(cc) == 2:
            if result[2] in cc:
                return [result[2], True, {'tm': result[0], 'bs': result[2], 'sx': result[3]}]
        # 3头
        if len(cc) == 3:
            if result[4] in cc:
                return [result[4], True, {'tm': result[0], 'bs': result[2], 'sx': result[3]}]
        # 6尾
        if len(cc) == 6:
            if result[1] in cc:
                return [result[1], True, {'tm': result[0], 'bs': result[2], 'sx': result[3]}]
        # 7肖
        if len(cc) == 7:
            if result[3] in cc:
                return [result[3], True, {'tm': result[0], 'bs': result[2], 'sx': result[3]}]
        # 30码
        if result[0] in cc:
            return [result[0], True, {'tm': result[0], 'bs': result[2], 'sx': result[3]}]
        if result:
            return ['', False, {'tm': result[0], 'bs': result[2], 'sx': result[3]}]
    except:
        print("Error: unable to fetch data")
    finally:
        db.close()
    return ['', False, None]


if __name__ == '__main__':
    a = '1,2,3'
    b = '红波,蓝波'
    c = '1,3,4,5,7,8'
    d = '羊,狗,兔,龙,鸡,猴,马'
    e = '01,02,04,06,09,10,11,12,13,14,15,16,18,21,22,23,25,26,30,33,34,35,36,37,38,40,42,45,46,47'
    print(len(a))
    print(len(b))
    print(len(c))
    print(len(d))
    print(len(e))
    pass

