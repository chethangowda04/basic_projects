#rock paper scissor game
import random
num=random.randint(0,2)
# a = """
# do you want play:
# 1)yes
# 2)no
# """
option="""
1)scissor
2)paper
3)stone
"""
print(option)
choice=input("enter the choice:")
list=['scissor','paper','stone']
type=list[num]
print(f"computer choose {type}")
# if choice==type:
#     continue
if choice=='scissor' and type=='paper':
        print("you win")
elif choice == 'scissor' and type== 'scissor':
        print("draw")
elif choice == 'scissor' and type == 'stone':
        print("computer win")
elif choice == 'paper' and type == 'paper':
        print("draw")
elif choice == 'paper' and type == 'scissor':
        print("computer win")
elif choice == 'paper' and type == 'stone':
        print("you win")
elif choice == 'stone' and type == 'paper':
        print("computer win")
elif choice == 'stone' and type == 'scissor':
        print("you win")
elif choice == 'stone' and type == 'stone':
        print("draw")