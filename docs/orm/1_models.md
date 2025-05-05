# Cách dựng Models trong SQLAlchemy
SQLAlchemy cung cấp hai cách chính để định nghĩa models:
1. **Declarative Base** (cách hiện đại, được khuyến nghị)

2. **Classical Mapping** (cách cổ điển)

Dưới đây là chi tiết cách dựng models bằng Declarative Base - cách tiếp cận phổ biến và dễ sử dụng nhất.

```python
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Tạo Base class cho tất cả models
Base = declarative_base()
```
# Cấu trúc cơ bản của một Model
Một model thường gồm:

* `__tablename__`: Tên bảng trong database

* Các cột (Column)

* Quan hệ (Relationships)

* Các phương thức tiện ích

ví dụ
```python
class User(Base):
    __tablename__ = 'users'
    
    # Primary key
    id = Column(Integer, primary_key=True)
    
    # Các trường thông tin
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Quan hệ 1-n với bảng Post
    posts = relationship("Post", back_populates="author")
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
```







## 2. Cấu trúc cơ bản của một Model

Một model thường gồm:
- `__tablename__`: Tên bảng trong database
- Các cột (Column)
- Quan hệ (Relationships)
- Các phương thức tiện ích

Ví dụ:
```python
class User(Base):
    __tablename__ = 'users'
    
    # Primary key
    id = Column(Integer, primary_key=True)
    
    # Các trường thông tin
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Quan hệ 1-n với bảng Post
    posts = relationship("Post", back_populates="author")
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
```

## 3. Các kiểu dữ liệu cơ bản

| Kiểu SQLAlchemy | Python          | Mô tả                     |
|-----------------|-----------------|---------------------------|
| Integer         | int             | Số nguyên                 |
| String(size)    | str             | Chuỗi, có thể giới hạn độ dài |
| Text            | str             | Chuỗi dài không giới hạn  |
| DateTime        | datetime.datetime| Ngày giờ                 |
| Float           | float           | Số thực                   |
| Boolean         | bool            | Giá trị True/False        |
| LargeBinary     | bytes           | Dữ liệu nhị phân          |
| Enum            | enum.Enum       | Kiểu liệt kê              |

## 4. Các tùy chọn Column thông dụng

```python
Column(
    Integer,                # Kiểu dữ liệu
    primary_key=True,       # Khóa chính
    autoincrement=True,     # Tự động tăng
    nullable=False,         # Không được null
    unique=True,           # Giá trị duy nhất
    default=0,             # Giá trị mặc định
    index=True,            # Tạo index
    name='user_name',      # Tên cột trong DB (khác tên attribute)
    server_default='guest' # Giá trị mặc định ở DB level
)
```

## 5. Định nghĩa quan hệ giữa các models

### Quan hệ một-nhiều (One-to-Many)

```python
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey('users.id'))
    
    # Quan hệ ngược trở lại User
    author = relationship("User", back_populates="posts")
    
    # Quan hệ nhiều-nhiều với Tag (xem bên dưới)
    tags = relationship("PostTag", back_populates="post")
```

### Quan hệ nhiều-nhiều (Many-to-Many)

Cần bảng trung gian (association table):

```python
# Bảng trung gian cho quan hệ nhiều-nhiều
class PostTag(Base):
    __tablename__ = 'post_tags'
    
    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Quan hệ với Post và Tag
    post = relationship("Post", back_populates="tags")
    tag = relationship("Tag", back_populates="posts")

class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    
    # Quan hệ ngược với Post qua PostTag
    posts = relationship("PostTag", back_populates="tag")
```

### Quan hệ một-một (One-to-One)

```python
class UserProfile(Base):
    __tablename__ = 'user_profiles'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    bio = Column(Text)
    avatar_url = Column(String(200))
    
    # Quan hệ một-một với User
    user = relationship("User", backref="profile", uselist=False)
```

## 8. Một số best practices

1. Đặt tên bảng ở dạng số nhiều (`users`, `posts`)
2. Đặt tên model ở dạng số ít (`User`, `Post`)
3. Luôn định nghĩa `__repr__` để debug dễ dàng hơn
4. Sử dụng `back_populates` hoặc `backref` để thiết lập quan hệ hai chiều
5. Đặt tên foreign key theo convention: `[tablename]_[primarykey]` (ví dụ: `user_id`)
6. Sử dụng server_default cho các giá trị mặc định phức tạp
7. Xem xét thêm index cho các cột thường được tìm kiếm

Với các hướng dẫn trên, bạn có thể xây dựng được hệ thống models phức tạp cho ứng dụng của mình bằng SQLAlchemy.