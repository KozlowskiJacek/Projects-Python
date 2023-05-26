import pandas as pd
from pandas.errors import ParserError

from datetime import datetime
import pprint
import csv
import os


class GPSMaker:
    TOLERANCE = 300

    def __init__(self, filename):
        self.filename = filename

        try:
            self.dataframe = pd.read_csv(self.filename)
        except ParserError:
            print("Sorry... Something went wrong: ParserERROR")
            print("-------------------------------------------")
            input("Press ENTER button to exit...")
            exit()

        self.dataframe.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

        self.reg_numbers = self.dataframe['Numer rejestracyjny'].unique()

        self.output = []

    def get_raports(self, simple = True,):
        for reg_number in self.reg_numbers:
            self.get_raport_for_reg_number(reg_number, simple)

    def get_raport_for_reg_number(self, reg_number, simple):
        reg_number_dataframe = self.dataframe.loc[self.dataframe['Numer rejestracyjny'] == reg_number]

        ride = []
        pivot = 0
        iloc_of_rides = []

        k_status = reg_number_dataframe['Status']
        iloc_of_status = k_status.tolist()

        k_driving_time = reg_number_dataframe['Czas rozpoczęcia']
        iloc_of_driving_time = k_driving_time.tolist()

        for s in iloc_of_status: 
            if s == 'Zapłon włączony':
                ride.append(iloc_of_driving_time[pivot])
                pivot += 1

            elif s == 'Zakłócenia zasilania':
                pivot += 1
                if simple is False:
                    ride.append(iloc_of_driving_time[pivot])
                    

            elif s == 'Odzyskano zasilanie':
                pivot += 1
                if simple is False:
                    ride.append(iloc_of_driving_time[pivot])
                    

            elif s == 'Start biegu jałowego':
                pivot += 1
                if simple is False:
                    ride.append(iloc_of_driving_time[pivot])
                    

            elif s == 'Koniec biegu jałowego':
                pivot += 1
                if simple is False:
                    ride.append(iloc_of_driving_time[pivot])
                    

            elif s == 'Zapłon wyłączony':
                    ride.append(iloc_of_driving_time[pivot])
                    iloc_of_rides.append(ride)
                    ride = []
                    pivot += 1
            else:
                print(f"Unknown log: {s}, Zgłoś to komuś z działu IT")
                ride.append(iloc_of_driving_time[pivot])
                pivot += 1 

        filtered_rides = self.filter_by_tolerance(iloc_of_rides)

        self.arrangement_of_iloc(filtered_rides, reg_number)

        location = []

        for point in self.output[-1]:
            if point == reg_number or point == '':
                location.append('')
            else:
                row_l = reg_number_dataframe.loc[reg_number_dataframe['Czas rozpoczęcia'] == point]
            
                try:
                    location.append(row_l.iloc[0]['Adres'])
                except IndexError:
                    location.append('')
   
        city = []

        for point in self.output[-1]:
            if point == reg_number or point == '':
                city.append('')
            else:
                row_c = reg_number_dataframe.loc[reg_number_dataframe['Czas rozpoczęcia'] == point]

                try:
                    city.append(row_c.iloc[0]['Miasto'])
                except IndexError:
                    city.append('')
        
        driving_time = []
           
        for t in filtered:
            first_time = datetime.strptime(t[0], '%Y-%m-%d %H:%M:%S')
            last_time = datetime.strptime(t[-1], '%Y-%m-%d %H:%M:%S')

            value = last_time - first_time

            value_str = str(value)

            formatted_value = value_str.split('.')[0]
            formatted_value = formatted_value.rjust(8, '0')

            driving_time.append(formatted_value)
        
        sum_of_driving_time = []

        for point in self.output[-1]:
            if point == reg_number or point == '':
                sum_of_driving_time.append('')
            else:
                row = reg_number_dataframe.loc[reg_number_dataframe['Czas rozpoczęcia'] == point]
                
                try:
                    status_list = row.iloc
                    for i in status_list:
                        is_turned_off = 'Zapłon wyłączony' in i['Status']
                    
                        if is_turned_off:
                            sum_of_driving_time.append(driving_time.pop(0))
                        else:
                            sum_of_driving_time.append('')
                except IndexError:
                    sum_of_driving_time.append('')

        gap = []
        self.output.append(sum_of_driving_time)
        self.output.append(location)
        self.output.append(city)
        self.output.append(gap)

    def save_to_file(self, filename):
        to_save = pd.DataFrame(self.output)
        
        to_save = to_save.transpose()

        to_save.to_csv(filename, index = False, header = False)

    def filter_by_tolerance(self, iloc_of_rides):
        global filtered
        pivot = 0
        filtered = []
        ride_with_none = []
        
        for i in iloc_of_rides:
            first_time = datetime.strptime(i[0], '%Y-%m-%d %H:%M:%S')
            last_time = datetime.strptime(i[-1], '%Y-%m-%d %H:%M:%S')

            converted_time = last_time - first_time

            if converted_time.total_seconds() < self.TOLERANCE:
                converted_time = None
                ride_with_none.append(converted_time)
            else:
                ride_with_none.append(converted_time)

        for n in ride_with_none:
            if n == None:
                pivot += 1
            else:
                filtered.append(iloc_of_rides[pivot])
                pivot += 1

        return filtered

    def arrangement_of_iloc(self, filtered, reg_number):
        iloc_for_reg_number = [reg_number]
        for x in filtered:
            iloc_for_reg_number.extend([" "] + x)

        self.output.append(iloc_for_reg_number)      


files = os.listdir("input")
for file in files:
    gps_maker = GPSMaker(f'input/{file}')
    gps_maker.get_raports(simple=True,)
    gps_maker.save_to_file(f"output/GPSMaker_{file}")

print("All cvs files have been changed correctly.")
print("-------------------------------------------")
input("Press ENTER button to exit...")
