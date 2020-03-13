def rgb(r, g, b):
    return ('%02x%02x%02x' % (check(r), check(g), check(b))).upper()

def check(i): 
  return max(0, min(i, 255))
