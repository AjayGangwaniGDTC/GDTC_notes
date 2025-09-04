# utils.py

def calcLoad(vol):  # C0103: name should be calc_load
    "calculates load"  # C0116: missing docstring format
    if vol < 0:
        return 0
    return vol * 1.5  # R1705: no need for 'else' after return

def format_status(s):
    return "[[[" + s + "]]]"  # C0209: should use f-string formatting
