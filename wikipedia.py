# Program to get wikipedia summary
# pip install wikipedia
import wikipedia
result = wikipedia.summary("Python", sentences = 5) #sentences refer to number of lines
print(result)
