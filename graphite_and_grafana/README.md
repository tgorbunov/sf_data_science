# graphite_and_grafana

Проект для запуска Graphite (образ `graphiteapp/graphite-statsd`, включающий Graphite, Carbon и StatsD) через Docker Compose.

## Запуск

```powershell
docker-compose up -d
```

## Порты

| Порт        | Назначение                                   |
|-------------|-----------------------------------------------|
| 80          | Веб-интерфейс Graphite (http://localhost)     |
| 2003-2004   | Carbon (приём метрик, plaintext/pickle)       |
| 2023-2024   | Carbon aggregator                             |
| 8125/udp    | StatsD                                        |
| 8126        | StatsD admin                                  |

Логин/пароль по умолчанию: `root` / `root`.

## Проверка отправки метрики

```python
import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 2003))
message = f"test.metric 42 {int(time.time())}\n"
sock.send(message.encode())
sock.close()
```

## Остановка

```powershell
docker-compose down
```
