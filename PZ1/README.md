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
![Диаграмма](//www.plantuml.com/plantuml/png/JP0nIyH048Nx-HMlJ30MiSpUuHrdOs5h8o87jyiDn5LCHDlOsecj_o44XHJYRvZzHyukYrxrac_tlNqpgwxVFlIFjosb3shaJIRvaK_u2l8jOnZ287DY4zQG6Hj3pGNxcyjjYoNML_KrZh5HKNxkT_PPQLs1LKuCqTEUMuk2iLZ2dvRW3eMyorWIq9onSoc4KuYAKSmEHJfP83-aldvl_RyJEEWGxve4_mfm_BT-nuwKSYGuGcr8MMua7_8LNagACuVNF7KEhP22Z6xbxfvMQj8L_G80)
