import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class Pais:
    provincias = []#list para contener objetos de clase Provincia
    nombre = ""
    def __init__(self, p):
        self.provincias = p
        self.nombre = "Argentina"

    #Devuelve todos: varones + mujeres
    def get_total_poblacion(self):
        total = 0
        for p in self.provincias:
            total = total + p.get_total_poblacion()
        return total

    #Devuelte el objeto Provincia por el cod recibido
    def get_provincia(self, cod_provincia):
        p = None
        for x in self.provincias:
            if(x.get_cod() == cod_provincia):
                p = x
                break
        return p

    """
        Show the total illiterate population
        Show total population illiterate feminine
        Show total population illiterate male
    """
    
    def mostrar_totales_poblacion(self):
        total_pob = self.get_total_poblacion()
        total_pob_masculina_analfabeta = 0
        total_pob_masculina_alfabetos = 0
        total_pob_femenina_alfabetos = 0
        total_pob_femenina_analfabetos = 0
        for p in self.provincias:
            total_pob_masculina_analfabeta += p.alfabetismo.analfabetos.varones
            total_pob_femenina_analfabetos += p.alfabetismo.analfabetos.mujeres
            total_pob_masculina_alfabetos += p.alfabetismo.alfabetos.varones
            total_pob_femenina_alfabetos += p.alfabetismo.alfabetos.mujeres
        print("Total population:", total_pob)
        print("Male population:", total_pob_masculina_analfabeta + total_pob_masculina_alfabetos)
        print("Female population:", total_pob_femenina_analfabetos + total_pob_femenina_alfabetos)

    
   
    """
        Show the name of the province and its ratio of inhabitants per home
        Sort by ratio descendingly
    """
    def mostrar_ratio_habitantes_por_vivienda_por_provincia(self):
        habitante_casa = 0
        habitante_rancho = 0
        habitante_casilla = 0
        habitante_departamento = 0
        habitante_inquilino = 0
        habitante_hotel_o_pension = 0
        habitante_vivienda_mobil = 0
        for h in self.provincias:
            habitante_casa += h.viviendas[0].cantidad
            habitante_rancho += h.viviendas[1].cantidad
            habitante_casilla += h.viviendas[2].cantidad
            habitante_departamento += h.viviendas[3].cantidad
            habitante_inquilino += h.viviendas[4].cantidad
            habitante_hotel_o_pension += h.viviendas[5].cantidad
            habitante_vivienda_mobil += h.viviendas[6].cantidad
        print("Inhabitants in houses: ", str(habitante_casa))
        print("Ranch inhabitants: ", str(habitante_rancho))
        print("Inhabitants in square: ", str(habitante_casilla))
        print("Apartment inhabitants: ", str(habitante_departamento))
        print("Inhabitants in room / tenants: ", str(habitante_inquilino))
        print("Inhabitants in room / hotel or pension: ", str(habitante_hotel_o_pension))
        print("Inhabitants in mobile housing: ", str(habitante_vivienda_mobil))
        
    """
        Show the % of illiteracy by sex
    """
    def mostrar_porcentaje_analfabetismo_por_sexo(self):
        
        total_pob_masculina_analfabeta = 0
        total_pob_masculina_alfabetos = 0
        total_pob_femenina_alfabetos = 0
        total_pob_femenina_analfabetos = 0
        total_alfabetismo = 0
        for p in self.provincias:
            total_pob_masculina_analfabeta += p.alfabetismo.analfabetos.varones
            total_pob_femenina_analfabetos += p.alfabetismo.analfabetos.mujeres
            total_pob_masculina_alfabetos += p.alfabetismo.alfabetos.varones
            total_pob_femenina_alfabetos += p.alfabetismo.alfabetos.mujeres
        
        print("Percentage of illiterate men",round(total_pob_masculina_analfabeta / total_pob_masculina_alfabetos   * 100 ,3),"/100%")
        print("Percentage of illiterate women", round(total_pob_femenina_analfabetos /  total_pob_femenina_alfabetos   * 100, 3),"/100%")
        

    """
        Show the name of the province and the % of illiterates.
        Sort the list descending by %
    """
    def mostrar_porcentaje_analfabetismo_por_prov(self):
        nombres_provincias = []
        alfabetos_h = [] #hombres
        no_Alfabetos_h = [] #hombres
        alfabetos_m = [] #mujeres
        no_Alfabetos_m = [] #mujeres
        avg_h = []
        avg_m = []
        avg_t = []
        for p in self.provincias:
            nombres_provincias.append(p.nombre)
            alfabetos_h.append(p.alfabetismo.alfabetos.varones)
            no_Alfabetos_h.append(p.alfabetismo.analfabetos.varones)
            alfabetos_m.append(p.alfabetismo.alfabetos.mujeres)
            no_Alfabetos_m.append(p.alfabetismo.analfabetos.mujeres)
 
        for a, no_a in zip(alfabetos_h, no_Alfabetos_h):
            res = round(no_a / a * 100, 2)
            avg_h.append(res)
        
        for a, no_a in zip(alfabetos_m, no_Alfabetos_m):
            res = round(no_a / a * 100, 2)
            avg_m.append(res)

        
        for h, m in zip(avg_h, avg_m):
            res = round((h + m)/2 ,2)
            avg_t.append(res)
        
        res = zip(nombres_provincias, avg_t)
        for n, v in res:
            print("Name of the state: " + n, "--> " + "Total percentage of illiterate: ", v ,"/100%")

        

    """
        Mostrar el nombre de provincia y el % de viviendas sin retrete
        Ordenar la lista descendentemente por el %


    """
    #
    def mostrar_porcentaje_vivendas_sin_retrete_por_prov(self):
        nombres_provincias = []
        vivienda_con = [] 
        vivienda_sin = [] 
        avg_t = []
        
        for p in self.provincias:
            nombres_provincias.append(p.nombre)
            vivienda_con.append(p.sanitario.con_retrete)
            vivienda_sin.append(p.sanitario.sin_retrete)    

        for viv_c, viv_s in zip(vivienda_con, vivienda_sin):
            res = round(viv_s / viv_c * 100, 2)
            avg_t.append(res)
        
        
        res = zip(nombres_provincias, avg_t)
        for n, v in res:
            print("Name of the state: " + n, "--> " + "Total percentage of housing without toilet: ", v ,"/100%")
        
        
    #use these to calculate the slope because they are ordered in ascending order
    def mostrar_porcentaje_vivendas_sin_retrete_por_provincia(self):
        nombres_provincias = []
        vivienda_con = [] 
        vivienda_sin = [] 
        avg_t = []
        
        for p in self.provincias:
            nombres_provincias.append(p.nombre)
            vivienda_con.append(p.sanitario.con_retrete)
            vivienda_sin.append(p.sanitario.sin_retrete)    

        for viv_c, viv_s in zip(vivienda_con, vivienda_sin):
            res = round(viv_s / viv_c * 100, 2)
            avg_t.append(res)
        
        
        res = zip(nombres_provincias, avg_t)
        resultados_ordenados = sorted(res, key=lambda x: x[1])
        for n, v in resultados_ordenados:
            print("Name of the state: " + n, "--> " + "Total percentage of housing without toilet: ", v ,"/100%")
        
        return nombres_provincias, avg_t

    def mostrar_porcentaje_vivendas_sin_retrete_por_prov(self):
        nombres_provincias = []
        vivienda_con = [] 
        vivienda_sin = [] 
        avg_t = []
        
        for p in self.provincias:
            nombres_provincias.append(p.nombre)
            vivienda_con.append(p.sanitario.con_retrete)
            vivienda_sin.append(p.sanitario.sin_retrete)    

        for viv_c, viv_s in zip(vivienda_con, vivienda_sin):
            res = round(viv_s / viv_c * 100, 2)
            avg_t.append(res)
        
        
        res = zip(nombres_provincias, avg_t)
        for n, v in res:
            print("Name of the state: " + n, "--> " + "Total percentage of housing without toilet: ", v ,"/100%")
        
    """
        Mostrar el nombre de provincia y el % de los que no viven en una casa o departamento.
        Ordenar la lista descendentemente por el %
    """
    def mostrar_porcentaje_vivienda_precaria_por_prov(self):
        nombres_provincias = []
        habitante_casa = []
        habitante_rancho = []
        habitante_casilla = []
        habitante_departamento = []
        habitante_inquilino = []
        habitante_hotel_o_pension = []
        habitante_vivienda_mobil = []
        total_casas_dep = []
        total_viviendas_precarias = []
        avg_viviendas_precarias = []
        for h in self.provincias:
            nombres_provincias.append(h.nombre)
            habitante_casa.append(h.viviendas[0].cantidad)
            habitante_rancho.append(h.viviendas[1].cantidad)
            habitante_casilla.append(h.viviendas[2].cantidad)
            habitante_departamento.append(h.viviendas[3].cantidad)
            habitante_inquilino.append(h.viviendas[4].cantidad)
            habitante_hotel_o_pension.append(h.viviendas[5].cantidad)
            habitante_vivienda_mobil.append(h.viviendas[6].cantidad)
        
        for c, d in zip(habitante_casa, habitante_departamento):
            res = (c + d)
            total_casas_dep.append(res)
        
        for r, c, i, p, vm in zip(habitante_rancho, habitante_casilla, habitante_inquilino, habitante_hotel_o_pension, habitante_vivienda_mobil):
            res = (r + c + i + p + vm)
            total_viviendas_precarias.append(res)
        
        for c_d, v_p in zip(total_casas_dep, total_viviendas_precarias):
            res = round(v_p / c_d * 100, 2)
            avg_viviendas_precarias.append(res)

        res = zip(nombres_provincias, avg_viviendas_precarias)
        sorted_res = sorted(res, key=lambda x: x[1], reverse=True)

        for n, v in sorted_res:
            print("Name of the state: " + n, "--> " + "Total percentage of precarious housing: ", v ,"/100%")
        
    #use these to calculate the slope because they are ordered in ascending order
    def mostrar_porcentaje_vivienda_precaria_por_provincia(self):
        nombres_provincias = []
        habitante_casa = []
        habitante_rancho = []
        habitante_casilla = []
        habitante_departamento = []
        habitante_inquilino = []
        habitante_hotel_o_pension = []
        habitante_vivienda_mobil = []
        total_casas_dep = []
        total_viviendas_precarias = []
        avg_viviendas_precarias = []
        for h in self.provincias:
            nombres_provincias.append(h.nombre)
            habitante_casa.append(h.viviendas[0].cantidad)
            habitante_rancho.append(h.viviendas[1].cantidad)
            habitante_casilla.append(h.viviendas[2].cantidad)
            habitante_departamento.append(h.viviendas[3].cantidad)
            habitante_inquilino.append(h.viviendas[4].cantidad)
            habitante_hotel_o_pension.append(h.viviendas[5].cantidad)
            habitante_vivienda_mobil.append(h.viviendas[6].cantidad)
        
        for c, d in zip(habitante_casa, habitante_departamento):
            res = (c + d)
            total_casas_dep.append(res)
        
        for r, c, i, p, vm in zip(habitante_rancho, habitante_casilla, habitante_inquilino, habitante_hotel_o_pension, habitante_vivienda_mobil):
            res = (r + c + i + p + vm)
            total_viviendas_precarias.append(res)
        
        for c_d, v_p in zip(total_casas_dep, total_viviendas_precarias):
            res = round(v_p / c_d * 100, 2)
            avg_viviendas_precarias.append(res)

        res = zip(nombres_provincias, avg_viviendas_precarias)
        sorted_res = sorted(res, key=lambda x: x[1], reverse=True)

        for n, v in sorted_res:
            print("Name of the state: " + n, "--> " + "Total percentage of precarious housing: ", v ,"/100%")
        return nombres_provincias, avg_viviendas_precarias

    
    #use these to calculate the slope because they are ordered in ascending order
    def alfabetismo_ordenado_asc(self):
        nombres_provincias = []
        alfabetos_h = [] #men
        no_Alfabetos_h = [] #men
        alfabetos_m = [] #women
        no_Alfabetos_m = [] #women
        avg_h = []
        avg_m = []
        avg_t = []
        for p in self.provincias:
            nombres_provincias.append(p.nombre)
            alfabetos_h.append(p.alfabetismo.alfabetos.varones)
            no_Alfabetos_h.append(p.alfabetismo.analfabetos.varones)
            alfabetos_m.append(p.alfabetismo.alfabetos.mujeres)
            no_Alfabetos_m.append(p.alfabetismo.analfabetos.mujeres)

        #the for iterates the two lists to get the percentages  
        for a, no_a in zip(alfabetos_h, no_Alfabetos_h):
            res = round(no_a / a * 100, 2)
            avg_h.append(res)
        
        #the for iterates the two lists to get the percentages
        for a, no_a in zip(alfabetos_m, no_Alfabetos_m):
            res = round(no_a / a * 100, 2)
            avg_m.append(res)

        #the for iterates the two lists to get the percentages
        for h, m in zip(avg_h, avg_m):
            res = round((h + m)/2 ,2)
            avg_t.append(res)
        
        res = zip(nombres_provincias, avg_t)
        resultados_ordenados = sorted(res, key=lambda x: x[1])
        for n, v in resultados_ordenados:
            print("Name of the state: " + n, "--> " + "Literacy percentage: ", v ,"/100%")
        
        return nombres_provincias, avg_t
    

