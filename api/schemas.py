from ninja import Schema

class BlockSchema(Schema):
    id: int
    title: str

class MenuSchema(Schema):
    order: int
    name: str

class CategorySchema(Schema):
    id: int
    name: str