def main():
    frct = input('Fraction: ').strip()
    prct = convert(frct)
    print(gauge(prct))


def convert(fraction):
                      x, y = fraction.split("/")
                      if int(x)/int(y) > 1:
                          raise ValueError
                      elif int(y) == 0:
                          raise ZeroDivisionError
                      return int(int(x)/int(y) * 100)


def gauge(percentage):
       try:
              if 1 < percentage < 99:
                     return f'{percentage:.0f}%'
              elif 0 <= percentage <= 1:
                     return "E"
              elif 99 <= percentage <= 100:
                     return "F"
              else:
                    raise TypeError
       except TypeError:
              pass


if __name__ == "__main__":
    main()