class Provincia:
    cod = None
    nombre = None
    alfabetismo = None #to contain an object of class Literacy
    sanitario = None #to contain an object of class Sanitary
    viviendas = [] #list to contain all housing types
    def __init__(self, c, n, a, r, v):
        self.cod = c
        self.nombre = n
        self.alfabetismo = a
        self.sanitario = r
        self.viviendas = v

    #Devuelve todos: varones más mujeres
    def get_total_poblacion(self):
        return self.alfabetismo.get_total()
        
    def get_cod(self):
        return self.cod



class PorSexo:
    varones = None
    mujeres = None
    def __init__(self, v, m):
        self.varones = v
        self.mujeres = m
   
    #Devuelve todos: varones más mujeres
    def get_total(self):
        return self.varones + self.mujeres


class Alfabetismo:
    alfabetos = None #para contener un objeto de clase PorSexo con datos de la personas alfabetas
    analfabetos = None #para contener un objeto de clase PorSexo con datos de la personas analfabetas    
    def __init__(self, a, no_a):
        self.alfabetos = a
        self.analfabetos = no_a

    #Total de la población: alfabetas + analfabetas
    def get_total(self):
        return self.alfabetos.get_total() + self.analfabetos.get_total()


class Sanitario:
    con_retrete = None
    sin_retrete = None
    def __init__(self, c, s):
        self.con_retrete = c
        self.sin_retrete = s

