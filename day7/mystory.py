story = """A mouse lived in a windmill in old Amsterdam {0}
A windmill with a mouse in  {1}
And he wasn't grousin'
He sang every morning
"How lucky I am
{2} Living in a windmill in old Amsterdam"

Once upon a time there was a teeny tiny mouse called Archie. His home was a mighty windmill where he lived with his mother and father. 

All day long {3} little Archie ran up and down the stairs and all around the many floors and corridors of his lovely home. """

 

adjective = raw_input("Enter an ajective: ")
noun1 = raw_input("Enter a noun: ")
number1 = raw_input("Enter a number as word: ")
noun2 = raw_input("Enter a second noun: ")
number2= raw_input("Enter a number as word: ")


print story.format(adjective,noun1,number1,number2,noun1)


