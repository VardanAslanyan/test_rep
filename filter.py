import xlsxwriter
from pathlib import Path
import xlrd

work_dir = Path.home()
loc = work_dir.joinpath('Desktop/python/invoices_24122020.xls')


def readxls():
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(1, sheet.nrows):
        f = float(sheet.cell_value(i, 14))
        yield sheet.cell_value(i, 13), f


def createdict():
    d = {}
    for k, v in readxls():
        if d.get(k) is not None:
            d[k] += v
        d.setdefault(k, v)
    b = {n: d[n] for n in d if d[n] > 3000000}
    return b


def write_to_excel(t):
    workbook = xlsxwriter.Workbook('companies.xlsx', {'default_date_format': 'dd/mm/yy'})
    worksheet = workbook.add_worksheet('companies')

    cell_format = workbook.add_format({'bold': True, 'italic': True, 'bg_color': 'gray'})
    worksheet.write_string('A1', 'հ/հ', cell_format)
    worksheet.set_column('A:A', 5)
    worksheet.write_string('B1', 'Գնորդի անվանում', cell_format)
    worksheet.set_column('B:B', 90)
    worksheet.set_column('C:C', 30)
    worksheet.write_string('C1', 'Շրջանառություն առանց ԱԱՀ', cell_format)

    count = 1

    for m, n in t.items():
        worksheet.write(count, 0, count)
        worksheet.write(count, 1, m)
        worksheet.write(count, 2, n)
        count += 1

    workbook.close()


def write_to_sheets():
    write_to_excel(createdict())
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    j = createdict()
    for x, y in j.items():
        workbook = xlsxwriter.Workbook(f'{x}.xlsx', {'default_date_format': 'dd/mm/yy'})
        worksheet = workbook.add_worksheet('company')
        cell_format = workbook.add_format({'bold': True})
        count = 0
        for q in 'ABCDEFGHIJKLMNOPQRSTUVW':
            worksheet.write_string(f'{q}1', sheet.row_values(0)[count], cell_format)
            worksheet.set_column(f'{q}:{q}', 15)
            count += 1
        w = 1
        for h in range(1, sheet.nrows):

            if x == sheet.row_values(h)[13]:

                for s in range(len(sheet.row_values(h))):

                    worksheet.write(w, s, sheet.row_values(h)[s])
                w += 1
        workbook.close()


write_to_sheets()

