https://docs-python.ru/standart-library/modul-csv-python/priemy-raboty-modulem-csv/


запись
```python
with open('date_output.csv', mode='w', encoding='cp1251') as date_output:
	file_writer = csv.writer(date_output, delimiter = ';', lineterminator='\n')
	file_writer.writerow(['номер магазина', 'ip магазина'])
	    for i in list_string:
	        answer = check_num_or_ip(i)
	        file_writer.writerow(answer)
```
