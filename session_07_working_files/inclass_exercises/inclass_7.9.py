# 7.9:  Again with class What inheriting from class Do,
# compare the results from dir() and the results from the
# .__dict__ attribute of the class.  (No need to create an
# instance, simply work with the What class object.)

class Do:

    d = 5

    def dothis(self):
        print('done!')


class What(Do):
    w = 10

    def whatever(self):
        print('chill!')


