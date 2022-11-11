per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму депозита: '))

deposit = []
for key in per_cent:
    percent_stak = per_cent[key] / 100 + 1
    all_money = money * percent_stak
    clear_profit = all_money - money
    deposit.append(clear_profit)

print(deposit)
print(f"Максимальная сумма, которую вы можете заработать — {max(deposit)}")