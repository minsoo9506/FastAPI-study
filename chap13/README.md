# chap13

## 1. Persisting a trained model with Joblib
### dumping a trained model
- 모델 객체를 `joblib`을 이용하여 효율적인 형태로 disk에 저장한다. (dump) [`.py`](./01_joblib_dump.py)
### loading a trained model
- 저장한 객체를 불러와서 prediction에 사용한다. (load) [`.py`](./02_joblib_load.py)

## 2. Implementing an efficient prediction endpoint(
- app 시작시에 model을 load하고 depends를 이용하여 예측값을 보낸다. [`.py`](./03_prediction_endpoint.py)

## 3. Caching results with Joblib
- 같은 input이 request로 들어오면 매번 model에 넣어서 predict할 필요는 없을 것이다.
- `joblib`을 이용하여 output을 cache하여 빠르게 reponse를 보낼 수 있다. [`.py`](./04_caching.py)