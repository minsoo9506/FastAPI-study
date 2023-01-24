# chapter 04

## 1. Defining models and their field types with Pydantic

### standard field types
- 기본적인 field type 적용 [`.py`](./01_standard_field_type.py)
    - `Enum` 클래스를 이용하여 정해진 값들만 validation을 통과하게 할 수 있다.

### optional fields and default values
- optional field의 경우는 `Optional`을 이용하고 default value는 할당하면 된다. [`.py`](./02_optional_fields_default_values.py)

### field validation
- `Field`함수를 이용한다. [`.py`](./03_fields_validation.py)
    - `Field`의 첫번째 인자는 default값을 의미, `...`는 required의 의미

### dynamic default values
- 현재 시간처럼 dynamic한 값을 받아야하는 경우 `default_factory`라는 parameter를 이용한다. [`.py`](./04_dynamic_default_values.py)
    - 그렇지 않으면 인스턴스를 처음 생성하는 시점의 값이 반복된다.

### validating email addresses and URLs with pydantic type
- `pip install email-validator`
- email과 http url도 validation할 수 있다. [`.py`](./05_email_url_validation.py)

## 2. Creating model variations with class inheritance
- 중복되는 내용을 클래스 상속을 통해 해소한다. [`.py`](./06_model_inheritance.py)

## 3. Adding custom data validation with Pydantic

### applying validation at a field level
- 데코레이터 `@validator`를 통해서 field level에서 원하는 로직을 구현할 수도 있다. [`.py`](./07_custom_validation_field.py)

### applying validation at an object level
- 데코레이터 `@root_validator`를 통해서 object level에서 원하는 로직을 구현할 수도 있다. [`.py`](./08_custom_validation_object.py)

### applying validation before pydantic parsing
- validator들은 default로 parsing을 한 뒤에 적용된다. 즉, invalid한 type이 들어오면 validator에 적용되기 전에 error가 난다.
- 하지만 때로는 validator를 먼저 적용한 뒤에 판단하고 싶을 수 있다. `pre` parameter를 이용한다. [`.py`](./09_custom_validation_before_parsing.py)