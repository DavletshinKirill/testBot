Вот основные команды Git, которые вам могут понадобиться:

    Клонирование репозитория:

Code

git clone https://github.com/username/repository.git

Эта команда создает локальную копию удаленного репозитория на вашем компьютере.

Инициализация репозитория:

Code

git init

Эта команда создает новый Git-репозиторий в текущей директории.

Добавление файлов в индекс (staging area):

Code

git add filename.txt
git add .

Первая команда добавляет один файл в индекс, вторая - все измененные файлы в текущей директории.

Создание коммита с комментарием:

Code

git commit -m "Описание изменений"

Эта команда создает новый коммит с указанным комментарием.

Отправка изменений на удаленный репозиторий:

Code

git push origin main

Эта команда отправляет ваши локальные коммиты на удаленный репозиторий на ветку main.

Слияние веток:

Code

git checkout main
git merge dev

Первая команда переключает вас на ветку main, вторая - сливает ветку dev в main.

Создание Pull Request:

    На GitHub или другом хостинге для Git перейдите в раздел "Pull Requests" и нажмите "New pull request".
    Выберите ветки, которые вы хотите слить (обычно ваша ветка в качестве "compare" и main в качестве "base").
    Добавьте описание изменений и отправьте Pull Request.

Обновление локального репозитория:

Code

git pull

Эта команда обновляет ваш локальный репозиторий, загружая последние изменения с удаленного репозитория.

Просмотр статуса репозитория:

Code

git status

Эта команда показывает состояние вашего локального репозитория, включая измененные, добавленные и неотслеживаемые файлы.

Просмотр истории коммитов:

Code

git log

Эта команда выводит историю коммитов в вашем репозитории.