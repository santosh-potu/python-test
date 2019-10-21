def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt);
        if ok in ('y','ye','yes'):
            return True
        elif ok in ('n','no'):
            return False
        retries = retries - 1
        if retries < 1 :
            raise(ValueError("Invalid User Response"))
        print(reminder);

ask_ok(retries=2, prompt='OK to overwrite the file?')


def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any ", kind, "?")
    print("-- I'm sorry, we're all out of", kind)

    for arg in arguments:
        print (arg)
        print("-"*40)
    for key in keywords:
        print (key, ":", keywords[key])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