#class structure
class Vivienda:
    """
     TIPO (según INDEC):
        0: Casa
        1: Rancho
        2: Casilla
        3: Departamento
        4: Pieza/s en inquilinato
        5: Pieza/s en hotel o pensión
        6: Local no construido para habitación
        7: Vivienda móbil
    """
    tipo = None
    cantidad = None
    def __init__(self, t, c):
        self.tipo = t
        self.cantidad = c


#data source: https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-135

arg = Pais([
    Provincia(0, 'Ciudad Autónoma de Buenos Aires', Alfabetismo(PorSexo(1160483, 1395255), PorSexo(5344, 7059)), Sanitario(1061211, 21787), [Vivienda(0, 252771), Vivienda(1, 565), Vivienda(2, 1884), Vivienda(3, 788791), Vivienda(4, 19571), Vivienda(5, 17082), Vivienda(6, 2237), Vivienda(7, 97)]),
    Provincia(1, '24 partidos del Gran Buenos Aires', Alfabetismo(PorSexo(3917957, 4223950), PorSexo(55416, 61809)), Sanitario(2294650, 358638), [Vivienda(0, 2212645), Vivienda(1, 17794), Vivienda(2, 73827), Vivienda(3, 329731), Vivienda(4, 12452), Vivienda(5, 1405), Vivienda(6, 5091), Vivienda(7, 343)]),
    Provincia(2, 'Interior de la provincia de Buenos Aires', Alfabetismo(PorSexo(2285525, 2438254), PorSexo(33289, 28494)), Sanitario(1625106, 146799), [Vivienda(0, 1502191), Vivienda(1, 12283), Vivienda(2, 35724), Vivienda(3, 212714), Vivienda(4, 4117), Vivienda(5, 817), Vivienda(6, 3026), Vivienda(7, 1033)]),
    Provincia(3, 'Catamarca', Alfabetismo(PorSexo(144528, 148625), PorSexo(3108, 2928)), Sanitario(75871, 13505), [Vivienda(0, 83578), Vivienda(1, 2134), Vivienda(2, 400), Vivienda(3, 2666), Vivienda(4, 427), Vivienda(5, 30), Vivienda(6, 96), Vivienda(7, 45)]),
    Provincia(4, 'Chaco', Alfabetismo(PorSexo(394795, 411225), PorSexo(22440, 24292)), Sanitario(916669, 61884), [Vivienda(0, 236946), Vivienda(1, 12558), Vivienda(2, 5696), Vivienda(3, 12052), Vivienda(4, 2048), Vivienda(5, 165), Vivienda(6, 424), Vivienda(7, 244)]),
    Provincia(5, 'Chubut', Alfabetismo(PorSexo(205779, 206044), PorSexo(4049, 4265)), Sanitario(197102, 51742), [Vivienda(0, 122955), Vivienda(1, 1479), Vivienda(2, 1917), Vivienda(3, 19318), Vivienda(4, 1068), Vivienda(5, 58), Vivienda(6, 237), Vivienda(7, 144)]),
    Provincia(6, 'Córdoba', Alfabetismo(PorSexo(1314229, 1425717), PorSexo(22334, 18451)), Sanitario(176147, 93986), [Vivienda(0, 840488), Vivienda(1, 5929), Vivienda(2, 2775), Vivienda(3, 124044), Vivienda(4, 2852), Vivienda(5, 791), Vivienda(6, 1199), Vivienda(7, 475)]),
    Provincia(7, 'Corrientes', Alfabetismo(PorSexo(372493, 399455), PorSexo(17969, 16523)), Sanitario(136043, 11133), [Vivienda(0, 210288), Vivienda(1, 13056), Vivienda(2, 8147), Vivienda(3, 14201), Vivienda(4, 2293), Vivienda(5, 236), Vivienda(6, 393), Vivienda(7, 230)]),
    Provincia(8, 'Entre Ríos', Alfabetismo(PorSexo(486281, 519080), PorSexo(12294, 9610)), Sanitario(326978, 30272), [Vivienda(0, 317956), Vivienda(1, 3805), Vivienda(2, 7273), Vivienda(3, 26680), Vivienda(4, 644), Vivienda(5, 176), Vivienda(6, 495), Vivienda(7, 221)]),
    Provincia(9, 'Formosa', Alfabetismo(PorSexo(200956, 206992), PorSexo(7821, 9575)), Sanitario(79122, 51012), [Vivienda(0, 109807), Vivienda(1, 12203), Vivienda(2, 1514), Vivienda(3, 4124), Vivienda(4, 2104), Vivienda(5, 44), Vivienda(6, 229), Vivienda(7, 109)]),
    Provincia(10, 'Jujuy', Alfabetismo(PorSexo(261419, 269965), PorSexo(5404, 11784)), Sanitario(122201, 32710), [Vivienda(0, 134293), Vivienda(1, 7286), Vivienda(2, 2595), Vivienda(3, 7824), Vivienda(4, 2510), Vivienda(5, 74), Vivienda(6, 245), Vivienda(7, 84)]),
    Provincia(11, 'La Pampa', Alfabetismo(PorSexo(128679, 133208), PorSexo(2805, 2227)), Sanitario(101706, 3091), [Vivienda(0, 95356), Vivienda(1, 458), Vivienda(2, 169), Vivienda(3, 8239), Vivienda(4, 317), Vivienda(5, 10), Vivienda(6, 177), Vivienda(7, 71)]),
    Provincia(12, 'La Rioja', Alfabetismo(PorSexo(131833, 136616), PorSexo(2843, 2154)), Sanitario(75564, 10803), [Vivienda(0, 77743), Vivienda(1, 1970), Vivienda(2, 1643), Vivienda(3, 4208), Vivienda(4, 597), Vivienda(5, 56), Vivienda(6, 105), Vivienda(7, 45)]),
    Provincia(13, 'Mendoza', Alfabetismo(PorSexo(681053, 730907), PorSexo(15527, 16003)), Sanitario(421292, 38258), [Vivienda(0, 398510), Vivienda(1, 7618), Vivienda(2, 1985), Vivienda(3, 48846), Vivienda(4, 1686), Vivienda(5, 216), Vivienda(6, 595), Vivienda(7, 94)]),
    Provincia(14, 'Misiones', Alfabetismo(PorSexo(412901, 422882), PorSexo(17110, 18662)), Sanitario(201604, 88659), [Vivienda(0, 249745), Vivienda(1, 7866), Vivienda(2, 11548), Vivienda(3, 16938), Vivienda(4, 3376), Vivienda(5, 77), Vivienda(6, 560), Vivienda(7, 153)]),
    Provincia(15, 'Neuquén', Alfabetismo(PorSexo(219539, 225070), PorSexo(5120, 5339)), Sanitario(145697, 13605), [Vivienda(0, 130466), Vivienda(1, 1924), Vivienda(2, 3425), Vivienda(3, 21312), Vivienda(4, 1743), Vivienda(5, 83), Vivienda(6, 228), Vivienda(7, 121)]),
    Provincia(16, 'Río Negro', Alfabetismo(PorSexo(255390, 262917), PorSexo(6541, 6539)), Sanitario(171370, 19227), [Vivienda(0, 155561), Vivienda(1, 2149), Vivienda(2, 4091), Vivienda(3, 27071), Vivienda(4, 1230), Vivienda(5, 72), Vivienda(6, 331), Vivienda(7, 92)]),
    Provincia(17, 'Salta', Alfabetismo(PorSexo(459258, 478751), PorSexo(12710, 17657)), Sanitario(202113, 64962), [Vivienda(0, 220293), Vivienda(1, 14806), Vivienda(2, 11076), Vivienda(3, 17161), Vivienda(4, 2881), Vivienda(5, 120), Vivienda(6, 450), Vivienda(7, 288)]),
    Provincia(18, 'San Juan', Alfabetismo(PorSexo(260076, 278149), PorSexo(6360, 5133)), Sanitario(142970, 19234), [Vivienda(0, 134753), Vivienda(1, 11219), Vivienda(2, 1075), Vivienda(3, 14489), Vivienda(4, 405), Vivienda(5, 43), Vivienda(6, 196), Vivienda(7, 24)]),
    Provincia(19, 'San Luis', Alfabetismo(PorSexo(170030, 177358), PorSexo(3674, 2838)), Sanitario(108089, 9677), [Vivienda(0, 104692), Vivienda(1, 1125), Vivienda(2, 470), Vivienda(3, 10380), Vivienda(4, 654), Vivienda(5, 106), Vivienda(6, 208), Vivienda(7, 131)]),
    Provincia(20, 'Santa Cruz', Alfabetismo(PorSexo(113297, 106023), PorSexo(1291, 1213)), Sanitario(72841, 3392), [Vivienda(0, 64118), Vivienda(1, 524), Vivienda(2, 852), Vivienda(3, 9339), Vivienda(4, 1181), Vivienda(5, 43), Vivienda(6, 118), Vivienda(7, 58)]),
    Provincia(21, 'Santa Fe', Alfabetismo(PorSexo(1273525, 1383361), PorSexo(25003, 23092)), Sanitario(862253, 86116), [Vivienda(0, 793209), Vivienda(1, 10303), Vivienda(2, 8279), Vivienda(3, 132409), Vivienda(4, 2023), Vivienda(5, 796), Vivienda(6, 1119), Vivienda(7, 231)]),
    Provincia(22, 'Santiago del Estero', Alfabetismo(PorSexo(328348, 340598), PorSexo(14809, 13061)), Sanitario(122529, 75377), [Vivienda(0, 169162), Vivienda(1, 20833), Vivienda(2, 1097), Vivienda(3, 5830), Vivienda(4, 463), Vivienda(5, 75), Vivienda(6, 223), Vivienda(7, 223)]),
    Provincia(23, 'Tierra del Fuego, Antártida e Islas del Atlántico Sur', Alfabetismo(PorSexo(52991, 50430), PorSexo(347, 358)), Sanitario(35041, 1648), [Vivienda(0, 25108), Vivienda(1, 102), Vivienda(2, 3817), Vivienda(3, 7326), Vivienda(4, 226), Vivienda(5, 43), Vivienda(6, 44), Vivienda(7, 23)]),
    Provincia(24, 'Tucumán', Alfabetismo(PorSexo(557210, 596990), PorSexo(15859, 13295)), Sanitario(276897, 58924), [Vivienda(0, 287900), Vivienda(1, 4931), Vivienda(2, 11031), Vivienda(3, 30431), Vivienda(4, 897), Vivienda(5, 184), Vivienda(6, 344), Vivienda(7, 103)])
])











