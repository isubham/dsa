
'''
- any data structure as input
- string, integer, 4:45 -> 

- add
- update
- remove
'''

class Clock():

    def __init__(self):
        pass

    def get_hour_angle(self, hour):
        if hour == 12:
            return 0
        res = (360 * hour) / 12
        return res


    def get_minute_angle(self, minute):
        if minute == 60:
            return 0
        return (360 * minute) / 60


    def add_delta_of_minute_on_hour(self, minute):
        return (minute / 60) * (360 / 12)


    def get_difference_in_angle(self, hour, minute):
        res = self.get_hour_angle(hour) \
            -((self.get_minute_angle(minute) + self.add_delta_of_minute_on_hour(minute)))
        res_mod = abs(res)
        res_another = 360 - res_mod
        diff = int(min(res_mod, res_another))
        return diff


def test_diff():
    c = Clock() 
    print(c.get_difference_in_angle(12, 0) == 0)
    print(c.get_difference_in_angle(12, 30) == 165)
    print(c.get_difference_in_angle(12, 45) == 90)


def test_m():
    c = Clock()
    print(c.get_minute_angle(1) == 6)
    print(c.get_minute_angle(60) == 0)
    print(c.get_minute_angle(0) == 0)
    print(c.get_minute_angle(30) == 180)



def test_h():
    c = Clock()
    print(c.get_hour_angle(0) == 0) 
    print(c.get_hour_angle(6) == 180)
    print(c.get_hour_angle(9) == 270) 
    print(c.get_hour_angle(11) == 0) 
    print(c.get_hour_angle(12) == 0) 


def test_add_h_to_m():
    c = Clock()
    print(c.add_delta_of_minute_on_hour(0) == 0)
    print(c.add_delta_of_minute_on_hour(30) == 15)
    print(c.add_delta_of_minute_on_hour(60) == 30)


def test():
    # test_m()
    # test_h()
    test_add_h_to_m()
    # test_diff()

test()