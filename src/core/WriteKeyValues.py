import os

class WriteKeyValues():
    def __init__(self, inputstring):

        cumulative_string = inputstring
        # os.path.dirname(__file__) gives us the directory of script
        pathname = os.path.dirname(__file__) + "\\KeyValues.csv"
        # print pathname

        if os.path.exists(pathname):
            with open(pathname, "a") as g:
                g.write(cumulative_string)
        else:
            with open(pathname, "w") as g:
                g.write(cumulative_string)