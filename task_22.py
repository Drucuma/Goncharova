import math

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_spend=0
total_salary = 0
money_capital = 0

for i in range(months):
    total_spend += spend
    spend *= (1+increase)
total_salary = salary*months
money_capital = total_spend - total_salary
print(f"Подушка безопасности, чтобы пр  отянуть {months} месяцев без долгов:", math.ceil(money_capital))



