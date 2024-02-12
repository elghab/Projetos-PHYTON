import math

input = 0
Output_desire = 0

input_wight = 0.5

learning_rate = 0.1

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

print('entrada', input, 'desejado', Output_desire)

error = math.inf

bias = 1
bias_weight = 0.5

iteration = 0

while not error == 0:
    iteration += 1
    print('########### Iteracao:', iteration)
    print('peso', input_wight)
    sum = (input * input_wight) + (bias * bias_weight)

    output = activation(sum)

    print('saida', output)

    error = Output_desire - output

    print('erro', error)

    if not error == 0:
        input_wight = input_wight + (learning_rate * input * error)
        bias_weight = bias_weight + (learning_rate * bias * error)

print ('A rede aprendeu! o valor desejado foi alcançado!')
        



# aula do youtube https://www.youtube.com/watch?v=I8MkOHFOmhc