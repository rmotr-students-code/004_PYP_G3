f = open('email.txt')

try:
    f.write()  # raise Exception()
except Exception:
    pass
finally:
    f.close()  # Never closed