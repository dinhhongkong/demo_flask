# Cài đặt môi trường ảo (Virtual Environment)

## Cài đặt virtualenv

Để cài đặt môi trường ảo, chạy lệnh sau:

```bash
pip3 install virtualenv
```

hoặc

```bash
py -m venv venv
```

## Kích hoạt môi trường ảo

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
.\venv\Scripts\activate
```

## Tạo requirements.txt

```bash
pip freeze > requirements.txt
```

## Cài đặt các thư viện từ requirements.txt

```bash
pip install -r requirements.txt
```

## Chạy trực tiếp bằng Python

macOS/Linux:

```bash
python app.py
```
