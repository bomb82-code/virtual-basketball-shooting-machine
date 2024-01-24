# The virtual basketball-shooting machine
This repository provides code and solutions for a virtual basketball-shooting machine which is an example of Experience Learning algorithms. The experience learning of basketball-shooting machine is realized by a python program (gradient_descent_eperience.py) and a matlab program(experiencenihe.m). These are meant to exhibit the advantages of experiential learning.

 # Environment
python 3.7
numpy 1.21.5
xlwt 1.3.0
matlab R2014a

# Python program (gradient_descent_eperience.py)

In this program, the virtual basketball-shooting machine model is first given. 
D=√(（SS-100)^2+(HA^2)/(0.2^2 )+((PA-45)^2)/(0.2^2 ))	
In order to simulate the random error and quantization error in practice, errors are superimposed to the three parameters of the virtual basketball-shooting machine in the program.
This model is then detected using a conventional gradient descent algorithm. 
