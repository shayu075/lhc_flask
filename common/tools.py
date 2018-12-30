from moudle.my_study import SxCard, SpidersDate
import pymysql


def get_sx_info_by_year(year):
    print('================sx_by_year开始请求%s数据=================' % (year,))
    sql = 'select * from sx_by_year where year = ' + year

    return select_turn_class_by_sql(SxCard, sql)


def get_spiders_by_type(_type):
    print('================spiders_record开始请求%s数据=================' % (_type,))
    sql = 'select * from spiders_record where type = ' + _type

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


if __name__ == '__main__':
    for x in get_spiders_by_type('0'):
        print(x.id)
    pass

