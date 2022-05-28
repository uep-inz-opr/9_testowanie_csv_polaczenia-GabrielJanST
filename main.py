import csv

class MenadzerPolaczen:
  def __init__(self, filename):
    self.filename = filename
    self.data_dict = self.read_data()

  def read_data(self):
    calls_dict_sum = dict()
    with open(self.filename, 'r') as fin:
      reader = csv.reader(fin, delimiter= ",")
      headers = next(reader)

      for row in reader:
        from_subsr = int(row[0])
        if from_subsr not in calls_dict_sum:
            calls_dict_sum[from_subsr] = 0
            calls_dict_sum[from_subsr] += 1 
    return calls_dict_sum

  def pobierz_najczesciej_dzwoniacego(self):
    return max(self.data_dict_sum, key= lambda x: x[1])

if __name__ == "__main__":
  nazwa_pliku = "phoneCalls.csv"
  mp = MenadzerPolaczen(nazwa_pliku)
  wynik = mp.pobierz_najczesciej_dzwoniacego()
  print (wynik)
