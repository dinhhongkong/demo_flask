## STRATEGY LOADING

Trong SQLAlchemy, phương thức .options() được sử dụng với nhiều strategy loading khác nhau ngoài joinedload. Dưới đây là các strategy phổ biến:
## Các Eager Loading Strategies chính
### 1. joinedload():
- Tạo LEFT OUTER JOIN để load quan hệ cùng lúc
- Tốt cho quan hệ one-to-many/many-to-one

```python
from sqlalchemy.orm import joinedload
Film.query.options(joinedload(Film.film_categories)).all()
```
### 2. selectinload():
- Thực hiện thêm SELECT IN query sau query chính
- Tránh cartesian product với quan hệ many-to-many

```python
from sqlalchemy.orm import selectinload
Film.query.options(selectinload(Film.film_categories)).all()
```
### 3. subqueryload():
- Dùng subquery để load quan hệ
- Hiệu năng kém hơn selectinload với nhiều bản ghi
```python
from sqlalchemy.orm import subqueryload
Film.query.options(subqueryload(Film.film_categories)).all()
```
### 4. lazyload():
- Load khi truy cập (mặc định)
```python
from sqlalchemy.orm import lazyload
Film.query.options(lazyload(Film.film_categories)).all()
```
### 5. noload():
- Không load quan hệ dù có truy cập
```python
from sqlalchemy.orm import noload
Film.query.options(noload(Film.film_categories)).all()
```

## Các tùy chọn khác trong options()
### 1. Load nhiều quan hệ:

```python
from sqlalchemy.orm import joinedload
Film.query.options(
    joinedload(Film.film_category_list),
    joinedload(Film.actors)
).all()
```
### 2. Nested eager loading (load quan hệ lồng nhau):

```python
from sqlalchemy.orm import joinedload
Film.query.options(
    joinedload(Film.film_category_list).joinedload(FilmCategory.category)
).all()
```
### 3. Deferred loading (chỉ load khi cần):
```python
from sqlalchemy.orm import defer
Film.query.options(defer(Film.description)).all()
```
### 4. Undefer (bỏ qua deferred):
```python
from sqlalchemy.orm import undefer
Film.query.options(undefer(Film.description)).all()
```