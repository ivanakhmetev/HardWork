### 1.py
ЦС исходная - 8  
ЦС итоговая 4, 4, 1, 1  
Метод (зачем-то обернутый в класс, не стал уже это менять) пробует установить соединение с базой данных и напечатать результат какого-то запроса.  
Исходно неплохо названы переменные, но логика действительно не сразу видна / перемешана.   
Изолировал целевой метод (обращение к базе, печать), заменив цикл for на map.  
Очистил установку соединения от побочных проверок и выводов.  
В итоге получилось проще и понятнее: попытки установки соединения с прерыванием и действие, если соединение установилось. Ушла переменная status, хотя 
в варианте автора это имеет смысл. Т.е. автор неплохо назвал переменную, но это можно было сделать лучше, вообще отказавшись от нее с помощью снижения ЦС(неожиданно). 

### 2.py
