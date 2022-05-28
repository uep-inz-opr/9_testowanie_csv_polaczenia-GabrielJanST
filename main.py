import csv

class MenadzerPolaczen:
  def __init__(self, filename):
    self.filenaCme = filename
    self.data_dict = self.read_data('phoneCalls.csv', 'r')

  def read_data(self):
    calls_dict_sum = dict()
    with open(self.read_data) as fin:
      reader = csv.reader(fin, delimiter= ",")
      headers = next(reader)

      for row in reader:
        from_subsr = int(row[0])
        if from_subsr not in calls_dict_sum:
            max(calls_dict_sum[from_subsr],key=calls_dict_sum[from_subsr])
    return calls_dict_sum

  def pobierz_najczesciej_dzwoniacego(self):
    return max(self.data_dict_sum, key= lambda x: x[1])

if __name__ == "__main__":
  nazwa_pliku = input()
  mp = MenadzerPolaczen(input)
  wynik = mp.pobierz_najczesciej_dzwoniacego()
  print (wynik)
