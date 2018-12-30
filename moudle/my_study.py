from app import db


class SxCard(db.Model):
    __tablename__ = 'sx_by_year'

    hm = db.Column(db.String(16), primary_key=True)
    year = db.Column(db.String(16), primary_key=True)
    sx = db.Column(db.String(16))
    bs = db.Column(db.String(16))
    wx = db.Column(db.String(16))
    dx = db.Column(db.String(16))
    jy = db.Column(db.String(16))
    ds = db.Column(db.String(16))
    nn = db.Column(db.String(16))
    jx = db.Column(db.String(16))
    td = db.Column(db.String(16))
    yy = db.Column(db.String(16))
    hb = db.Column(db.String(16))
    sex = db.Column(db.String(16))
    wfx = db.Column(db.String(16))

    def __repr__(self):
        return '<SxCard %r>' % self.hm


class SpidersDate(db.Model):
    __tablename__ = 'spiders_record'

    id = db.Column(db.String(16), primary_key=True)
    qs = db.Column(db.String(16))
    year = db.Column(db.String(16))
    month = db.Column(db.String(16))
    day = db.Column(db.String(16))
    cc = db.Column(db.String(64))
    type = db.Column(db.String(16), primary_key=True)
    sx_card = db.Column(db.String(16))

    def __repr__(self):
        return '<SpidersDate %r>' % self.id


class HisRecord(db.Model):
    __tablename__ = 'lhc_result_record'

    id = db.Column(db.String(16),primary_key=True)
    year = db.Column(db.String(16))
    month = db.Column(db.String(16))
    day = db.Column(db.String(16))
    qs = db.Column(db.String(16))
    pm1 = db.Column(db.String(16))
    p1_sx = db.Column(db.String(16))
    pm2 = db.Column(db.String(16))
    p2_sx = db.Column(db.String(16))
    pm3 = db.Column(db.String(16))
    p3_sx = db.Column(db.String(16))
    pm4 = db.Column(db.String(16))
    p4_sx = db.Column(db.String(16))
    pm5 = db.Column(db.String(16))
    p5_sx = db.Column(db.String(16))
    pm6 = db.Column(db.String(16))
    p6_sx = db.Column(db.String(16))
    tm = db.Column(db.String(16))
    sx = db.Column(db.String(16))
    ds = db.Column(db.String(16))
    bs = db.Column(db.String(16))
    dx = db.Column(db.String(16))
    wx = db.Column(db.String(16))
    tt = db.Column(db.String(16))
    ws = db.Column(db.String(16))
    hds = db.Column(db.String(16))
    jy = db.Column(db.String(16))
    ms = db.Column(db.String(16))
    dw = db.Column(db.String(16))
    yy = db.Column(db.String(16))
    td = db.Column(db.String(16))
    jx = db.Column(db.String(16))
    hb = db.Column(db.String(16))
    sex = db.Column(db.String(16))
    bh = db.Column(db.String(16))
    nn = db.Column(db.String(16))
    zhds = db.Column(db.String(64))

    def __repr__(self):
        return '<HisRecord %r>' % self.id


if __name__ == '__main__':
    pass
