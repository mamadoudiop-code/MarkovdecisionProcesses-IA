import random

class gridworld:
  #gridworld MDP
  def __init__(self):
    self.states =[(c,l) for l in range(1,4) for c in range(1,5)]
    self.states.remove((2,2)) #wall here
    self.actions =['L', 'U', 'R', 'D']
    self.gamma = 0.8

  def R(self, state):
    if (state==(4,2)):
      return 1
    elif (state==(4,1)):
      return -100
    return 0
  
  # transition probabilities
  def p(self, s1, a, s2):
    getAction = {
    'R': (1,0),
    'L': (-1,0),
    'U': (0,1),
    'D': (0,-1)
    }

    c1, l1 = s1 #line, col
    c2, l2 = s2 #
    dc, dl = getAction[a]

    # absorbing states: (etats finaux / absorbants)
    if (c1==4 and (l1==1 or l1==2)):
      return 0
  
    #other states
    # correct action
    if(l1+dl==l2 and c1+dc ==c2):
      return 0.8
    # goes off to side
    if(l1+dc==l2 and c1+dl ==c2) or (l1-dc==l2 and c1-dl ==c2):
      return 0.1
  
    #did we stay in place?
    if (l1==l2 and c1==c2):
      stayprob=0
      #if there was a wall ahead, p=0.8
      if(l1+dl<1 or l1+dl>3 or c1+dc<1 or c1+dc>4 or (l1+dl==2 and c1+dc ==2)): 
        stayprob=0.8
      # if there's a wall on one side, add 0.1
      if(l1+dc<1 or l1+dc>3 or c1+dl<1 or c1+dl>4 or (l1+dc==2 and c1+dl==2)):
        stayprob+=0.1
      #otherside
      if(l1-dc<1 or l1-dc>3 or c1-dl<1 or c1-dl>4 or (l1-dc==2 and c1-dl==2)):
        stayprob+=0.1
      return stayprob
    return 0 #no chance of going anywhere else

  #final states
  def isFinal(self, s):
    if (s==(4,1) or s==(4,2)):
      return True
    return False

  def simulate(self, s, a):
    possibles = [(s2, self.p(s,a,s2)) for s2 in self.states if self.p(s,a,s2)>0 ]
    newstate = random.choices([ss for ss,pp in possibles], weights=[pp for ss,pp in possibles])
    newstate = newstate[0] #random.choices returns a list
    return newstate, self.R(newstate)



  