# chapter 07

## 1. Security dependencies in FastAPI
- FastAPI에서 제공하는 dependency를 이용한다. [`.py`](./01_api_key_header.py)
- 가장(너무) 간단한 방법 중 하나다.

## 2. Storing a user and their password securely in a database
- password를 hash function을 이용하여 암호화해서 db에 저장한다. [`.py`](./02_hashing_password.py)

## 3. Retrieving a user and generating an access token, Securing endpoints with access tokens
- 유저의 이메일과 비밀번호를 받아서 확인이 되면 access token을 준다. [`.py`](./authentication/)

## 4. Configuring CORS and protecting against CSRF attacks
- skip