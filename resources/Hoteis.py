from flask_restful import Resource

hoteis = [
    {
        "id": 1,
        "nome": "Lucas",
    },
    {
        "id": 2,
        "nome": "Vitoria",
    },
    {
        "id": 3,
        "nome": "Sarai",
    }
]


class Hoteis(Resource):
    def get(self):
        return {'Hoteis': hoteis}


class Hotel(Resource):
    def get(self, hotel_id):
        return self.pega_hotel(hotel_id)

    def pega_hotel(self, hotel_id):
        for hotel in hoteis:
            if (hotel["id"] == hotel_id):
                return {'Hotel': hotel}
        return {"Erro:": "Hotel nao encontrado"}
