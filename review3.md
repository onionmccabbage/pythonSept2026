## Python Review 3

- Alter these instructions to suit your thinking
- Aim for good architecture (maybe use separate modules, remember 'if __name__...')
- Look online, talk to each other, ask me etc.
- There will be an opportunity to share your code

Write a 'Weather' class with get/set methods for:

  'city' and 'description'

(remember: you will also need __init__ )

Your class should validate:
  - the value for 'city' is a non-empty string of three or more characters 
    (e.g. if type(city)== str and len(city)>2:)
  - if city is missing or unacceptable, you should provide a sensible default 
    (e.g. 'London')
  - 'description' must be a string, but it may be an empty string
  - decide if you will raise a TypeError or set a default for description

If you like, in your Weather class override __str__ so the class prints nicely,
something like 'The weather in London is cloudy'

Exercise the code by making instances of your Weather class with suitable values

### Optional (If Time)
Add a class property for 'temperature', which must be a float or integer

Decide how to handle invalid temperature values (e.g. raise an exception or set a default)

Include the temperature im your __str__ printout


Persist the city and description from each weather instance into a text file 

You could include a timestamp in this text file (use datetime)

Also provide a mechanism to read back the weather reports from the text file

