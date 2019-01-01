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


def get_tuple_tm_bingo_by_id_and_cc(id, cc):
    db = pymysql.connect("localhost", "root", "123456", "my_study")
    cursor = db.cursor()
    try:
        cursor.execute('select tm, ws, concat(bs, "波"), sx from lhc_result_record where id = ' + id)
        result = cursor.fetchone()
        for x in result:
            if x in cc:
                return (x, True)
    except:
        print("Error: unable to fetch data")
    finally:
        db.close()
    return ('', False)


if __name__ == '__main__':
    pass

