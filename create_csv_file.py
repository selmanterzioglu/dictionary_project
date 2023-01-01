import csv


class create_csv_file():

    def __init__(self, path, data):
        self.path = path
        self.data = data
        self.init()

    def init(self):
        
        data_for_write = ""
        print("data_for_write: ", self.data)
        counter = 0
        for i in range(len(self.data)):
            for k in range(1, len(self.data[i])):
                data_for_write += self.data[i][k] + ";"

# ing1,ing2;turkce1, turkce2; cumle1;cumle1 detayli
