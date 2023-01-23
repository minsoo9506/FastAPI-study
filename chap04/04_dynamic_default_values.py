import time
from datetime import datetime

from pydantic import BaseModel, Field


class Model(BaseModel):
    now: datetime = Field(default_factory=datetime.now)


d1 = Model()
print(d1)

time.sleep(1)

d2 = Model()
print(d2)

# now=datetime.datetime(2023, 1, 24, 0, 1, 16, 468194)
# now=datetime.datetime(2023, 1, 24, 0, 1, 17, 469344)
# 근데 default_factory를 이용하지 않고 일반적인 방법으로 하면 두 값이 같은 값으로 나온다
