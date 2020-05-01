import random
import math
import copy
from flask import Flask, request
from flask_restful import Api, Resource
from flask import jsonify
from flask_restful.utils import cors
import json
from flask_cors import CORS

import random as rn

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

#----------------------------------------Clases Componentes--------------------------------------------------------------
class Procesador:
    def __init__(self, nombre, ghz, precio, nucleos, calidad):
        self.nombre = nombre
        self.ghz = ghz
        self.precio = precio
        self.nucleos = nucleos
        self.calidad = calidad

class TarjetaGrafica:
    def __init__(self, nombre, frecuencia, precio, memoria, ancho_banda, calidad):
        self.nombre = nombre
        self.frecuencia = frecuencia
        self.precio = precio
        self.memoria = memoria
        self.ancho_banda = ancho_banda
        self.calidad = calidad

class RAM:
    def __init__(self, nombre, mhz, precio, memoria, calidad):
        self.nombre = nombre
        self.mhz = mhz
        self.precio = precio
        self.memoria = memoria
        self.calidad = calidad

class PlacaBase:
    def __init__(self, nombre, precio, calidad):
        self.nombre = nombre
        self.precio = precio
        self.calidad = calidad

class Cooler:
    def __init__(self, nombre, precio, calidad):
        self.nombre = nombre
        self.precio = precio
        self.calidad = calidad

class FuentePoder:
    def __init__(self, nombre, precio, calidad):
        self.nombre = nombre
        self.precio = precio
        self.calidad = calidad

class Disco:
    def __init__(self, nombre, tipo, precio, espacio, calidad):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.espacio = espacio
        self.calidad = calidad

class Case:
    def __init__(self, nombre, precio, calidad):
        self.nombre = nombre
        self.precio = precio
        self.calidad = calidad
#-------------------------------------------creacion de listas----------------------------------------------------------
lst_procesadores = []
lst_procesadores.append(Procesador("Intel Core i9-10900X", 3.70, 2474.62, 10, 30000))
lst_procesadores.append(Procesador("Intel Core i9-9900K", 3.60, 1986.54, 8, 29990))
lst_procesadores.append(Procesador("Intel Core i7 8700K", 3.70, 1710, 6, 26000))
lst_procesadores.append(Procesador("Intel Core i5 9600K", 3.70, 840, 6, 20000))
lst_procesadores.append(Procesador("Intel Core i5 8400", 2.80, 750, 6, 16000))
lst_procesadores.append(Procesador("Intel Core i3 8100", 3.60, 430, 4, 10000))
lst_procesadores.append(Procesador("Intel Pentium G5600", 3.90, 380, 2, 8000))
lst_procesadores.append(Procesador("Intel Celeron G4900", 3.10, 210, 2, 5000))


lst_tarjeta_grafica = []
lst_tarjeta_grafica.append(TarjetaGrafica("GeForce RTX 2080 Ti", 1350, 7459, 11, 616, 30000))
lst_tarjeta_grafica.append(TarjetaGrafica("GeForce RTX 2080 Super", 1650, 3400, 8, 496, 29990))
lst_tarjeta_grafica.append(TarjetaGrafica("GeForce RTX 2070 Super", 1605, 2650, 8, 484, 27000))
lst_tarjeta_grafica.append(TarjetaGrafica("GeForce RTX 2060 Super", 1470, 1800, 11, 616, 26900))
lst_tarjeta_grafica.append(TarjetaGrafica("GeForce GTX 1660 Super", 1530, 1300, 6, 336, 20000))
lst_tarjeta_grafica.append(TarjetaGrafica("GeForce GTX 1660 Ti", 1500, 1000, 6, 288, 18000))
lst_tarjeta_grafica.append(TarjetaGrafica("GeForce GTX 1060", 1645, 800, 6, 616, 13000))
lst_tarjeta_grafica.append(TarjetaGrafica("GeForce GTX 1050 Ti", 1480, 600, 4, 112, 5200))
lst_tarjeta_grafica.append(TarjetaGrafica("GeForce GT 1030", 1518, 320, 2, 48, 2000))


lst_RAM = []
lst_RAM.append(RAM("Corsair Vengeance", 2133, 313, 16, 9000))
lst_RAM.append(RAM("G.Skill Ripjaws", 2133, 290, 16, 9000))
lst_RAM.append(RAM("Trident Z", 2133, 270, 16, 8000))
lst_RAM.append(RAM("HyperX Fury", 2133, 230, 16, 7000))
lst_RAM.append(RAM("Team Group Delta", 2133, 160, 8, 3500))
lst_RAM.append(RAM("ADATA XPG Spectrix", 2133, 150, 8, 3500))


