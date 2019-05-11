a= [1,3,5,8,7,9,2]

#multiplicar la cada elemento de la lista por 10

[i*10 for i in a]

#multiplicar cada elemento de la lista por 10 con lambda

f= lambda x : x*10

[f(i) for i in a]


[(lambda x: x*10)(i) for i in a]
