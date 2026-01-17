from typing import Optional

from fastapi import FastAPI, status

from schemas import Animal

app = FastAPI()

my_animals: list[Animal] = []

@app.post("/", status_code=status.HTTP_201_CREATED)
def create_animal(data: Optional[Animal]):
    global my_animals
    if data:
        my_animals.append(data)
        return {
            'mensagem': 'Animal criado com sucesso'
        }
    return {
        'mensagem': 'Dados vazios'
    }


@app.get("/", status_code=status.HTTP_200_OK)
def list_animal():
    return {
        'animal': my_animals
    }