#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gurobipy import *


# In[2]:


# Create a new model
m = Model("mip1")

# Create variables
S = m.addVar(vtype=GRB.CONTINUOUS, name="S")
C = m.addVar(vtype=GRB.CONTINUOUS, name="C")
I = m.addVar(vtype=GRB.CONTINUOUS, name="I")
L = m.addVar(vtype=GRB.CONTINUOUS, name="L")
T = m.addVar(vtype=GRB.CONTINUOUS, name="T")
V = m.addVar(vtype=GRB.CONTINUOUS, name="V")
# Set objective
m.setObjective(150*S+225*C+250*I+500*L+400*T+200*V, GRB.MAXIMIZE)


# In[3]:


m.addConstr(S+C+I+L+T+V<=1200000, "c0")
m.addConstr(S+C<=620000, "c1")
m.addConstr(I+L<=400000, "c2")
m.addConstr(T+V<=275000, "c3")
m.addConstr(.5*S + .5*C - .5*L - .5*I>= 0, "c4")
m.addConstr(13*S + 7*C - 12*I - 15*L - 7*T - 2*V >=0, "c5")
m.addConstr(S <= 600000, "c6")
m.addConstr(C <= 400000, "c7")
m.addConstr(I <= 300000, "c8")
m.addConstr(L <= 225000, "c9")
m.addConstr(T <= 325000, "c10")
m.addConstr(V <= 100000, "c11")


# In[4]:


m.optimize()

for v in m.getVars():
    print('%s %g' % (v.varName, v.x)) #v.varName = Chair, Desk, Table
                                      #v.x = optimized value for that variable

print('Obj: %g' % m.objVal) 


# In[5]:


# Get shadow prices
shadow_prices = m.getAttr('Pi')
m.printAttr('Pi')
slack_valueus=m.getAttr('slack')
m.printAttr('slack')
for c in m.getConstrs():
    print('%s: %g' % (c.ConstrName, c.slack))


# In[ ]:




