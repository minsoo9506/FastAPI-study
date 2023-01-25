# chapter 05

## 1. What is dependency injection?
- dependency injection
    - a system able to automatically instantiate objects and the ones they depend on
- 예를 들어, [`.py`](./01_dependency_injection.py)에 있는 `Header` 함수를 사용할 때, 구체적으로 required object에 대해 어떻게 동작하는지는 모른다.

## 2. Creating and using a function dependency
- FastAPI에서는 dependency를 함수나 클래스로 구현이 가능하다.
- 함수 예시 [`.py`](./02_create_function_dependency.py)

### get an object or raise a 404 error
- [`.py`](./03_create_function_dependency.py)의 예시처럼 dependency를 만들어주면 함수 내부의 처리의 구현이 깔끔해진다.

## 3. Creating and using a prameterized dependency with a class
- dependency에 parameter를 넣고 싶으면 클래스를 만들어서 이용한다. 
- `__init__`과 `__call__` 함수를 이용한다. [`.py`](./04_class_dependency.py)

### use class methods as dependencies
- 비슷하지만 약간의 차이가 있는 경우 한 클래스내에서 메소드로 구현하면 된다. [`.py`](./05_class_dependency.py)

## 4. Using dependencies at a path, router, and global level
- 지금까지처럼 single endpoint가 아니라 다양하게 dependency를 적용할 수도 있다.
    - path operation decorator의 parameter `dependencies` 이용  [`.py`](./06_path_dependency.py)
    - router [`.py`](./07_router_dependency.py)
    - global [`.py`](./08_global_dependency.py)