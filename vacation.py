def create_story(name1, name2, pet, animal, place, adj, verb, adv):
  line1 = name1+" and "+name2+" were best friends.\nOne day "+name1+" and "+name2+" decided to go on a\nvacation to "+place+". However, they didn't know\nwhat to do with their "+adj+" pet "+animal+" named "+pet+".\n"+pet+" had been causing problems, due to constant "+verb+"ing.\n"+name1+" found a sitter for their pet, and "+adv+" went on the trip."
  return line1

def main():
    person_one = "Joe" 
    person_two = "Lily" 
    pet_name = "Poncho"
    animal = "polar bear"
    place = "Madagascar"
    adjective = "Ridiculous"
    verb = "plank"
    adverb = "spastically"
    story = create_story(person_one, person_two, pet_name, \
                        animal, place, adjective, verb, adverb)
    print(story)

main()