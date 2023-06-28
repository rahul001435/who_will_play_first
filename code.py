import random
choose = ["ravi" , "shweta" , "mahima" , "akshay" , "ritik"]

first = random.choice(choose)
print(f"first postion: {first}" )
choose.remove(first)


second = random.choice(choose)
print(f"second postion: {second}" )
choose.remove(second)

third = random.choice(choose)
print("third postion:" , third )
choose.remove(third)

fourth = random.choice(choose)
print(f"fourth postion: {fourth}" )
choose.remove(fourth)

fifth = random.choice(choose)
print(f"fifth postion: {fifth}" )
choose.remove(fifth)

