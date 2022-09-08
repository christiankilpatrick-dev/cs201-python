n_humans = 535753
n_zombies = 10
n_bitten = ((n_humans-n_zombies)*0.1)
year = 2001

print(str(year)+","+str(n_zombies)+","+str(n_humans))

for i in range(0, 28):
    n_humans = n_humans - n_bitten
    n_zombies = n_zombies + n_bitten
    n_bitten = ((n_humans-n_zombies)*0.1)
    year = year+1
    
    print(str(year)+","+str(n_zombies)+","+str(n_humans))