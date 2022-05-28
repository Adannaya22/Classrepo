from tokenize import Number
from typing_extensions import Self
from unicodedata import name


class student:
    # This is a docstring for creating a skeleton class.

   def __init__(self, name, age, tracks, score):
         self . name = str(name)
         self . age = int(age)
         self . tracks = list[tracks]
         self . score = float(score)

   def change_name(self, new_name):
         self . name = new_name
         new_name = "Peter"
         print("The new name is (Peter)")

   def change_age(self, new_age):
         self . age = new_age
         new_age = 34
         print("The new age is (34)")

   def add_track(self, new_track):
         self . track = new_track
         new_track = "UI/UX"
         print("The new track is (UI/UX)")

   def get_score(self, new_score):
         self . score = new_score
         new_score = user_input = "number"
         print("The new number is (50.4)")   

Bob = student(name="Bob", age=26,tracks= "FE/BE",score= 20.90)

print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(50.4)





   