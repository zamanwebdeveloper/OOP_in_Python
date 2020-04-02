# Global Keyword
# function and class -- outside
i = 5
def func():
    print(i)
def chng():
    global i
    i = 6
    print(i)
func()
chng()
func()


