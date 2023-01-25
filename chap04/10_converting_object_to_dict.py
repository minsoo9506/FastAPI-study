from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str


p = Post(title="intro", content="hi!")

p_dict = p.dict()
print(p_dict["title"])
# intro

p_dict_include = p.dict(include={"title"})  # exclude도 가능
print(p_dict_include)
# {'title': 'intro'}
