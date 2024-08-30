'''
Jason C Thompsen
CSC110
Project 1
Program concatenates string variables into a predefined central string as fill-in-the-blank responses
'''

def create_story(name1, street, name2, object, vehicle, adj):
  line1 = name1 +' decided to move from their apartment on 5th\nto a condo on '+street+'. They called their friend ' + name2+'\nfor help. However, they could not fit '+object+' into\nthe moving truck, so they had to rent a '+adjective+' '+vehicle+'\nin order to move it!'
  return line1

person_one = "Janet"
street_name = "Loopdydoo Avenue"
person_two = "Richard"
object_name = "Christmas tree"
vehicle = "Horse-drawn carriage"
adjective = "Off-road"
story = create_story(person_one, street_name, person_two, object_name, vehicle, adjective)
print(story)