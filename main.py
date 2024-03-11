from gridworld import gridworld 
from iteratedPD import againstTitforTat
import learner

gw = gridworld()
#learner.valueIteration(gw)
learner.Qlearning(gw)

#ipd = againstTitforTat()
#learner.valueIteration(ipd)
#learner.Qlearning(ipd)



