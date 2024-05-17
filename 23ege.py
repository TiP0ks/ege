def f(s, e):
  if s >= e or s == 32: return s == e
  return f(s + 2, e) + f(s + 4, e)
print(f(9, 27) * f(27, 29) * f(29, 37))