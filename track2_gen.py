import datetime
import random
import hashlib
import xlsxwriter


def track2_tail():
    today = datetime.date.today()
    exp_year = datetime.date.today().year // 100 + 5
    exp_date = f'{str(exp_year)}{today.strftime("%m")}'
    last_part = '1011536004110000?'
    track_cont = f'={exp_date}{last_part}'
    return track_cont  # return the right side of track2


def pans_pref(start, end):
    prefix = '765432'
    for i in range(start, end):
        zero = '0' * (9 - len(str(i)))
        y = f'{prefix}{zero}{str(i)}'

        yield y  # return string 15 digits


def luhn_digit_find(n):
    l = [int(i) for i in n]
    x = l[1::2]
    y = l[::2]
    sum_pan = 0
    for p in y:

        p *= 2
        if p > 9:
            doubled = p % 10 + 1
        else:
            doubled = p
        sum_pan += doubled
    t = (((sum_pan + sum(x)) * 9) % 10)

    return t  # find out Luhn check digit


start_pan = int(input('Please input start number'))
end_pan = int(input('Please input end number'))
# create excel file and input info
workbook = xlsxwriter.Workbook('cards.xlsx', {'default_date_format': 'dd/mm/yy'})
worksheet = workbook.add_worksheet('cards')

cell_format = workbook.add_format({'bold': True, 'italic': True, 'bg_color': 'gray'})
worksheet.write_string('A1', 'PAN', cell_format)
worksheet.set_column('A:A', 20)
worksheet.write_string('B1', 'PIN', cell_format)
worksheet.set_column('B:B', 5)
worksheet.write_string('C1', 'PIN SHA-256 (can be calculated here: https://xorbin.com/tools/sha256-hash-calculator)',
                       cell_format)
worksheet.set_column('C:C', 70)
worksheet.write_string('D1', 'EXPIRATION DATE', cell_format)
worksheet.set_column('D:D', 17)
worksheet.write_string('E1', 'Track2', cell_format)
worksheet.set_column('E:E', 40)

count = 1

exp_year = datetime.datetime.now().year + 5
today_is = datetime.datetime.now().replace(year=exp_year)
track2_tail_for = track2_tail()

for m in pans_pref(start_pan, end_pan):
    A = '{}{}'.format(m, luhn_digit_find(m))
    track_2 = f';{A}{track2_tail_for}'
    #print(track_2)
    worksheet.write_string(count, 0, A)
    worksheet.write(count, 4, track_2)
    worksheet.write_datetime(count, 3, today_is)
    pin = random.randint(999, 9999)
    worksheet.write_number(count, 1, pin)

    k = hashlib.sha256(str(pin).encode('utf-8'))
    val_hex = k.hexdigest()
    worksheet.write(count, 2, val_hex)
    count += 1

workbook.close()