lst_placa_base = []
lst_placa_base.append(PlacaBase("Asus Rog Maximus Xi Formula", 2000, 1000))
lst_placa_base.append(PlacaBase("Gigabyte Z390 Aorus Master", 1380, 8000))
lst_placa_base.append(PlacaBase("Msi Mag Z390 Tomahawk", 760, 7000))
lst_placa_base.append(PlacaBase("Msi B360", 658, 5000))
lst_placa_base.append(PlacaBase("Gigabyte B360", 350, 5000))


lst_disco = []
lst_disco.append(Disco("Western Digital WD Black NVMe", "SSD", 650, "1 TB", 1000))
lst_disco.append(Disco("WD Bkue Nand", "SSD", 454, "1 TB", 700))
lst_disco.append(Disco("Seagate Barracuda", "HDD", 140, "1 TB", 100))
lst_disco.append(Disco("WD Blue", "HDD", 170, "1 TB", 100))
lst_disco.append(Disco("WD Black", "SSHD", 310, "1 TB", 100))


lst_cooler = []
lst_cooler.append(Cooler("Cooler Master Hyper H412", 38, 100))
lst_cooler.append(Cooler("Thermaltake UX100 ARGB", 49, 200))
lst_cooler.append(Cooler("Freezer 7 X de Arctic Cooling", 67, 250))
lst_cooler.append(Cooler("ARCTIC Freezer", 161, 400))
lst_cooler.append(Cooler("ARCTIC Freezer 34 duo", 162, 850))
lst_cooler.append(Cooler("Noctua NH-U12A", 337, 1200))
lst_cooler.append(Cooler("Dark Rock Pro TR4", 497, 900))


lst_fuente_poder = []
lst_fuente_poder.append(FuentePoder("NOX NX 750W ATX", 199, 5000))
lst_fuente_poder.append(FuentePoder("EVGA SuperNOVA 750 G3, 80 Plus Gold", 516, 5000))
lst_fuente_poder.append(FuentePoder("Corsair VS650", 273, 3000))
lst_fuente_poder.append(FuentePoder("Cooler Master MasterWatt 650", 276, 2900))
lst_fuente_poder.append(FuentePoder("Thermaltake TR2 S 700W", 280, 4000))


lst_case = []
lst_case.append(Case("Nox Modus", 122, 100))
lst_case.append(Case("Nox Coolbay MX2", 118, 150))
lst_case.append(Case("DeepCool Matrexx 30", 122, 200))
lst_case.append(Case("Aerocool Cylon", 140, 150))
lst_case.append(Case("Aerocool Streak", 120, 270))


#-------------------------------------------algoritmo--------------------------------------------------------------------
class SimulatedAnnealingPCGamer:
    def __init__(self, temperatura, velocidad_enfriamiento, presupuesto):
        self.temperatura = temperatura
        self.velocidad_enfriamiento = velocidad_enfriamiento
        self.presupuesto = presupuesto

    def algoritmo(self):
        #Establecemos una seleccion aleatoria
        pc_game = []

        while True:
            pc_game = []
            pc_game.append(random.choice(lst_procesadores))
            pc_game.append(random.choice(lst_tarjeta_grafica))
            pc_game.append(random.choice(lst_RAM))
            pc_game.append(random.choice(lst_placa_base))
            pc_game.append(random.choice(lst_disco))
            pc_game.append(random.choice(lst_cooler))
            pc_game.append(random.choice(lst_fuente_poder))
            pc_game.append(random.choice(lst_case))

            if not self.excede_presupuesto(pc_game):
                break

        current = copy.deepcopy(pc_game)
        best = copy.deepcopy(pc_game)
        new = copy.deepcopy(pc_game)

        while self.temperatura > 0.0001:
            cambio = copy.deepcopy(current)
            while True:
                # elegimos dos elementos(indices del array) y esperamos que no salgan del presupuesto
                i1 = random.randint(0, len(current) - 1)
                i2 = random.randint(0, len(current) - 1)
                cambio[i1] = self.seleccion_al_azar(i1)
                cambio[i2] = self.seleccion_al_azar(i2)

                if not self.excede_presupuesto(cambio):
                    break

            new = copy.deepcopy(cambio)

            #calculo de la energia
            current_energy = self.calcular_calidad(current)
            new_energy = self.calcular_calidad(new)
            best_energy = self.calcular_calidad(best)

            #funcion de aceptacion
            if new_energy > current_energy:
                prob = 1
            else:
                prob = math.exp((new_energy - current_energy)/self.temperatura)
            if prob > random.random():
                current = copy.deepcopy(new)

            #calculo de la energia
            if current_energy > best_energy:
                best = copy.deepcopy(current)

            self.temperatura = (1 - self.velocidad_enfriamiento)*self.temperatura

        return best


    def excede_presupuesto(self, lst_componentes):
        suma = 0
        for x in lst_componentes:
            suma = suma + x.precio
        if suma > self.presupuesto:
            return True

        return False

    def seleccion_al_azar(self, index):
        if index == 0:
            return random.choice(lst_procesadores)
        elif index == 1:
            return random.choice(lst_tarjeta_grafica)
        elif index == 2:
            return random.choice(lst_RAM)
        elif index == 3:
            return random.choice(lst_placa_base)
        elif index == 4:
            return random.choice(lst_disco)
        elif index == 5:
            return random.choice(lst_cooler)
        elif index == 6:
            return random.choice(lst_fuente_poder)
        elif index == 7:
            return random.choice(lst_case)

    def calcular_calidad(self, lst_componentes):
        suma = 0
        for x in lst_componentes:
            suma = suma + x.calidad

        return suma


