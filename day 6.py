# exercise 1
print("merging two dictionaries")
core_subjects={"maths":88,"physics":92,"chemistry":85}
extra_subjects={"computer science":95,"applied maths":96}
core_subjects.update(extra_subjects) 
print (core_subjects) 

print ("")
# exercise 2
print ("removing a key from a dictionary")
del core_subjects ["applied maths"]
print (core_subjects)

print ("")
# exercise 3
print ("two list into one dictionary")
list_one = ["maths", "physics","chemistry"]
list_two = ["80","90","100"]
print (list_one)
print (list_two)
mark_sheet = {}
for subjects in list_one:
	for marks in list_two:
		mark_sheet[subjects] = marks
		list_two. remove (marks)
		break
print (mark_sheet)

# exercise 4
print ("finding length of a set")
CSK = {"dhoni", "bravo", "jadeja"}
print (CSK)
set_length = len(CSK)
print (set_length)

# exercise 5
print ("to remove intersection of 2st set from 1nd set")
set_one = {"January","February","March","April","May","June"}
print (set_one)
set_two = {"June","July","August","September"}
print (set_two)
repeats = set_one & set_two
set_one = set_one - repeats
print (set_one)

