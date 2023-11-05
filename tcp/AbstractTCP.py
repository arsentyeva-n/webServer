from abc import ABC, abstractmethod

# Абстрактный класс TCP сервера.
class AbstractTCPServer(ABC):
    # метод должен отвечать за запуск TCP-сервера и начало прослушивания заданного хоста и порта. Он будет слушать входящие соединения и создавать соксеты для клиентов.
    @abstractmethod
    def start(self, host, port):
        pass
    
    # метод должен обеспечивать корректное завершение работы TCP-сервера и закрытие всех сокетов. Он будет вызываться, когда необходимо остановить сервер.
    @abstractmethod
    def stop(self):
        pass
    
    
    
    # Метод будет отслеживать изменения в базе данных.
    @abstractmethod
    def db_check(self):
        pass


    # метод будет отвечать за обработку ошибок, которые могут возникнуть в вашем сервере. Он может выполнять журналирование ошибок, отправку уведомлений и другие действия в случае ошибок.    
    @abstractmethod
    def handle_error(self, error_message):
        pass
   
        
# Абстрактный класс TCP соединения
class AbstractTCPConnection(ABC):
     # обработка каждого входящего соединения от клиента. Он должен читать запись из базы данных, отслеживать изменения в базе данных и отправлять измененную запись клиенту по TCP. Работает параллельно
    @abstractmethod
    def handle_client(self, client_socket):
        pass

    # метод будет использоваться для отправки измененной записи клиенту через его TCP-соксет. Он должен принимать соксет клиента и измененную запись, и выполнять процесс отправки данных клиенту.
    @abstractmethod
    def _send_data(self, data):
        pass

    # метод будет использоваться для получения данных от клиента через TCP-сокет.
    @abstractmethod
    def _receive_data(self, client_socket):
        pass

    # Метод должен добавлять или обновлять запись в базе данных. Данные берутся от клиента.
    @abstractmethod
    def _insert_data(self, data):
        pass
   
    # Этот метод может быть использован для обработки случаев, когда клиент отключается. Он должен выполнять необходимые действия, связанные с отключением клиента, чтобы поддерживать корректную работу сервера.
    @abstractmethod
    def handle_client_disconnect(self, client_socket):
        pass