def mostrar_menu():
    print("Menu:")
    print("1. Show populations")
    print("2. Show ratio of inhabitants to homes")
    print("3. Show literacy by sex")
    print("4. Show literacy by province")
    print("5. Show homes without toilet by province")
    print("6. Show percentage of precarious housing by province")
    print("7. Show earrings and show plot with slopes")
    print("0. Salir")

# Simple Menu
while True:
    mostrar_menu()
    
    opcion = input("Selecciona una opción (0-7): ")

    if opcion == "0":
        print("¡Hasta luego!")
        break
    elif opcion == "1":
        print(arg.get_provincia(1))
        print(arg.get_total_poblacion())
        print(arg.mostrar_totales_poblacion())
    elif opcion == "2":
        print(arg.mostrar_ratio_habitantes_por_vivienda_por_provincia())
    elif opcion == "3":
        print(arg.mostrar_porcentaje_analfabetismo_por_sexo())
    elif opcion == "4":
        print(arg.mostrar_porcentaje_analfabetismo_por_prov())
    elif opcion == "5":
        print(arg.mostrar_porcentaje_vivendas_sin_retrete_por_prov())
    elif opcion == "6":
        print(arg.mostrar_porcentaje_vivienda_precaria_por_prov())
    elif opcion == "7":
        # Obtener los datos directamente de las funciones
        nombres_provincias_precaria, porcentaje_viviendas_precarias = arg.mostrar_porcentaje_vivienda_precaria_por_provincia()
        nombres_provincias_sin_retrete, porcentaje_viviendas_sin_retrete = arg.mostrar_porcentaje_vivendas_sin_retrete_por_provincia()
        nombres_provincias_alfabetizadas, porcentaje_viviendas_sin_alfabetizar = arg.alfabetismo_ordenado_asc()

        # Reshape para tener las dimensiones correctas
        porcentaje_viviendas_precarias = np.array(porcentaje_viviendas_precarias).reshape(-1, 1)
        porcentaje_viviendas_sin_retrete = np.array(porcentaje_viviendas_sin_retrete).reshape(-1, 1)
        porcentaje_viviendas_sin_alfabetizar = np.array(porcentaje_viviendas_sin_alfabetizar).reshape(-1, 1)

        # Crear modelos de regresión lineal
        modelo_precaria = LinearRegression()
        modelo_sin_retrete = LinearRegression()
        modelo_sin_alfabetizar = LinearRegression()

        # Ajustar los modelos a los datos
        modelo_precaria.fit(np.arange(len(porcentaje_viviendas_precarias)).reshape(-1, 1), porcentaje_viviendas_precarias)
        modelo_sin_retrete.fit(np.arange(len(porcentaje_viviendas_sin_retrete)).reshape(-1, 1), porcentaje_viviendas_sin_retrete)
        modelo_sin_alfabetizar.fit(np.arange(len(porcentaje_viviendas_sin_alfabetizar)).reshape(-1, 1), porcentaje_viviendas_sin_alfabetizar)

        # Obtener las pendientes de los modelos
        pendiente_precaria = modelo_precaria.coef_[0]
        pendiente_sin_retrete = modelo_sin_retrete.coef_[0]
        pendiente_sin_alfabetizar = modelo_sin_alfabetizar.coef_[0]

        # Imprimir las pendientes
        print("Slope for percentage of precarious housing:", pendiente_precaria)
        print("Slope for percentage of homes without toilets:", pendiente_sin_retrete)
        print("Slope for percentage of non-literate households:", pendiente_sin_alfabetizar)
        plt.scatter(np.arange(len(porcentaje_viviendas_precarias)), porcentaje_viviendas_precarias, label='Precarious Housing', color='red')
        plt.scatter(np.arange(len(porcentaje_viviendas_sin_retrete)), porcentaje_viviendas_sin_retrete, label='Homes Without Toilet', color='blue')
        plt.scatter(np.arange(len(porcentaje_viviendas_sin_alfabetizar)), porcentaje_viviendas_sin_alfabetizar, label='Unliterate Housing', color='green')
        plt.plot(np.arange(len(porcentaje_viviendas_precarias)), modelo_precaria.predict(np.arange(len(porcentaje_viviendas_precarias)).reshape(-1, 1)), color='red')
        plt.plot(np.arange(len(porcentaje_viviendas_sin_retrete)), modelo_sin_retrete.predict(np.arange(len(porcentaje_viviendas_sin_retrete)).reshape(-1, 1)), color='blue')
        plt.plot(np.arange(len(porcentaje_viviendas_sin_alfabetizar)), modelo_sin_alfabetizar.predict(np.arange(len(porcentaje_viviendas_sin_alfabetizar)).reshape(-1, 1)), color='green')
        plt.xlabel('States')
        plt.ylabel('Percentage')
        plt.legend()
        plt.show()       
    else:
        print("Invalid option. Enter a number from 0 to 8.")