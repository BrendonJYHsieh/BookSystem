from core import BookSystem
from core import Authorization

def main():
    
    test = Authorization.User()
    test.register("B1081504444@gapps.ntust.edu.tw","1231231233")
    test.login("B1081504444@gapps.ntust.edu.tw","1231231233")
    
    #sys = BookSystem.BookSystem()
    #sys.start()

if __name__=="__main__":
   main()