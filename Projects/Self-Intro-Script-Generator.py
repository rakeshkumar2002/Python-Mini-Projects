# Self Intro Script Generator
import datetime

name = input("Can you please tell me your name?").strip()
age = input("Can you please tell me your age?").strip()
city = input("Can you please tell me in which city you live?").strip()
profession = input("What do you do for living?").strip()
hobby = input("What do like to do in your free time?").strip()

border = "*" * 80
print("\n {border}  \n\n")
print(f"Hello! My name is {name}. I'm {age} years old and live in {city}. I work as a {profession} and I absolutely enjoy {hobby} in my free time. Nice to meet you!")
print("\n *************************************************************************************************************************************************************** \n\n")
current_date = datetime.date.today().isoformat()
print(f"\n Logged on: {current_date} \n")