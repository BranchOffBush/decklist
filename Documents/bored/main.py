import decks as a

def main():
    while True:
        print("***Menu***")
        print("1. Print Pre Gens")
        print("2. Bobby....")
        print("3. exit")

        choice = input("enter a number in the menu please")
        if choice == "1":
            a.preGen1(a.topDocString, a.bottomDocString, a.divider)
            a.preGen2(a.topDocString, a.bottomDocString, a.divider)
            a.preGen3(a.topDocString, a.bottomDocString, a.divider)
            a.preGen4(a.topDocString, a.bottomDocString, a.divider)
            a.preGen5(a.topDocString, a.bottomDocString, a.divider)
        elif choice == "2":
            print("Good choice.....BOBBYYY!!!")
            print("""
most major mulitplayer/online video games made by AAA companies are rigged using elaborate backend systems
similar to tailor gameplay like a tailored for you social media page, so much so that they can quote
"fine-tune the matchmaking process, the system may include an analytics and feedback engine that analyzes player and match data
to determine whether a given match was good. A match may be deemed “good” when a player is determined to have enjoyed gameplay
associated with the match based on one or more quality factors that are used as a proxy for player satisfaction. The quality
factors may include, for example, a duration of a gameplay session (e.g., via analysis of player historical data),
player psychological state (e.g., frustration level), and/or other information."
if you wanna know more
""")
            print("https://docs.google.com/document/d/1XxSzqnmj_6FDfWmouyFS4Y0NRsA-_4jsatEvLhXm6ek/edit?usp=sharing \n")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()
