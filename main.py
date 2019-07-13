def func():
    try:
        1 / 0
    except ZeroDivisionError:
        raise KeyError('Just a test')


def func2(obj):
    try:
        obj()
    except ZeroDivisionError:
        raise KeyError('Just another test')
