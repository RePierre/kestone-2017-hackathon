#!/usr/bin/env python3


class MeshRecord:
    def __init__(self):
        self.rectype = None
        self._mh = None
        self._aq = []
        self._entries = []
        self._mn = None
        self._pa = []
        self._mh_th = []
        self._st = []
        self._n1 = None
        self._rn = None
        self._rr = None
        self._an = None
        self._pi = []
        self._ms = None
        self._ol = None
        self._pm = None
        self._hn = None
        self._mr = None
        self._da = None
        self._dc = None
        self._dx = None
        self._ui = None
        self._print_entry = None
        self._ec = []

    @property
    def rectype(self):
        return self._rectype

    @rectype.setter
    def rectype(self, value):
        self._rectype = value

    @property
    def mh(self):
        return self._mh

    @mh.setter
    def mh(self, value):
        self._mh = value

    @property
    def aq(self):
        return self._aq

    @property
    def entries(self):
        return self._entries

    @property
    def mn(self):
        return self._mn

    @mn.setter
    def mn(self, value):
        self._mn = value

    @property
    def pa(self):
        return self._pa

    @property
    def mh_th(self):
        return self._mh_th

    @property
    def st(self):
        return self._st

    @property
    def n1(self):
        return self._n1

    @n1.setter
    def n1(self, value):
        self._n1 = value

    @property
    def rn(self):
        return self._rn

    @rn.setter
    def rn(self, value):
        self._rn = value

    @property
    def rr(self):
        return self._rr

    @rr.setter
    def rr(self, value):
        self._rr = value

    @property
    def an(self):
        return self._self.an

    @an.setter
    def an(self, value):
        self._an = value

    @property
    def pi(self):
        return self._pi

    @property
    def ms(self):
        return self._ms

    @ms.setter
    def ms(self, value):
        self._ms = value

    @property
    def ol(self):
        return self._ol

    @ol.setter
    def ol(self, value):
        self._ol = value

    @property
    def pm(self):
        return self._pm

    @pm.setter
    def pm(self, value):
        self._pm = value

    @property
    def hn(self):
        return self._hn

    @hn.setter
    def hn(self, value):
        self._hn = value

    @property
    def mr(self):
        return self._mr

    @mr.setter
    def mr(self, value):
        self._mr = value

    @property
    def da(self):
        return self._da

    @da.setter
    def da(self, value):
        self._da = value

    @property
    def dc(self):
        return self._dc

    @dc.setter
    def dc(self, value):
        self._dc = value

    @property
    def dx(self):
        return self._dx

    @dx.setter
    def dx(self, value):
        self._dx = value

    @property
    def ui(self):
        return self._ui

    @ui.setter
    def ui(self, value):
        self._ui = value

    @property
    def print_entry(self):
        return self._print_entry

    @print_entry.setter
    def print_entry(self, value):
        self._print_entry = value

    @property
    def ec(self):
        return self._ec


class MeshRecordParser:
    def __init__(self):
        self._parse_map = {
            'RECTYPE': parse_rectype,
            'MH': parse_mh,
            'AQ': parse_aq,
            'ENTRY': parse_entry,
            'MN': parse_mn,
            'PA': parse_pa,
            'MH_TH': parse_mh_th,
            'ST': parse_st,
            'N1': parse_n1,
            'RN': parse_rn,
            'RR': parse_rr,
            'AN': parse_an,
            'PI': parse_pi,
            'MS': parse_ms,
            'OL': parse_ol,
            'PM': parse_pm,
            'HN': parse_hn,
            'MR': parse_mr,
            'DA': parse_da,
            'DC': parse_dc,
            'DX': parse_dx,
            'UI': parse_ui,
            'PRINT ENTRY': parse_print_entry,
            'EC': parse_ec,
            'CATSH': ignore,
            'DE': ignore,
            'FX': ignore,
            'DS': ignore,
            'RH': ignore,
            'CX': ignore
        }

    def parse(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line == "*NEWRECORD":
                    record = MeshRecord()
                    continue
                if len(line) == 0:
                    yield record
                    continue
                line_header = self.get_line_header(line)
                if not line_header.isupper():
                    continue
                parser = self._parse_map[line_header]
                parser(line, record)

    def get_line_header(self, line):
        parts = line.split('=')
        header = parts[0].strip()
        return header


def parse_rectype(line, record):
    record.rectype = line.replace('RECTYPE = ', '')


def parse_mh(line, record):
    record.mh = line.replace('MH = ', '')


def parse_aq(line, record):
    values = line.replace('AQ = ', '')
    record.aq.extend(values.split())


def parse_entry(line, record):
    value = line.replace('ENTRY = ', '')
    record.entries.append(value)


def parse_mn(line, record):
    record.mn = line.replace('MN = ', '')


def parse_pa(line, record):
    value = line.replace('PA = ', '')
    record.pa.append(value)


def parse_mh_th(line, record):
    value = line.replace('MH_TH = ', '')
    record.mh_th.append(value)


def parse_st(line, record):
    value = line.replace('ST = ', '')
    record.st.append(value)


def parse_n1(line, record):
    record.n1 = line.replace('N1 = ', '')


def parse_rn(line, record):
    record.rn = line.replace('RN = ', '')


def parse_pi(line, record):
    record.pi.append(line.replace('PI = ', ''))


def parse_ms(line, record):
    record.ms = line.replace('MS = ', '')


def parse_ol(line, record):
    record.ol = line.replace('OL = ', '')


def parse_pm(line, record):
    record.pm = line.replace('PM = ', '')


def parse_hn(line, record):
    record.hn = line.replace('HN = ', '')


def parse_mr(line, record):
    record.mr = line.replace('MR = ', '')


def parse_da(line, record):
    record.da = line.replace('DA = ', '')


def parse_dc(line, record):
    record.dc = line.replace('DC = ', '')


def parse_dx(line, record):
    record.dx = line.replace('DX = ', '')


def parse_ui(line, record):
    record.ui = line.replace('UI = ', '')


def parse_rr(line, record):
    record.rr = line.replace('RR = ', '')


def parse_an(line, record):
    record.an = line.replace('AN = ', '')


def parse_print_entry(line, record):
    record.print_entry = line.replace('PRINT ENTRY = ', '')


def parse_ec(line, record):
    value = line.replace('EC = ', '')
    record.ec.append(value)


def ignore(line, record):
    pass
