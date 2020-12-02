# this file collects a range of uitility functions this multi-factor framework needs

import matplotlib.pyplot as plt


class util():
    @staticmethod
    def plot(x, y, file_name='default'):
        assert ((type(x) == list) & (type(x) == list)), "Plot inputs have to be lists"
        assert (len(x) == len(y)), "x-axis & y-axis need to be equally numbered"
        # plot to pdf file:
        f = plt.figure()
        plt.plot(x, y, 'o')
        f.savefig("./plots/" + file_name + ".pdf", bbox_inches="tight")
    
        
