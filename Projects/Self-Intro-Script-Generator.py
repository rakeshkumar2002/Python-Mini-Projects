# Self Intro Script Generator
import datetime

name = input("Can you please tell me your name?")
age = input("Can you please tell me your age?")
city = input("Can you please tell me in which city you live?")
profession = input("What do you do for living?")
hobby = input("What do like to do in your free time?")

print("\n *************************************************************************************************************************************************************** \n\n")
print(f"Hello! My name is {name}. I'm {age} years old and live in {city}. I work as a {profession} and I absolutely enjoy {hobby} in my free time. Nice to meet you!")
print("\n *************************************************************************************************************************************************************** \n\n")
current_date = datetime.date.today().isoformat()
print(f"\n Logged on: {current_date} \n")