# Тема 1. Работа с репозиториями.
Отчет по Теме #1 выполнил:
- Судак Сергей Александрович
- АИС-22-1

| Задание | Лаб_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + | 
| Задание 10 | + |
| Задание 11 | + |
| Задание 12 | + |
| Задание 13 | + |
| Задание 14 | + |
| Задание 15 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:


## Лабораторная работа №1
### Установка.
Переходим на официальный сайт Git (https://git-scm.com/download/win) и скачиваем исполняемый файл.
Запускаем загруженный файл и устанавливаем. Рекомендуется использовать настройки по умолчанию.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/git_ins1.PNG)
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/git_ins2.PNG)

## Лабораторная работа №2
### Настройка.
Установка имени пользователя и адреса электронной почты.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/sett.PNG)

## Лабораторная работа №3
### Создание нового репозитория.
Инициализация репозитория локально.
Сначала переходим в папку проекта. Затем инициализируем пустой репозиторий в текущей папкес помощью Git init.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/create.PNG)
  
## Лабораторная работа №4
### Подготовка файлов.
Добовление одного файла.
Чтобы подготовить конкретный файл к коммиту, используем команду git add с указанием пути к файлу.
Проверка статуса.
После добавления файлов можно использовать команду git status, чтобы увидеть, какие файлы были подготовлены к коммиту.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/prepar.PNG)

## Лабораторная работа №5
### Фиксация изменений.
git commit используется для создания коммита, с флагом -m для добавления описания.
git log используется для просмотра списка коммитов.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/changes.PNG)
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/create2.PNG)

## Лабораторная работа №6
### Подключение к удаленному репозиторию.
git remote add origin URL связывает локальный репозиторий с удаленным.
git push загружает текущие изменения из вашего локального репозитория на удаленный.
git pull используется для извлечения изменений из удаленного репозитория и объединения их с текущей локальной веткой.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/conn.PNG)
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/conn2.PNG)
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/create3.PNG)
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/create4.PNG)

## Лабораторная работа №7
### Ветвление.
git branch с именем чтобы создать новую ветку.
С git checkout можно переключиться на другую ветку.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/branch.PNG)

## Лабораторная работа №8
### Особенности применения «Фетч».
fetch представляет собой операцию, которая извлекает изменения и обновления из удаленного репозитория, но не объединяет их с локальной веткой.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/fetch.PNG)

## Лабораторная работа №9
### Удаление файлов, веток, локальных и удалённых репозиториев.
git rm удаляет файл.
git push с флагом –delete используется для удаления удаленной ветки
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/delete.PNG)

## Лабораторная работа №10
### Отслеживание изменений в коммитах.
Команда git log выводит историю коммитов для текущей ветки.
Команда git diff позволяет сравнивать изменения между коммитами или ветками.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/log%20diff.PNG)

## Лабораторная работа №11
### Возвращение файла к предыдущему (определенному) состоянию.
git checkout возвращает файл к предыдущему состоянию в Git.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/ret.PNG)
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/ret2.PNG)
  
## Лабораторная работа №12
### Возвращение к предыдущему коммиту.
Для возврата к предыдущему коммиту в Git вы можете использовать команду git reset.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/git%20reset.PNG)
  
## Лабораторная работа №13
### Исправление коммита.
--amend повзволяет внести изменения в последний коммит.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/amend.PNG)
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/amend2.PNG)
  
## Лабораторная работа №14
### Разрешение конфликтов при слиянии.
Обычно конфликты возникают при выполнении операции слияния с другой веткой. Git может сообщить о конфликтах и приостановить слияние.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/24%201.PNG)
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/24%202.PNG)
  
## Лабораторная работа №15
### Настройка .gitignore.
.gitignore - это текстовый файл, который используется для указания Git'у файлов и директорий, которые не должны быть отслеживаемыми системой контроля версий.
### Результат.
![Меню](https://github.com/wasdwasdasd/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_1/pic/25.PNG)
  
## Общие выводы по теме
- Развернутый вывод
