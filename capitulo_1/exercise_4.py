# 4. What is your average pace in minutes and seconds per mile?

segundos = 42 * 60 + 42
milhas = 10 / 1.61
ritmo_medio_em_segundos_por_milha = segundos / milhas
minutos = ritmo_medio_em_segundos_por_milha // 60
segundos = ritmo_medio_em_segundos_por_milha % 60

print(f"O ritmo médio correndo 10 quilômetros em 42 minutos e 42 segundos é de \
{minutos:.0f} minutos e {segundos:.1f} segundos por milha.")
