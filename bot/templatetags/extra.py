from django import template
register = template.Library()
import datetime as dt
import os, ntpath, glob, traceback


@register.filter
def format_model(value):
    try:
        return value.replace("-","")
    except:
        return ""

        
@register.filter
def format_timesince(value):
    try:
        ls = {'s':'','year':'y','month':'m','week':'w','day':'d','hour':'h','minute':'m'}
        for x in ls:
            if x in value:
                value = value.replace(x,ls[x])
        return value
    except:
        return ""

@register.filter
def over_24(value):
    try:
        now = dt.datetime.now()
        diff = now - value
        #print diff.days*24 + diff.seconds/3600
        if diff.days*24 + diff.seconds/3600 >24:
            return True
        else:
            return False
    except:
        return False

@register.filter
def find_path(x):
    path, filename = ntpath.split(x)
    path = 'file://{0}\\'.format(path.replace('/','\\'))
    return path

@register.filter
def get_file(x):
    path, filename = ntpath.split(x)
    ls = []
    for f in glob.glob(os.path.join(path,'*.*')):
        p, fn = ntpath.split(f)
        ls.append([f.replace('\\\\192.168.209.10\\','').replace("\\","/"),fn])
    return ls

@register.filter
def subtract(value, arg):
    return value - arg

@register.filter
def due_date(value, arg):
    try:
        return value + dt.timedelta(days=arg)
    except:
        return value

@register.filter
def stndrd(st):
    ls = []
    for x in st.split(','):
        if str(x)[-1:] == '1':
            ls.append('{0}<sup>st</sup>'.format(x))
        elif str(x)[-1:] == '2':
            ls.append('{0}<sup>nd</sup>'.format(x))
        elif str(x)[-1:] == '3':
            ls.append('{0}<sup>rd</sup>'.format(x))
        else:
            ls.append('{0}<sup>th</sup>'.format(x))
    return ','.join(ls)

@register.filter
def i2p(value):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = float(value)
        return '{0}%'.format(round(value * 100, 2))
    except:
        pass
    return ''


@register.filter
def multi(value, arg):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = float(value)
        arg = float(arg)
        if arg: return round(value * arg, 2)
    except:
        pass
    return ''

@register.filter
def to_words(value):
    try:
        import math

        # Tokens from 1000 and up
        _PRONOUNCE = [
            'vigintillion',
            'novemdecillion',
            'octodecillion',
            'septendecillion',
            'sexdecillion',
            'quindecillion',
            'quattuordecillion',
            'tredecillion',
            'duodecillion',
            'undecillion',
            'decillion',
            'nonillion',
            'octillion',
            'septillion',
            'sextillion',
            'quintillion',
            'quadrillion',
            'trillion',
            'billion',
            'million',
            'thousand',
            ''
        ]

        # Tokens up to 90
        _SMALL = {
            '0': '',
            '1': 'ONE',
            '2': 'TWO',
            '3': 'THREE',
            '4': 'FOUR',
            '5': 'FIVE',
            '6': 'SIX',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine',
            '10': 'ten',
            '11': 'eleven',
            '12': 'twelve',
            '13': 'thirteen',
            '14': 'fourteen',
            '15': 'fifteen',
            '16': 'sixteen',
            '17': 'seventeen',
            '18': 'eighteen',
            '19': 'nineteen',
            '20': 'twenty',
            '30': 'thirty',
            '40': 'forty',
            '50': 'fifty',
            '60': 'sixty',
            '70': 'seventy',
            '80': 'eighty',
            '90': 'ninety'
        }

        def get_num(num):
            '''Get token <= 90, return '' if not matched'''
            return _SMALL.get(num, '').upper()

        def triplets(l):
            '''Split list to triplets. Pad last one with '' if needed'''
            res = []
            for i in range(int(math.ceil(len(l) / 3.0))):
                sect = l[i * 3: (i + 1) * 3]
                if len(sect) < 3:  # Pad last section
                    sect += [''] * (3 - len(sect))
                res.append(sect)
            return res

        def norm_num(num):
            """Normelize number (remove 0's prefix). Return number and string"""
            n = int(num)
            return n, str(n)

        def small2eng(num):
            '''English representation of a number <= 999'''
            n, num = norm_num(num)
            hundred = ''
            ten = ''
            if len(num) == 3:  # Got hundreds
                hundred = get_num(num[0]) + ' HUNDRES'
                num = num[1:]
                n, num = norm_num(num)
            if (n > 20) and (n != (n / 10 * 10)):  # Got ones
                tens = get_num(num[0] + '0')
                ones = get_num(num[1])
                ten = tens + ' ' + ones
            else:
                ten = get_num(num)
            if hundred and ten:
                return hundred + ' ' + ten
                # return hundred + ' and ' + ten
            else:  # One of the below is empty
                return hundred + ten

        def num2eng(num):
            '''English representation of a number'''
            num = str(int(num))  # Convert to string, throw if bad number
            if (len(num) / 3 >= len(_PRONOUNCE)):  # Sanity check
                raise ValueError('Number too big')

            if num == '0':  # Zero is a special case
                return 'ZERO '

            # Create reversed list
            x = list(num)
            x.reverse()
            pron = []  # Result accumolator
            ct = len(_PRONOUNCE) - 1  # Current index
            for a, b, c in triplets(x):  # Work on triplets
                p = small2eng(c + b + a)
                if p:
                    pron.append(p + ' ' + _PRONOUNCE[ct].upper())
                ct -= 1
            # Create result
            pron.reverse()
            return ', '.join(pron)

        dollars, cents = [int(num) for num in str(value).split(".")]

        dollars = num2eng(dollars)
        if dollars.strip() == "ONE":
            dollars = dollars + "DOLLAR AND "
        else:
            dollars = dollars + "DOLLARS AND "

        cents = num2eng(cents) + "CENTS"
        return dollars + cents

    except:
        traceback.print_exc()
        return ''


@register.filter
def store(value):
    try:
        return str(value)[-2:]
    except:
        return value


@register.filter
def format_timesince(value):
    try:
        ls = {'s': '', 'year': 'y', 'month': 'm', 'week': 'w', 'day': 'd', 'hour': 'h', 'minute': 'm'}
        for x in ls:
            if x in value:
                value = value.replace(x, ls[x])
        return value
    except:
        return ""

@register.filter
def div(value, arg):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = float(value)
        arg = float(arg)
        if arg: return int(value / arg)
    except:
        pass
    return ''

