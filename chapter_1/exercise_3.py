# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your 
# average pace in seconds per mile?

segundos = 42 * 60 + 42
milhas = 10 / 1.61
segundos_por_milha = segundos / milhas 

print(f"O ritmo médio correndo 10 quilômetros em 42 minutos e 42 segundos é de \
{segundos_por_milha:.1f} segundos por milha.")
