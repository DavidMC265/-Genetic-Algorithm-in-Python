#!/usr/bin/env python
# coding: utf-8

# In[83]:


import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt


# In[84]:


# Station names instead of City objects
stationList = ["El Rosario", "San Lázaro", "Cuatro caminos", "Tacuba", "Politecnico", "Indios Verdes", "Instituto del Petroleo", "Deportivo 18 de Marzo", "Martin Carrera", "La Raza", "Consulado", "Oceania", "Hidalgo", "Guerrero", "Garibaldi", "Morelos", "Bellas Artes", "Balderas", "Salto del agua", "Pino Suarez", "Candelaria", "Gomez Farias", "Tacubaya", "Centro Medico", "Mixcoac", "Zapata", "Ermita", "Atlalico", "Barranca del muerto", "Universidad", "Tasquena", "Tlahuac"]  #All stations


# In[85]:


def get_travel_time(fromStation, toStation):
  # This is for illustrative purposes and might not reflect real travel times
  travel_time_in_minutes = random.randint(5, 20)
  return travel_time_in_minutes


# In[86]:


class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0


# In[87]:


def routeDistance(self):
       if self.distance == 0:
           pathDistance = 0
           for i in range(0, len(self.route)):
               fromStation = self.route[i]
               toStation = None
               if i + 1 < len(self.route):
                   toStation = self.route[i + 1]
               else:
                   toStation = self.route[0]
               travelTime = get_travel_time(fromStation, toStation)
               pathDistance += travelTime
           self.distance = pathDistance
       return self.distance


# In[88]:


def routeFitness(self):
       if self.fitness == 0:
           self.fitness = 1 / float(self.routeDistance())
       return self.fitness


# In[89]:


def createRoute(stationList):
  # Ensure route starts at "El Rosario" and ends at "San Lázaro"
  route = [stationList[0]] + random.sample(stationList[1:-1], len(stationList) - 2) + [stationList[-1]]
  return route


# In[90]:


def initialPopulation(popSize, stationList):
  population = []

  for i in range(0, popSize):
    population.append(createRoute(stationList.copy()))
  return population


# In[91]:


# Function to rank routes by fitness
def rankRoutes(population):
  fitnessResults = {}
  for i in range(0, len(population)):
    fitnessResults[i] = Fitness(population[i]).routeFitness()
  return sorted(fitnessResults.items(), key=operator.itemgetter(1), reverse=True)


# In[92]:


def selection(population, rankedPopulation, eliteSize):
  selected = []
  for i in range(0, eliteSize):
    selected.append(population[rankedPopulation[i][0]])
  remaining = random.sample(population, len(population) - eliteSize)
  selected.extend(remaining)
  return selected


# In[93]:


def matingPool(population, selectionResults):
  matingpool = []
  for i in range(0, len(selectionResults)):
    selection = selectionResults[i]
    matingpool.append(population[selection[0]])
  return matingpool


# In[94]:


def breed(parent1, parent2):
  # One-point crossover
  crossoverPoint = random.randint(1, len(parent1) - 2)
  offspring = parent1[:crossoverPoint] + parent2[crossoverPoint:]
  return offspring


# In[95]:


def mutate(route, mutationRate):
  for i in range(0, len(route)):
    if random.random() < mutationRate:
      swapIndex = random.randint(0, len(route) - 1)
      if swapIndex != i:
        route[i], route[swapIndex] = route[swapIndex], route[i]  # Swap elements
  return route


# In[96]:


def nextGeneration(pop, eliteSize, mutationRate):
  # Select parents
  rankedPop = rankRoutes(pop)
  selectionResults = selection


# In[ ]:


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
  pop = initialPopulation(popSize, population)
  print("Initial travel time: " + str(1 / rankRoutes(pop)[0][1]))

  for i in range(0, generations):
    pop = nextGeneration(pop, eliteSize, mutationRate)

  print("Final travel time: " + str(1 / rankRoutes(pop)[0][1]))
  bestRouteIndex = rankRoutes(pop)[0][0]
  bestRoute = pop[bestRouteIndex]

 # Extract the part of the route from El Rosario to San Lazaro
  route_to_display = bestRoute[1:-1]  # Exclude the first ("El Rosario") and last element ("San Lázaro")

  return route_to_display

bestRoute = geneticAlgorithm(stationList.copy(), popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
print("Fastest route:", bestRoute)

