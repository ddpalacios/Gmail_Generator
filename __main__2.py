from Random_Account import Random_Gen
from Navigation import Navigation_Window

if __name__ == "__main__":
    
    url = "http://gmail.com"

    window = Navigation_Window(url, 'firefox')
    random_gen = Random_Gen()
    window.Create_account(random_gen.random_first(),
                          random_gen.random_last(),
                          random_gen.randomUser(),
                          random_gen.random_pass(),
                          "2247354329")
    # Once completed, close browser
    window.curser.close()