#-----------------------------------API FLASK---------------------------------------------------------------------------
def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


class ProcesadoresResource(Resource):
    @cors.crossdomain(origin='*',
                      methods={"HEAD", "OPTIONS", "GET", "POST"})
    def get(self):
        return jsonify(to_dict(lst_procesadores))

class TarjetasGraficasResource(Resource):
    @cors.crossdomain(origin='*',
                      methods={"HEAD", "OPTIONS", "GET", "POST"})
    def get(self):
        return jsonify(to_dict(lst_tarjeta_grafica))

class RAMResource(Resource):
    @cors.crossdomain(origin='*',
                      methods={"HEAD", "OPTIONS", "GET", "POST"})
    def get(self):
        return jsonify(to_dict(lst_RAM))

class PlacasBaseResource(Resource):
    @cors.crossdomain(origin='*',
                      methods={"HEAD", "OPTIONS", "GET", "POST"})
    def get(self):
        return jsonify(to_dict(lst_placa_base))

class CoolersResource(Resource):
    @cors.crossdomain(origin='*',
                      methods={"HEAD", "OPTIONS", "GET", "POST"})
    def get(self):
        return jsonify(to_dict(lst_cooler))

class FuentesPoderResource(Resource):
    @cors.crossdomain(origin='*',
                      methods={"HEAD", "OPTIONS", "GET", "POST"})
    def get(self):
        return jsonify(to_dict(lst_fuente_poder))

class DiscosResource(Resource):
    @cors.crossdomain(origin='*',
                      methods={"HEAD", "OPTIONS", "GET", "POST"})
    def get(self):
        return jsonify(to_dict(lst_disco))

class CasesResource(Resource):
    @cors.crossdomain(origin='*',
                      methods={"HEAD", "OPTIONS", "GET", "POST"})
    def get(self):
        return jsonify(to_dict(lst_case))

class MejorPCPresupuesto(Resource):
    @cors.crossdomain(origin='*',
                      methods={"HEAD", "OPTIONS", "GET", "POST"})
    def post(self):
        presupuesto = request.json['presupuesto']

        sa = SimulatedAnnealingPCGamer(1000, 0.045, presupuesto)

        mejor_pc = sa.algoritmo()

        return jsonify(to_dict(mejor_pc))


api.add_resource(ProcesadoresResource, '/procesadores')
api.add_resource(TarjetasGraficasResource, '/tarjetasgraficas')
api.add_resource(RAMResource, '/rams')
api.add_resource(PlacasBaseResource, '/plcacasbases')
api.add_resource(CoolersResource, '/coolers')
api.add_resource(FuentesPoderResource, '/fuentepoder')
api.add_resource(DiscosResource, '/discos')
api.add_resource(CasesResource, '/cases')
api.add_resource(MejorPCPresupuesto, '/mejorpc')


if __name__ == '__main__':
    app.run(debug=True)