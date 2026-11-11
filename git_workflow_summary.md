# git init - Инициализация репозитория
# git switch -c / git checkout -b создание ветки и переход на нее
# git add - добавление файлов в stage area
# git commit -m - создание коммита с сообщением
# git stash - временно убрать незакомиченное, чтобы перейти к другой ветке
# git status - просмотреть что изменено и готово к коммиту
# git log -- - oneline просмотр  истории коммитов
# git diff -  просмореть что изменили в файле
# git diff --staged просмотреть, что изменили, когда оно в stage area
# git branch - просмотр веток
# git push -u origin - добавление коммита в удаленный репозиторий
# git pull - забираем изменения из удаленного репозитория себе
# git merge - объединение двух веток с сохранением истории коммитов
# git fetch - забираем измененеия с удаленного репозитория , но не объединяем со своим
# git rebase объединение двух веток, но история коммитов переписывается

ветка  main - основная

feature/add-discount-system - добавили систему скидов в product.py(В данном случае просто комментарий)
feature/add-email-validation - добавили проверку на валидацию email(В данном случае просто комментарий)
feature/add-inventory-management - добавили методы check_stock(показывает сколько есть товара) и update_stock(обновляет количество товара)
feature/add-shipping - Добавлены методы calculate_shipping и get_category в Product
feature/test-conflict - Изменен метод get_total_price в feature/test-conflict
feature/test-rebase - Добавлен метод apply_discount в Product

Конфликты:
В файле src/models/product.py был конфликт. В двух разных ветках feature/test-conflict и main был изменен один и тот же метод
и закоммичен. - конфликт решен путем выбора метода из main
В файле src/models/product.py был конфликт. В двух разных ветках feature/add-shipping и main были добавлены и закоммичены.
Конфликт решен путем добавления обоих методом в ветку feature/add-shipping.

В файле src/models/product.py был конлифкт слияния в основную ветку, в двух ветках ответвленных от main  feature/add-discount и 
feature/round-price менялся один и тот же метод get_total_price. При слиянии второй в main произошел конфликт. решен путем добавления
ручного объединения кода из веток

workflow для проекта SFMShop организован по модели Trunk-based. Создаются множество веток для определенных задач, когда фича
доделана ее добавляем в main.

Стратегия для работы с ветками  - создавать короткоживущие ветки feature для определнных задач, и влить по мере готовности в main





