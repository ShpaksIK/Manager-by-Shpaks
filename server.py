import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind(('localhost', 3030)) # Привязываем серверный сокет к localhost и 3030 порту.
soc.listen(1) # Начинаем прослушивать входящие соединения.
conn, addr = soc.accept() # Метод который принимает входящее соединение.

while True:
	soc_data = conn.recv(1024) # Получаем данные из сокета.
	# if not soc_data:
	# 	break
	conn.sendall(soc_data) # Отправляем данные в сокет.
	print(soc_data.decode('utf-8'))
conn.close()
input("Done")