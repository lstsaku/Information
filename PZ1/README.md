```mermaid
flowchart TD
    A(["Начало"]) --> B["Ввод n, массивов A и C"]
    B --> C["Min_Val = A[1] - C[1]"]
    C --> D["Index = 1, i = 2"]
    D --> E{"i <= n ?"}
    E -- "Да" --> F["Diff = A[i] - C[i]"]
    F --> G{"Diff < Min_Val ?"}
    G -- "Да" --> H["Min_Val = Diff<br>Index = i"]
    H --> I["i = i + 1"]
    G -- "Нет" --> I
    I --> E
    E -- "Нет" --> J["Вывод Min_Val, Index"]
    J --> K(["Конец"])
```
