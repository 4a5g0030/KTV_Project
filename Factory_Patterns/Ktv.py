import numpy as np 

class Ktv :
    def __init__(self):
        self.today = 0
        self.start_time = 0
        self.how_long = 0
        self.people = 0
        self.error = 0

    def set_data(self, today, start_time, how_long, people):
        self.today = today
        self.start_time = start_time
        self.how_long = how_long
        self.people = people
        self.check_data()
    
    def check_data(self):
        if(self.today <= 5 and self.start_time in np.array([9, 10])):
            self.error = 1


    def Calculation(self):
        pass

class with_room(Ktv):
    def Calculation(self):
        if(self.error == 1):
            return "輸入時間為打烊時間"
        else:    
            return round((self.room_level() * self.how_long + 138 *self.people) * 1.1)

    def room_level(self):
        if(self.people<=3):
            return 350
        elif(self.people<=6):
            return 490
        elif(self.people<=9):
            return 630
        elif(self.people<=12):
            return 770
        elif(self.people<=15):
            return 910
        else:
            return 1260

class with_people(Ktv):
    def Calculation(self):
        if(self.error == 1):
            return "輸入時間為打烊時間"
        else:
            return round(self.people_money_Calculation() * self.people * 1.1)
    def people_money(self, start_time, how_long):

        if(start_time in np.array([9,10])):
            if(self.today <= 5):
                return 0, 0, 0
            else:
                return 240, 3, 0
            
        elif(start_time in np.arange(11, 19)):
            if(self.today <= 5 ):
                return 210, 4, 0
            else:
                return 240, 3, 0

        elif(start_time in np.arange(19, 23)):
            if(self.today <= 4):
                return 300, 4, 0
            elif(self.today == 5):
                return 350, 3, 100
            elif(self.today == 6):
                return 420, 3, 100
            elif(self.today == 7):
                return 300, 4, 0
        
        elif(start_time == 23):
            if(self.today <= 4 or self.today == 7):
                return 260, 7, -1
            elif(self.today == 5):
                return 320, 7, 100
            elif(self.today == 6):
                return 380, 7, 100
        
        elif(start_time in np.array([0, 1, 2, 3, 4, 5])):
            if(self.today == 5 ):
                return 260, 7, -1
            elif(self.today == 6):
                return 320, 7, 100
            elif(self.today == 7):
                return 380, 7, 100

    def people_money_Calculation(self):
        r_money = 138
        how_long = self.how_long
        start_time = self.start_time

        while(how_long > 0):
            money, spend_time, rebate = self.people_money(start_time,how_long)
            r_money += money
            start_time += spend_time
            how_long -= spend_time
            if(how_long < 0):
                return r_money
            elif(rebate != 0):
                if(rebate == -1):
                    return r_money
                else:
                    return r_money + (rebate * how_long)
        
        return r_money

class Comparison_ktv():
    def __init__(self):
        self.people = with_people()
        self.room = with_room()
    
    def set_data(self, today, start_time, how_long, people):
        self.people.set_data(today, start_time, how_long, people)
        self.room.set_data(today, start_time, how_long, people)
    
    def Calculation(self):
        return self.people.Calculation(), self.room.Calculation()
    