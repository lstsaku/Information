graph TD
    A([Начало]) --> B[/Ввод n, массивов A и C/]
    B --> C[Min_Val = A[1] - C[1]<br>Index = 1, i = 2]
    C --> D{i <= n?}
    D -- Да --> E[Diff = A[i] - C[i]]
    E --> F{Diff < Min_Val?}
    F -- Да --> G[Min_Val = Diff<br>Index = i]
    G --> H[i = i + 1]
    F -- Нет --> H
    H --> D
    D -- Нет --> I[/Вывод Min_Val, Index/]
    I --> J([Конец])
