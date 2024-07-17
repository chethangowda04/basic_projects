#rock paper scissor game
import random
num=random.randint(0,2)


print("""
1)rock
2)paper
3)scissor
""")
choice=input("select your choice:")


list=['scissor','paper','rock']
type=list[num]
print(f"computer choose {type}")
if choice=='rock' and type=='paper':
        print("computer won")
elif choice == 'rock' and type== 'rock':
        print("draw")
elif choice == 'rock' and type == 'scissor':
        print("you won")
elif choice == 'paper' and type == 'paper':
        print("draw")
elif choice == 'paper' and type == 'scissor':
        print("computer won")
elif choice == 'paper' and type == 'rock':
        print("you won")
elif choice == 'scissor' and type == 'paper':
        print("you won")
elif choice == 'scissor' and type == 'scissor':
        print("draw")
elif choice == 'scissor' and type == 'rock':
        print("computer won")