# -*- coding: utf-8 -*-


def xrange(start_stop, stop=None, step=None):
    """
    Funkcja która działa jak funkcja range (wbudowana i z poprzednich zajęć)
    która działa dla liczb całkowitych.
    """
    start = start_stop
    if not stop:
        start = 0
        stop = start_stop

    while start < stop:
        yield start
        start += (step if step else 1)