import json

# ******Create Json object from a dictionary******** 

# Create a dictionary object
person_dict = {'first': 'Christopher', 'last':'Harrison'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Seattle'

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)

# Print JSON object
print(person_json)



# **********Creeate Json with List**********

# Create a dictionary object
person_dict = {'first': 'Christopher', 'last':'Harrison'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Seattle'

# Create a list object of programming languages 
languages_list = ['CSharp','Python','JavaScript']

# Add list object to dictionary for the languages key
person_dict['languages']= languages_list

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)

# Print JSON object
print(person_json)




# ****Create json with nested Dictionary *****

# Create a dictionary object
person_dict = {'first': 'Christopher', 'last':'Harrison'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Seattle'

# create a staff dictionary
# assign a person to a staff position of program manager
staff_dict ={}
staff_dict['Program Manager']=person_dict
# Convert dictionary to JSON object
staff_json = json.dumps(staff_dict)

# Print JSON object
print(staff_json)


# samlple JSON object
# ****Create json with nested Dictionary *****

# Create a dictionary object
person_dict = {'first': 'Christopher', 'last':'Harrison'}
# Add additional key pairs to dictionary as needed
person_dict['City']='Seattle'

# create a staff dictionary
# assign a person to a staff position of program manager
staff_dict ={}
staff_dict['Program Manager']=person_dict

# Create a list object of programming languages 
languages_list = ['CSharp','Python','JavaScript']

# Add list object to dictionary for the languages key
person_dict['languages']= languages_list

# Convert dictionary to JSON object
staff_json = json.dumps(staff_dict)

# Print JSON object
print(staff_json)

