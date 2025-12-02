import matplotlib.pyplot as plt

categories = ['Технологии', 'Спорт', 'Искусство', 'Путешествия', 'Еда']
preferences = [30, 15, 25, 20, 10]

plt.pie(preferences, labels=categories, autopct='%1.1f%%')

plt.title('Предпочтения пользователей')

plt.savefig("3.png")

plt.show()
