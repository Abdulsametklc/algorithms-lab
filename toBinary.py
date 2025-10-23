def toBinary(n):
  if n==0:
    return "0"
  binary = ""
  while n > 0:
    kalan = n % 2
    binary = str(kalan) + binary
    n = n // 2
  return binary
