def greeting() -> bool:
    print("Welcome to a SBp!\nThis is a program that will ask basic information about yourself\nThen, I'll just give you random responses.\nIt'll be so fun :D")
    user_readiness = input("Are you ready? y/n: ")
    if user_readiness == "y":
        print("Nice, lets get going!")
        return True
    elif user_readiness == "n":
        print(":( Bye bye then....")
        return False
    else:
        print("U good?")
        return False


def age_of_user() -> int:
    print("\nLets play a game!")
    print("Based on your age, ill tell you what you can and cannot do!")
    print("Ready?")
    age = int(input("Enter your age: "))
    if age < 13:
        print("Sorry, but you cannot sit in the passenger seat of a car. Sit at the back...")
    if age < 18:
        print("Sorry, you cannot vote!")
    if age <25:
        print("You cannot rent a car")
    if age > 35:
        print("You are an unc.....")
    if age == 35:
        print("Your 35?? Do you wanna know what 35 plus 32 is?")
        print("JK lets move on....")
    return age


def clean_words(words):
    if not words:
        return ""
    if len(words) == 1:
        return words[0]
    return ", ".join(words[:-1]) + " and " + words[-1]


def info_of_user(age: int) -> dict:
    name = input("\nEnter your name, please: ").strip()
    multilingual_status = input("Are you multilingual? y/n: ").strip().lower()

    if multilingual_status == "y":
        langs_raw = input("Enter your languages (comma-separated): ").strip()
        langs = []
        for x in langs_raw.split(","):
            cleaned = x.strip()
            if cleaned:
                langs.append(cleaned)
        print(f"Hello {name}, it's nice to meet you! So you're {age} ;)")
        print(f"It's also impressive that you can speak {clean_words(langs)}! "
              "Save some huzz for the rest of us...\n")

        return {
            "name": name,
            "age": age,
            "multilingual": True,
            "languages": langs,
            "desired": None
        }
    else:
        desired = input("Which language would you like to learn? ").strip()

        print(f"Hello {name}, {age} years old! I'm glad you wanna learn {desired}! Its quite ambitious but you got it! Lock in.\n")

        return {
            "name": name,
            "age": age,
            "multilingual": False,
            "languages": [],
            "desired": desired
        }
def main():
    if not greeting():          # end if not ready
        return

    age = age_of_user()            # ask/print rules here first
    user = info_of_user(age)    # collect name + multilingual, reuse age

    print("\nYour data:")
    print(user)

if __name__ == "__main__":
    main()

