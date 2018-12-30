from moudle.my_study import SxCard, SpidersDate
_sx_info = {}


def get_sx_info_by_year(year):
    if _sx_info.get(year):
        return _sx_info.get(year)

    print('================开始请求%s数据=================' % (year,))
    re = SxCard.query.filter_by(year=year).all()

    _sx_info[year] = re
    return _sx_info[year]


def get_spiders_by_type(_type):
    re = SpidersDate.query.filter_by(type=_type).all()
    return re





