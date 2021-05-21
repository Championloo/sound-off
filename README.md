# sound-off

Если у вас на работе тоже есть любитель послушать музыку на весь кабинет (даже в наушниках!), который иногда забывает заблокировать компьютер пока отходит, то у меня есть решение.

If you also have a lover at work to listen to music for the whole office (even with headphones!), who sometimes forgets to lock the computer while leaving, then I have a solution.

- вставьте токен telegram-бота /insert telegram bot token
- создайте исполнительный exe-файл с помощью pyinstaller /create an executable exe file using pyinstaller

```python -m PyInstaller --onefile --noconsole sound_off.py```
- поместите на компьютер (с OC Windows) любителя музыки /put on his computer (with Windows OS) a music lover
- опционально: создайте через планировщик задание с автоматическим включением приложения /optional: create a task through the scheduler with automatic activation of the application

*команда "Тише" устанавливает значение громкости на 27 /the command "Тише" sets the volume value to 27

В боте процесс выглядит так /In a bot, the process looks like this:

![image](https://user-images.githubusercontent.com/23462215/119099875-cd454e80-ba30-11eb-879f-c424fdf1e036.png)
