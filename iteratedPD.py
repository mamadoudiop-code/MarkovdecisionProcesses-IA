import random

class againstTitforTat:
  # IPD avec Tit for Tat
  def __init__(self):
    self.states =[('I','I'),('C', 'C'), ('C','D'), ('D', 'C'), ('D','D')] #decrit les dernieres actions passees
    self.actions =['C', 'D']
    self.gamma = 0.1

  #CC=-1,-1 CD=0,-10, DD = -5,-5
  def R(self, state):
    j1, j2 = state
    if (j1=='C'):
      if (j2=='C'):
        return -1 #CC
      return -10  #CD
    elif (j1=='D'):
      if (j2=='C'):
        return 0
      return -5
    else:
      return 0 #etat initial
  
  # transition probabilities
  def p(self, s1, a, s2):

    ji1, ji2 = s1 #etat initial
    jf1, jf2 = s2 #etat final
    
    if (ji1=='I'):#premiere action
      if(jf1==a and jf2=='C'): #on joue qq chose, l'autre joue C
        return 1
      return 0
      
    if(a==jf1) and (jf2==ji1): # adversaire joue ce qu'on a joué en dernier
      return 1
    else:
      return 0
    

  #final states
  def isFinal(self, s):
    if (random.random()<0.01): #randomly finishes
      return True
    return False

  def simulate(self, s, a):
    possibles = [(s2, self.p(s,a,s2)) for s2 in self.states if self.p(s,a,s2)>0 ]
    newstate = random.choices([ss for ss,pp in possibles], weights=[pp for ss,pp in possibles])
    newstate = newstate[0] #random.choices returns a list
    return newstate, self.R(newstate)



  