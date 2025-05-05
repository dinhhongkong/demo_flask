### Cài thư viện Redis client cho Python
Trước tiên, cần cài Redis client. Thường dùng redis-py
```bash
pip install redis
```

### Khởi tạo redis với Connection Pool
Với cách khởi tạo redis bình thường
```python
redis_client = redis.Redis(
    host='localhost',  # hoặc IP server Redis
    port=6379,         # port Redis
    db=0,              # db index, mặc định là 0
    decode_responses=True  # tự động decode từ bytes -> str
)
```
Mỗi lần redis.Redis() khởi tạo là một kết nối TCP riêng → tốn tài nguyên.
Connection Pool sẽ tái sử dụng kết nối, nhanh hơn, nhẹ hơn.
```python
# Tạo pool kết nối Redis
pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

# Khởi tạo Redis client với Pool
redis_client = redis.Redis(connection_pool=pool)
```

Một số lưu ý:

- Nếu Redis có password, thì thêm `password='your_password'` khi khởi tạo client.

- `decode_responses=True` giúp khỏi phải decode`('utf-8')` mỗi lần lấy dữ liệu từ Redis.

- Nếu Redis server ở xa (trên cloud/VPS), nhớ mở firewall và dùng SSL nếu cần bảo mật.



### Set key-value trong redis
```python
redis_client = redis.set(key, value)
```

### Get value trong redis
```python
redis_client = redis.get(key)
```