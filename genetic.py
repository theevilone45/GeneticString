import random, string
from random import randint
import os
from time import time

with open('data.txt', 'r') as myfile:
    target=myfile.read().replace('\n', ' ')

target_size = len(target)
population_size = 100
partners_count = 2
mutation_chance = 1
alpha=string.printable
target_accuracy=0.99

def generate_random_char():
	return random.choice(alpha)

def generate_random_string(n):
	return "".join(random.choice(alpha) for i in range(n))

def generate_population(n):
	population = []
	for i in range(n):
		population.append(generate_random_string(target_size))
	return population

def selection(pop):
	values = []
	for i in range(population_size):
		match = 0
		for j in range(target_size):
			if pop[i][j]==target[j]:
				match += 1
		value = match/target_size
		values.append(value)
	return values

def sort(arr):
	n=len(arr)
	while True:
		for i in range(n-1):
			x,y=arr[i]
			x1,y1=arr[i+1]
			if y<y1:
				arr[i],arr[i+1]=arr[i+1],arr[i]
		n-=1
		if n<=1:
			break
	pass


def cross_over(union):
	result=""

	for i in range(target_size):
		index = randint(0,partners_count-1)
		x,y=union[index]
		result+=x[i]

	mutation = randint(0,1000)
	if mutation >= int(mutation_chance*10):
		index = randint(0,target_size-1)
		new = list(result)
		new[index]=generate_random_char()
		result = ''.join(new)
	return result

def generate_new_population(union):
	pop=[]
	for i in range(population_size):
		temp = cross_over(union[:partners_count])
		pop.append(temp)
	return pop

def avg(arr):
	sum=0.0;
	for i in range(0,len(arr)-1):
		sum+=arr[i]
	return sum/len(arr)

def main():
	current_population = generate_population(population_size)
	generation_id = 0
	start = time()
	try:
		while True:
			fitness=selection(current_population)
			union = []
			for i in range(population_size):
				#print(current_population[i]+" : "+str(fitness[i]))
				union.append((current_population[i],fitness[i]))
			sort(union)

		#for i in range(len(union)):
			#print(union[i])
			x,y=union[0]
			diff_time=time()-start
			os.system("clear")
			print("Best member:     "+x)
			print("Best fitness:    "+str(y))
			print("Average fitness: "+str(avg(fitness)))
			print("Generation:      "+str(generation_id))
			print("Execution time:  "+str(diff_time))
		#new_member = cross_over(union[:child_count])
			current_population=generate_new_population(union)
			generation_id+=1
			if y>target_accuracy:
				print("DONE")
				break
		#print(current_population)
	except KeyboardInterrupt:
		print("\nBye :(")

main()
