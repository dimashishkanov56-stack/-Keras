import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('work_NS.keras')

print('Здравствуйте, этот бот со встроенной нейронной сетью \nспособен решать, устраивать вас на работу или же нет. Начнём?')

while True:
    print('-'*30)
    
    ask = input("Чтобы вводить - Да или 1, чтобы выйти - q или 2:")
    if ask == 'Да' or ask == '1':
        print("Супер, начинаем!")
    elif ask == 'q' or ask == '2':
        print("Жаль:( Ну ладно, если что, вы всегда можете зайти")
        break
    else:
        print("Извините, я не смог вас понять :/")
        continue  # ← если ввели мусор — начинаем заново

    no_criminal_record = int(input("Отсутствие судимости (1/0): "))
    sane = int(input("Вменяемость (1/0): "))
    education = int(input("Образование (1/0): "))

    X = np.array([[no_criminal_record, sane, education]])
    pred = model.predict(X)
    result = int(np.round(pred)[0][0])

    print(f"Прогноз: {result} (вероятность: {pred[0][0]:.3f})")

    if result == 1:
        print("Поздравляю, вы приняты на работу :D")
    else:
        print("К сожалению, вы не приняты на работу :(")

    ask2 = input("Продолжаем? Да-1, нет-q")
    if ask2 == 'Да' or ask2 == '1':
        print("Супер, продолжаем!")
        continue  
    elif ask2 == 'q' or ask2 == '2':
        print("Встретимся в следующий раз!")
        break
    else:
        print("Извините, я вас не понял :/")
        continue