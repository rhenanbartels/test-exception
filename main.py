def func():
    try:
        1 / 0
    except ZeroDivisionError:
        raise KeyError('Just a test')
