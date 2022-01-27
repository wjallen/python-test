# this is a demo script to show how filehandling 
# works in python

my_shapes = ['circle', 'heart', 'triangle', 'square']

with open('my_shapes.txt', 'w') as f:
    for shape in my_shapes:
        f.write( f'{shape}\n' )
