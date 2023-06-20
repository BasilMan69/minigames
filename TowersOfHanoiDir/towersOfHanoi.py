from .stack import Stack

class TowersOfHanoi:
  name = 'Towers of Hanoi'
  def __init__(self):
    #Create the self.stacks
    self.stacks = []
    self.left_stack = Stack("Left")
    self.middle_stack = Stack("Middle")
    self.right_stack = Stack("Right")
    self.stacks.append(self.left_stack)
    self.stacks.append(self.middle_stack)
    self.stacks.append(self.right_stack)

  def get_input(self):
    choices = [stk.get_name()[0].lower() for stk in self.stacks]
    while True:
      for i in range(len(self.self.stacks)):
        name = self.stacks[i].get_name()
        letter = choices[i].upper()
        print(f"Enter {letter} for {name}")
      user_input = input("").lower()
      if user_input in choices: 
        for i in range(len(self.stacks)):
          if user_input == choices[i]:
            return self.stacks[i]
      else:
        print("Invalid input.Try again!")

  def play(self):
    print("\nLet's play Towers of Hanoi!!")

    #Set up the Game
    num_disks = int(input("\nHow many disks do you want to play with?\n"))
    while num_disks < 3:
      num_disks = int(input("Enter a number greater than or equal to 3\n"))
    for i in range(num_disks, 0, -1):
      self.left_stack.push(i)

    num_optimal_moves = 2**num_disks - 1
    print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))

    #Play the Game
    num_user_moves = 0
    while self.right_stack.get_size() != num_disks:
      print("\n\n\n...Current stacks...")
      for stack in self.stacks:
        stack.print_items()
      while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = self.get_input()
        print("Which stack do you want to move to?\n")
        to_stack = self.get_input()
        if to_stack.is_empty() or from_stack.peek() < to_stack.peek():
          disk = from_stack.pop()
          to_stack.push(disk)
          num_user_moves += 1
          break
        else:
          print("\n\nInvalid Move.Try Again")
          print("\n\n\n...Current self.stacks...")
      for stack in self.stacks:
          stack.print_items()

    print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))

    
