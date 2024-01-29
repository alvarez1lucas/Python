"""
Autor: Alvarez Lucas
Fecha: 23/03/2023
Contenido: Resolución de la lista de ejercicios 1
"""


estadisticas = [
  {
  'Estación' : 'LA QUIACA OBS.', 
	'Temperatura (°C)' : {
            'Ene' : 12.8, 'Feb' : 12.5, 'Mar' : 12.4, 'Abr' : 10.9, 'May' : 6.9, 'Jun' : 4.4, 'Jul' : 4.1, 'Ago' : 6.7, 'Sep' : 9.3, 'Oct' : 11.7, 'Nov' : 12.8, 'Dic' : 13.2},
	'Temperatura máxima (°C)' : {
            'Ene' : 20.1, 'Feb' : 19.9, 'Mar' : 19.9, 'Abr' : 19.7, 'May' : 17.3, 'Jun' : 15.6, 'Jul' : 15.4, 'Ago' : 17.4, 'Sep' : 19.2, 'Oct' : 21.1, 'Nov' : 21.7, 'Dic' : 21.3},
	'Temperatura mínima (°C)' : {
            'Ene' : 7.4, 'Feb' : 7.0, 'Mar' : 6.3, 'Abr' : 2.8, 'May' : -3.0, 'Jun' : -6.2, 'Jul' : -6.8, 'Ago' : -4.2, 'Sep' : -1.1, 'Oct' : 2.8, 'Nov' : 5.2, 'Dic' : 6.9},
	'Humedad relativa (%)' : {
            'Ene' : 65.3, 'Feb' : 64.1, 'Mar' : 62.4, 'Abr' : 48.2, 'May' : 34.6, 'Jun' : 31.1, 'Jul' : 30.1, 'Ago' : 31.7, 'Sep' : 34.4, 'Oct' : 45.3, 'Nov' : 52.3, 'Dic' : 59.2},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 6.9, 'Feb' : 7.1, 'Mar' : 6.5, 'Abr' : 6.4, 'May' : 6.0, 'Jun' : 4.9, 'Jul' : 6.6, 'Ago' : 6.6, 'Sep' : 8.6, 'Oct' : 8.7, 'Nov' : 8.8, 'Dic' : 8.3},
	'Nubosidad total (octavos)' : {
            'Ene' : 5.2, 'Feb' : 4.8, 'Mar' : 4.1, 'Abr' : 2.7, 'May' : 1.8, 'Jun' : 1.6, 'Jul' : 1.4, 'Ago' : 1.6, 'Sep' : 2.0, 'Oct' : 3.0, 'Nov' : 3.6, 'Dic' : 4.5},
	'Precipitación (mm)' : {
            'Ene' : 97.5, 'Feb' : 68.4, 'Mar' : 55.9, 'Abr' : 8.2, 'May' : 1.0, 'Jun' : 0.5, 'Jul' : 0.0, 'Ago' : 1.4, 'Sep' : 3.5, 'Oct' : 16.0, 'Nov' : 27.3, 'Dic' : 71.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 15.9, 'Feb' : 12.2, 'Mar' : 9.8, 'Abr' : 2.4, 'May' : 0.3, 'Jun' : 0.1, 'Jul' : 0.0, 'Ago' : 0.4, 'Sep' : 0.9, 'Oct' : 3.5, 'Nov' : 7.4, 'Dic' : 12.7},
  },
{
	'Estación' : 'ORÁN AERO', 
	'Temperatura (°C)' : {
            'Ene' : None, 'Feb' : 25.1, 'Mar' : 23.9, 'Abr' : 20.9, 'May' : 17.7, 'Jun' : 15.0, 'Jul' : 14.7, 'Ago' : 17.2, 'Sep' : 20.1, 'Oct' : 23.8, 'Nov' : 25.0, 'Dic' : 26.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 32.3, 'Feb' : 31.1, 'Mar' : 29.4, 'Abr' : 26.0, 'May' : 23.2, 'Jun' : 21.2, 'Jul' : 22.0, 'Ago' : 25.6, 'Sep' : 28.3, 'Oct' : 31.5, 'Nov' : 32.0, 'Dic' : 32.6},
	'Temperatura mínima (°C)' : {
            'Ene' : 21.5, 'Feb' : 20.8, 'Mar' : 20.5, 'Abr' : 17.8, 'May' : 14.2, 'Jun' : 11.0, 'Jul' : 9.2, 'Ago' : 11.0, 'Sep' : 13.5, 'Oct' : 17.9, 'Nov' : 19.5, 'Dic' : 21.2},
	'Humedad relativa (%)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : 83.6, 'Abr' : 85.3, 'May' : 83.8, 'Jun' : 82.3, 'Jul' : 75.4, 'Ago' : 67.3, 'Sep' : 59.1, 'Oct' : 62.5, 'Nov' : 69.6, 'Dic' : 74.7},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 8.4, 'Feb' : 8.4, 'Mar' : 6.9, 'Abr' : 6.4, 'May' : 6.2, 'Jun' : 6.8, 'Jul' : 7.7, 'Ago' : 8.2, 'Sep' : 9.1, 'Oct' : 9.2, 'Nov' : 9.6, 'Dic' : 8.6},
	'Nubosidad total (octavos)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : 5.7, 'Abr' : 6.0, 'May' : 5.6, 'Jun' : 5.1, 'Jul' : 4.0, 'Ago' : 3.5, 'Sep' : 3.9, 'Oct' : 4.6, 'Nov' : 5.0, 'Dic' : 5.3},
	'Precipitación (mm)' : {
            'Ene' : 216.6, 'Feb' : 183.7, 'Mar' : 184.2, 'Abr' : 70.9, 'May' : 19.8, 'Jun' : 6.3, 'Jul' : 4.5, 'Ago' : 5.4, 'Sep' : 16.3, 'Oct' : 60.0, 'Nov' : 108.1, 'Dic' : 170.1},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 14.3, 'Feb' : 12.9, 'Mar' : 15.3, 'Abr' : 12.0, 'May' : 6.6, 'Jun' : 3.9, 'Jul' : 2.8, 'Ago' : 2.2, 'Sep' : 3.2, 'Oct' : 7.1, 'Nov' : 10.4, 'Dic' : 12.9},
},
{
	'Estación' : 'TARTAGAL AERO', 
	'Temperatura (°C)' : {
            'Ene' : 25.2, 'Feb' : 24.4, 'Mar' : None, 'Abr' : 20.2, 'May' : 17.2, 'Jun' : 14.9, 'Jul' : 14.6, 'Ago' : 17.4, 'Sep' : 20.2, 'Oct' : 23.9, 'Nov' : 24.6, 'Dic' : 25.3},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.7, 'Feb' : 30.7, 'Mar' : 29.1, 'Abr' : 25.5, 'May' : 22.7, 'Jun' : 21.0, 'Jul' : 22.1, 'Ago' : 25.5, 'Sep' : 28.2, 'Oct' : 31.4, 'Nov' : 31.7, 'Dic' : 32.0},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.6, 'Feb' : 20.0, 'Mar' : 19.6, 'Abr' : 17.0, 'May' : 13.2, 'Jun' : 10.7, 'Jul' : 9.1, 'Ago' : 10.6, 'Sep' : 13.2, 'Oct' : 17.5, 'Nov' : 18.8, 'Dic' : 20.3},
	'Humedad relativa (%)' : {
            'Ene' : 78.5, 'Feb' : None, 'Mar' : None, 'Abr' : 85.0, 'May' : 83.5, 'Jun' : 80.8, 'Jul' : 71.9, 'Ago' : 62.0, 'Sep' : 55.1, 'Oct' : 60.1, 'Nov' : 67.1, 'Dic' : 74.4},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 6.1, 'Feb' : 5.9, 'Mar' : 5.2, 'Abr' : 4.7, 'May' : 4.6, 'Jun' : 4.6, 'Jul' : 5.6, 'Ago' : 6.7, 'Sep' : 7.3, 'Oct' : 8.1, 'Nov' : 8.6, 'Dic' : 7.1},
	'Nubosidad total (octavos)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Precipitación (mm)' : {
            'Ene' : 200.2, 'Feb' : 182.8, 'Mar' : 187.7, 'Abr' : 65.3, 'May' : 22.0, 'Jun' : 6.7, 'Jul' : 3.6, 'Ago' : 5.1, 'Sep' : 15.1, 'Oct' : 45.0, 'Nov' : 110.0, 'Dic' : 176.4},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 11.6, 'Feb' : 11.1, 'Mar' : 11.7, 'Abr' : 10.5, 'May' : 5.9, 'Jun' : 3.6, 'Jul' : 2.2, 'Ago' : 1.7, 'Sep' : 2.4, 'Oct' : 5.1, 'Nov' : 9.0, 'Dic' : 11.4},
},
{
	'Estación' : 'JUJUY AERO', 
	'Temperatura (°C)' : {
            'Ene' : 23.6, 'Feb' : 22.5, 'Mar' : 21.4, 'Abr' : 18.3, 'May' : 14.8, 'Jun' : 12.2, 'Jul' : 11.9, 'Ago' : 15.0, 'Sep' : 17.8, 'Oct' : 21.7, 'Nov' : 23.0, 'Dic' : 23.8},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.0, 'Feb' : 28.8, 'Mar' : 27.2, 'Abr' : 24.0, 'May' : 21.3, 'Jun' : 19.7, 'Jul' : 20.3, 'Ago' : 23.3, 'Sep' : 25.7, 'Oct' : 29.0, 'Nov' : 29.9, 'Dic' : 30.5},
	'Temperatura mínima (°C)' : {
            'Ene' : 18.3, 'Feb' : 17.5, 'Mar' : 17.1, 'Abr' : 14.0, 'May' : 10.0, 'Jun' : 6.8, 'Jul' : 5.8, 'Ago' : 8.2, 'Sep' : 10.6, 'Oct' : 14.8, 'Nov' : 16.7, 'Dic' : 18.0},
	'Humedad relativa (%)' : {
            'Ene' : 74.4, 'Feb' : 77.7, 'Mar' : 82.0, 'Abr' : 82.4, 'May' : 79.7, 'Jun' : 76.7, 'Jul' : 68.0, 'Ago' : 58.7, 'Sep' : 52.3, 'Oct' : 56.0, 'Nov' : 62.0, 'Dic' : 68.8},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 8.2, 'Feb' : 8.3, 'Mar' : 7.3, 'Abr' : 7.1, 'May' : 7.4, 'Jun' : 7.3, 'Jul' : 9.2, 'Ago' : 10.3, 'Sep' : 11.0, 'Oct' : 10.7, 'Nov' : 10.2, 'Dic' : 8.9},
	'Nubosidad total (octavos)' : {
            'Ene' : 5.3, 'Feb' : 5.2, 'Mar' : 5.4, 'Abr' : 5.3, 'May' : 4.7, 'Jun' : 4.1, 'Jul' : 3.2, 'Ago' : 3.1, 'Sep' : 3.4, 'Oct' : 4.1, 'Nov' : 4.5, 'Dic' : 5.0},
	'Precipitación (mm)' : {
            'Ene' : 153.2, 'Feb' : 152.9, 'Mar' : 138.9, 'Abr' : 49.4, 'May' : 11.6, 'Jun' : 2.8, 'Jul' : 3.4, 'Ago' : 3.1, 'Sep' : 5.4, 'Oct' : 28.1, 'Nov' : 61.1, 'Dic' : 130.4},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 13.4, 'Feb' : 12.5, 'Mar' : 14.1, 'Abr' : 8.7, 'May' : 3.9, 'Jun' : 2.0, 'Jul' : 2.3, 'Ago' : 1.6, 'Sep' : 1.9, 'Oct' : 4.8, 'Nov' : 7.8, 'Dic' : 11.6},
},
{
	'Estación' : 'SALTA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 21.4, 'Feb' : 20.3, 'Mar' : 19.5, 'Abr' : 16.6, 'May' : 13.1, 'Jun' : 10.6, 'Jul' : 10.1, 'Ago' : 12.7, 'Sep' : 15.1, 'Oct' : 19.1, 'Nov' : 20.5, 'Dic' : 21.5},
	'Temperatura máxima (°C)' : {
            'Ene' : 27.4, 'Feb' : 26.4, 'Mar' : 25.2, 'Abr' : 22.7, 'May' : 20.3, 'Jun' : 19.6, 'Jul' : 20.0, 'Ago' : 22.3, 'Sep' : 23.9, 'Oct' : 26.8, 'Nov' : 27.5, 'Dic' : 28.0},
	'Temperatura mínima (°C)' : {
            'Ene' : 16.6, 'Feb' : 15.7, 'Mar' : 15.3, 'Abr' : 11.9, 'May' : 7.6, 'Jun' : 4.1, 'Jul' : 2.9, 'Ago' : 4.9, 'Sep' : 7.3, 'Oct' : 11.8, 'Nov' : 14.1, 'Dic' : 15.9},
	'Humedad relativa (%)' : {
            'Ene' : 78.2, 'Feb' : 81.0, 'Mar' : 83.7, 'Abr' : 82.9, 'May' : 80.5, 'Jun' : 75.5, 'Jul' : 69.1, 'Ago' : 62.8, 'Sep' : 58.2, 'Oct' : 61.2, 'Nov' : 67.1, 'Dic' : 73.1},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 6.8, 'Feb' : 6.5, 'Mar' : 5.8, 'Abr' : 5.8, 'May' : 6.3, 'Jun' : 6.1, 'Jul' : 6.9, 'Ago' : 7.5, 'Sep' : 7.9, 'Oct' : 9.0, 'Nov' : 8.7, 'Dic' : 7.7},
	'Nubosidad total (octavos)' : {
            'Ene' : 5.9, 'Feb' : 5.8, 'Mar' : 5.9, 'Abr' : 5.6, 'May' : 5.0, 'Jun' : 4.2, 'Jul' : 3.3, 'Ago' : 3.2, 'Sep' : 3.5, 'Oct' : 4.4, 'Nov' : 5.0, 'Dic' : 5.5},
	'Precipitación (mm)' : {
            'Ene' : 192.6, 'Feb' : 154.2, 'Mar' : 110.6, 'Abr' : 33.0, 'May' : 8.0, 'Jun' : 1.5, 'Jul' : 3.9, 'Ago' : 3.8, 'Sep' : 7.6, 'Oct' : 25.1, 'Nov' : 62.2, 'Dic' : 145.6},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 16.3, 'Feb' : 14.8, 'Mar' : 14.2, 'Abr' : 7.9, 'May' : 3.9, 'Jun' : 1.6, 'Jul' : 2.1, 'Ago' : 2.1, 'Sep' : 2.7, 'Oct' : 5.7, 'Nov' : 9.5, 'Dic' : 14.0},
},
{
	'Estación' : 'LAS LOMITAS', 
	'Temperatura (°C)' : {
            'Ene' : 27.9, 'Feb' : 26.8, 'Mar' : 25.8, 'Abr' : 22.5, 'May' : 18.8, 'Jun' : 16.9, 'Jul' : 16.6, 'Ago' : 19.1, 'Sep' : 21.2, 'Oct' : 24.6, 'Nov' : 25.9, 'Dic' : 27.3},
	'Temperatura máxima (°C)' : {
            'Ene' : 35.1, 'Feb' : 33.8, 'Mar' : 32.8, 'Abr' : 28.8, 'May' : 25.4, 'Jun' : 23.4, 'Jul' : 24.1, 'Ago' : 27.1, 'Sep' : 29.1, 'Oct' : 32.2, 'Nov' : 33.2, 'Dic' : 34.4},
	'Temperatura mínima (°C)' : {
            'Ene' : 21.7, 'Feb' : 21.1, 'Mar' : 20.3, 'Abr' : 17.5, 'May' : 13.7, 'Jun' : 11.8, 'Jul' : 10.4, 'Ago' : 12.2, 'Sep' : 14.2, 'Oct' : 17.8, 'Nov' : 19.3, 'Dic' : 20.9},
	'Humedad relativa (%)' : {
            'Ene' : 69.3, 'Feb' : 72.2, 'Mar' : 75.2, 'Abr' : 79.4, 'May' : 79.9, 'Jun' : 79.3, 'Jul' : 71.3, 'Ago' : 62.8, 'Sep' : 60.5, 'Oct' : 62.7, 'Nov' : 65.9, 'Dic' : 68.2},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 5.4, 'Feb' : 7.0, 'Mar' : 6.0, 'Abr' : 5.9, 'May' : 5.8, 'Jun' : 5.3, 'Jul' : 6.9, 'Ago' : 8.6, 'Sep' : 8.7, 'Oct' : 9.4, 'Nov' : 9.9, 'Dic' : 8.2},
	'Nubosidad total (octavos)' : {
            'Ene' : 4.0, 'Feb' : 3.9, 'Mar' : 3.5, 'Abr' : 4.2, 'May' : 4.1, 'Jun' : 4.4, 'Jul' : 3.5, 'Ago' : 3.1, 'Sep' : 3.5, 'Oct' : 3.7, 'Nov' : 3.7, 'Dic' : 3.8},
	'Precipitación (mm)' : {
            'Ene' : 142.4, 'Feb' : 116.7, 'Mar' : 160.4, 'Abr' : 84.6, 'May' : 57.5, 'Jun' : 18.6, 'Jul' : 13.1, 'Ago' : 16.1, 'Sep' : 30.4, 'Oct' : 72.5, 'Nov' : 119.0, 'Dic' : 132.6},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.8, 'Feb' : 9.2, 'Mar' : 9.9, 'Abr' : 9.3, 'May' : 7.1, 'Jun' : 6.0, 'Jul' : 3.9, 'Ago' : 2.9, 'Sep' : 4.4, 'Oct' : 7.3, 'Nov' : 8.7, 'Dic' : 8.8},
},
{
	'Estación' : 'IGUAZÚ AERO', 
	'Temperatura (°C)' : {
            'Ene' : 25.6, 'Feb' : 24.9, 'Mar' : 24.2, 'Abr' : 21.4, 'May' : 17.6, 'Jun' : 15.9, 'Jul' : 15.7, 'Ago' : 17.6, 'Sep' : 19.1, 'Oct' : 21.9, 'Nov' : 23.5, 'Dic' : 25.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.8, 'Feb' : 31.2, 'Mar' : 30.7, 'Abr' : 27.5, 'May' : 23.5, 'Jun' : 21.7, 'Jul' : 22.2, 'Ago' : 24.7, 'Sep' : 25.8, 'Oct' : 28.3, 'Nov' : 30.1, 'Dic' : 31.4},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.5, 'Feb' : 20.2, 'Mar' : 19.3, 'Abr' : 16.8, 'May' : 13.1, 'Jun' : 11.7, 'Jul' : 10.8, 'Ago' : 12.2, 'Sep' : 13.7, 'Oct' : 16.5, 'Nov' : 17.8, 'Dic' : 19.5},
	'Humedad relativa (%)' : {
            'Ene' : 78.1, 'Feb' : 80.4, 'Mar' : 79.7, 'Abr' : 83.7, 'May' : 86.5, 'Jun' : 88.1, 'Jul' : 83.6, 'Ago' : 78.5, 'Sep' : 76.4, 'Oct' : 77.3, 'Nov' : 74.9, 'Dic' : 75.7},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 6.4, 'Feb' : 6.3, 'Mar' : 5.3, 'Abr' : 6.1, 'May' : 6.4, 'Jun' : 6.2, 'Jul' : 7.4, 'Ago' : 8.4, 'Sep' : 8.8, 'Oct' : 7.4, 'Nov' : 7.5, 'Dic' : 6.6},
	'Nubosidad total (octavos)' : {
            'Ene' : 4.2, 'Feb' : 4.3, 'Mar' : 3.6, 'Abr' : 3.7, 'May' : 3.6, 'Jun' : 4.0, 'Jul' : 3.4, 'Ago' : 3.5, 'Sep' : 4.0, 'Oct' : 4.1, 'Nov' : 3.7, 'Dic' : 3.9},
	'Precipitación (mm)' : {
            'Ene' : 177.7, 'Feb' : 154.7, 'Mar' : 126.5, 'Abr' : 169.1, 'May' : 192.7, 'Jun' : 148.3, 'Jul' : 115.8, 'Ago' : 94.2, 'Sep' : 160.3, 'Oct' : 237.0, 'Nov' : 186.3, 'Dic' : 186.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 10.3, 'Feb' : 10.2, 'Mar' : 8.1, 'Abr' : 8.9, 'May' : 8.8, 'Jun' : 8.6, 'Jul' : 8.3, 'Ago' : 6.8, 'Sep' : 9.6, 'Oct' : 11.6, 'Nov' : 9.4, 'Dic' : 9.9},
},
{
	'Estación' : 'TUCUMÁN AERO', 
	'Temperatura (°C)' : {
            'Ene' : 25.2, 'Feb' : 24.0, 'Mar' : 22.6, 'Abr' : 19.2, 'May' : 15.7, 'Jun' : 12.7, 'Jul' : 12.2, 'Ago' : 14.9, 'Sep' : 17.8, 'Oct' : 21.8, 'Nov' : 23.4, 'Dic' : 24.9},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.0, 'Feb' : 29.7, 'Mar' : 27.9, 'Abr' : 24.6, 'May' : 21.2, 'Jun' : 18.6, 'Jul' : 19.3, 'Ago' : 22.8, 'Sep' : 25.4, 'Oct' : 28.9, 'Nov' : 29.9, 'Dic' : 30.8},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.1, 'Feb' : 19.3, 'Mar' : 18.5, 'Abr' : 15.1, 'May' : 11.4, 'Jun' : 8.2, 'Jul' : 6.8, 'Ago' : 8.5, 'Sep' : 11.0, 'Oct' : 15.2, 'Nov' : 17.5, 'Dic' : 19.3},
	'Humedad relativa (%)' : {
            'Ene' : 74.2, 'Feb' : 76.8, 'Mar' : 81.0, 'Abr' : 81.2, 'May' : 80.3, 'Jun' : 78.9, 'Jul' : 70.9, 'Ago' : 62.1, 'Sep' : 58.4, 'Oct' : 61.5, 'Nov' : 67.1, 'Dic' : 70.8},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 11.6, 'Feb' : 11.3, 'Mar' : 10.0, 'Abr' : 9.6, 'May' : 9.4, 'Jun' : 9.7, 'Jul' : 10.7, 'Ago' : 11.2, 'Sep' : 11.8, 'Oct' : 12.2, 'Nov' : 12.0, 'Dic' : 11.1},
	'Nubosidad total (octavos)' : {
            'Ene' : 5.0, 'Feb' : 5.1, 'Mar' : 5.2, 'Abr' : 5.1, 'May' : 4.7, 'Jun' : 4.6, 'Jul' : 3.4, 'Ago' : 3.3, 'Sep' : 3.5, 'Oct' : 4.2, 'Nov' : 4.7, 'Dic' : 4.8},
	'Precipitación (mm)' : {
            'Ene' : 230.6, 'Feb' : 172.3, 'Mar' : 151.1, 'Abr' : 62.5, 'May' : 25.9, 'Jun' : 13.1, 'Jul' : 7.4, 'Ago' : 8.5, 'Sep' : 16.1, 'Oct' : 65.1, 'Nov' : 103.0, 'Dic' : 175.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 13.7, 'Feb' : 11.5, 'Mar' : 12.9, 'Abr' : 9.6, 'May' : 6.9, 'Jun' : 5.2, 'Jul' : 3.3, 'Ago' : 2.1, 'Sep' : 3.3, 'Oct' : 7.3, 'Nov' : 10.8, 'Dic' : 12.1},
},
{
	'Estación' : 'SANTIAGO DEL ESTERO AERO', 
	'Temperatura (°C)' : {
            'Ene' : 26.7, 'Feb' : 25.5, 'Mar' : 23.8, 'Abr' : 19.8, 'May' : 16.1, 'Jun' : 12.7, 'Jul' : 12.2, 'Ago' : 15.3, 'Sep' : 18.5, 'Oct' : 22.7, 'Nov' : 24.8, 'Dic' : 26.5},
	'Temperatura máxima (°C)' : {
            'Ene' : 33.9, 'Feb' : 32.5, 'Mar' : 30.4, 'Abr' : 26.3, 'May' : 23.1, 'Jun' : 20.1, 'Jul' : 20.9, 'Ago' : 24.4, 'Sep' : 26.9, 'Oct' : 30.7, 'Nov' : 32.2, 'Dic' : 33.7},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.5, 'Feb' : 19.7, 'Mar' : 18.5, 'Abr' : 14.6, 'May' : 10.4, 'Jun' : 6.8, 'Jul' : 5.0, 'Ago' : 7.3, 'Sep' : 10.3, 'Oct' : 15.3, 'Nov' : 17.8, 'Dic' : 20.0},
	'Humedad relativa (%)' : {
            'Ene' : 66.8, 'Feb' : 70.0, 'Mar' : 74.2, 'Abr' : 76.6, 'May' : 74.5, 'Jun' : 73.2, 'Jul' : 63.6, 'Ago' : 54.3, 'Sep' : 50.9, 'Oct' : 54.8, 'Nov' : 59.0, 'Dic' : 62.7},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 9.2, 'Feb' : 9.2, 'Mar' : 8.6, 'Abr' : 7.8, 'May' : 7.3, 'Jun' : 7.1, 'Jul' : 8.2, 'Ago' : 9.0, 'Sep' : 10.2, 'Oct' : 11.6, 'Nov' : 10.9, 'Dic' : 10.0},
	'Nubosidad total (octavos)' : {
            'Ene' : 4.0, 'Feb' : 4.1, 'Mar' : 4.3, 'Abr' : 4.5, 'May' : 4.2, 'Jun' : 4.2, 'Jul' : 3.1, 'Ago' : 2.9, 'Sep' : 3.2, 'Oct' : 3.6, 'Nov' : 3.8, 'Dic' : 3.9},
	'Precipitación (mm)' : {
            'Ene' : 134.8, 'Feb' : 100.6, 'Mar' : 91.1, 'Abr' : 35.9, 'May' : 17.2, 'Jun' : 6.6, 'Jul' : 3.0, 'Ago' : 2.0, 'Sep' : 12.3, 'Oct' : 44.7, 'Nov' : 66.7, 'Dic' : 114.2},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 9.8, 'Feb' : 8.7, 'Mar' : 9.5, 'Abr' : 7.1, 'May' : 4.5, 'Jun' : 3.9, 'Jul' : 1.9, 'Ago' : 1.3, 'Sep' : 2.2, 'Oct' : 5.9, 'Nov' : 7.2, 'Dic' : 8.9},
},
{
	'Estación' : 'RESISTENCIA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 26.8, 'Feb' : 25.9, 'Mar' : 24.6, 'Abr' : 21.2, 'May' : 17.6, 'Jun' : 15.4, 'Jul' : 14.8, 'Ago' : 16.7, 'Sep' : 18.5, 'Oct' : 21.8, 'Nov' : 23.6, 'Dic' : 25.8},
	'Temperatura máxima (°C)' : {
            'Ene' : 33.3, 'Feb' : 32.1, 'Mar' : 30.7, 'Abr' : 26.9, 'May' : 23.6, 'Jun' : 21.3, 'Jul' : 21.4, 'Ago' : 23.7, 'Sep' : 25.3, 'Oct' : 28.1, 'Nov' : 29.8, 'Dic' : 32.1},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.9, 'Feb' : 20.5, 'Mar' : 19.5, 'Abr' : 16.5, 'May' : 12.6, 'Jun' : 10.8, 'Jul' : 9.5, 'Ago' : 10.8, 'Sep' : 12.4, 'Oct' : 15.9, 'Nov' : 17.7, 'Dic' : 19.7},
	'Humedad relativa (%)' : {
            'Ene' : 70.8, 'Feb' : 74.5, 'Mar' : 77.4, 'Abr' : 81.0, 'May' : 81.7, 'Jun' : 82.5, 'Jul' : 77.3, 'Ago' : 72.5, 'Sep' : 70.6, 'Oct' : 71.8, 'Nov' : 72.0, 'Dic' : 70.8},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 10.1, 'Feb' : 10.5, 'Mar' : 9.9, 'Abr' : 9.8, 'May' : 9.8, 'Jun' : 10.0, 'Jul' : 11.2, 'Ago' : 12.7, 'Sep' : 13.8, 'Oct' : 13.4, 'Nov' : 12.5, 'Dic' : 10.7},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.7, 'Feb' : 3.8, 'Mar' : 3.5, 'Abr' : 4.1, 'May' : 3.8, 'Jun' : 4.4, 'Jul' : 3.7, 'Ago' : 3.6, 'Sep' : 3.8, 'Oct' : 3.7, 'Nov' : 3.5, 'Dic' : 3.6},
	'Precipitación (mm)' : {
            'Ene' : 161.1, 'Feb' : 165.6, 'Mar' : 174.4, 'Abr' : 202.3, 'May' : 78.4, 'Jun' : 63.8, 'Jul' : 30.6, 'Ago' : 38.0, 'Sep' : 68.9, 'Oct' : 134.7, 'Nov' : 168.2, 'Dic' : 146.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.9, 'Feb' : 9.1, 'Mar' : 9.2, 'Abr' : 9.6, 'May' : 7.1, 'Jun' : 7.9, 'Jul' : 5.6, 'Ago' : 5.0, 'Sep' : 7.6, 'Oct' : 10.1, 'Nov' : 10.0, 'Dic' : 9.1},
},
{
	'Estación' : 'FORMOSA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 27.6, 'Feb' : 26.8, 'Mar' : 25.7, 'Abr' : 22.5, 'May' : 18.9, 'Jun' : 17.0, 'Jul' : 16.3, 'Ago' : 18.1, 'Sep' : 19.8, 'Oct' : 23.0, 'Nov' : 24.7, 'Dic' : 26.7},
	'Temperatura máxima (°C)' : {
            'Ene' : 33.8, 'Feb' : 32.8, 'Mar' : 31.9, 'Abr' : 28.1, 'May' : 24.4, 'Jun' : 22.4, 'Jul' : 22.3, 'Ago' : 24.8, 'Sep' : 26.3, 'Oct' : 29.0, 'Nov' : 30.7, 'Dic' : 32.8},
	'Temperatura mínima (°C)' : {
            'Ene' : 22.3, 'Feb' : 21.9, 'Mar' : 20.9, 'Abr' : 18.2, 'May' : 14.6, 'Jun' : 12.9, 'Jul' : 11.7, 'Ago' : 13.0, 'Sep' : 14.5, 'Oct' : 17.9, 'Nov' : 19.4, 'Dic' : 21.3},
	'Humedad relativa (%)' : {
            'Ene' : 71.2, 'Feb' : 74.3, 'Mar' : 75.9, 'Abr' : 79.5, 'May' : 80.2, 'Jun' : 80.8, 'Jul' : 76.5, 'Ago' : 71.6, 'Sep' : 70.2, 'Oct' : 71.8, 'Nov' : 71.4, 'Dic' : 70.8},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 11.8, 'Feb' : 11.9, 'Mar' : 11.2, 'Abr' : 11.5, 'May' : 11.6, 'Jun' : 11.9, 'Jul' : 13.1, 'Ago' : 14.4, 'Sep' : 14.9, 'Oct' : 14.9, 'Nov' : 14.4, 'Dic' : 13.0},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.9, 'Feb' : 3.9, 'Mar' : 3.6, 'Abr' : 4.0, 'May' : 3.9, 'Jun' : 4.4, 'Jul' : 3.8, 'Ago' : 3.6, 'Sep' : 3.8, 'Oct' : 3.9, 'Nov' : 3.6, 'Dic' : 3.7},
	'Precipitación (mm)' : {
            'Ene' : 165.7, 'Feb' : 128.7, 'Mar' : 144.8, 'Abr' : 175.0, 'May' : 99.3, 'Jun' : 68.9, 'Jul' : 47.5, 'Ago' : 44.2, 'Sep' : 90.8, 'Oct' : 142.0, 'Nov' : 166.5, 'Dic' : 163.4},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 9.1, 'Feb' : 8.9, 'Mar' : 8.5, 'Abr' : 9.2, 'May' : 7.7, 'Jun' : 7.2, 'Jul' : 5.5, 'Ago' : 5.8, 'Sep' : 7.6, 'Oct' : 9.6, 'Nov' : 9.1, 'Dic' : 9.1},
},
{
	'Estación' : 'CORRIENTES AERO', 
	'Temperatura (°C)' : {
            'Ene' : 27.0, 'Feb' : 26.0, 'Mar' : 24.7, 'Abr' : 21.4, 'May' : 18.0, 'Jun' : 15.9, 'Jul' : 15.2, 'Ago' : 17.0, 'Sep' : 18.5, 'Oct' : 21.8, 'Nov' : 23.7, 'Dic' : 25.8},
	'Temperatura máxima (°C)' : {
            'Ene' : 33.2, 'Feb' : 31.9, 'Mar' : 30.6, 'Abr' : 26.8, 'May' : 23.4, 'Jun' : 21.0, 'Jul' : 21.1, 'Ago' : 23.4, 'Sep' : 24.9, 'Oct' : 27.9, 'Nov' : 29.5, 'Dic' : 31.9},
	'Temperatura mínima (°C)' : {
            'Ene' : 21.3, 'Feb' : 20.8, 'Mar' : 19.7, 'Abr' : 16.9, 'May' : 13.4, 'Jun' : 11.6, 'Jul' : 10.4, 'Ago' : 11.5, 'Sep' : 13.1, 'Oct' : 16.3, 'Nov' : 17.9, 'Dic' : 20.1},
	'Humedad relativa (%)' : {
            'Ene' : 70.7, 'Feb' : 74.6, 'Mar' : 77.7, 'Abr' : 80.2, 'May' : 80.0, 'Jun' : 81.2, 'Jul' : 76.5, 'Ago' : 72.3, 'Sep' : 70.8, 'Oct' : 72.3, 'Nov' : 72.1, 'Dic' : 70.9},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 11.9, 'Feb' : 12.2, 'Mar' : 11.8, 'Abr' : 11.9, 'May' : 11.9, 'Jun' : 12.1, 'Jul' : 13.4, 'Ago' : 14.6, 'Sep' : 15.5, 'Oct' : 15.7, 'Nov' : 14.1, 'Dic' : 12.5},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.6, 'Feb' : 3.6, 'Mar' : 3.3, 'Abr' : 3.9, 'May' : 3.6, 'Jun' : 4.3, 'Jul' : 3.5, 'Ago' : 3.5, 'Sep' : 3.6, 'Oct' : 3.5, 'Nov' : 3.3, 'Dic' : 3.5},
	'Precipitación (mm)' : {
            'Ene' : 167.3, 'Feb' : 161.9, 'Mar' : 175.1, 'Abr' : 206.6, 'May' : 91.9, 'Jun' : 70.5, 'Jul' : 37.5, 'Ago' : 47.2, 'Sep' : 75.7, 'Oct' : 150.7, 'Nov' : 184.3, 'Dic' : 157.7},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.5, 'Feb' : 9.4, 'Mar' : 8.6, 'Abr' : 10.2, 'May' : 7.5, 'Jun' : 8.4, 'Jul' : 6.1, 'Ago' : 5.7, 'Sep' : 8.1, 'Oct' : 10.4, 'Nov' : 10.0, 'Dic' : 9.3},
},
{
	'Estación' : 'POSADAS AERO', 
	'Temperatura (°C)' : {
            'Ene' : 27.0, 'Feb' : 26.2, 'Mar' : 25.1, 'Abr' : 21.9, 'May' : 18.3, 'Jun' : 16.5, 'Jul' : 16.1, 'Ago' : 17.9, 'Sep' : 19.2, 'Oct' : 22.3, 'Nov' : 24.2, 'Dic' : 26.3},
	'Temperatura máxima (°C)' : {
            'Ene' : 33.0, 'Feb' : 32.1, 'Mar' : 31.2, 'Abr' : 27.6, 'May' : 23.9, 'Jun' : 21.9, 'Jul' : 21.9, 'Ago' : 24.2, 'Sep' : 25.1, 'Oct' : 28.3, 'Nov' : 30.3, 'Dic' : 32.4},
	'Temperatura mínima (°C)' : {
            'Ene' : 21.8, 'Feb' : 21.3, 'Mar' : 20.2, 'Abr' : 17.4, 'May' : 14.0, 'Jun' : 12.3, 'Jul' : 11.6, 'Ago' : 13.1, 'Sep' : 14.3, 'Oct' : 17.1, 'Nov' : 18.6, 'Dic' : 20.7},
	'Humedad relativa (%)' : {
            'Ene' : 68.5, 'Feb' : 72.1, 'Mar' : 73.0, 'Abr' : 76.4, 'May' : 77.4, 'Jun' : 78.8, 'Jul' : 74.7, 'Ago' : 70.3, 'Sep' : 69.8, 'Oct' : 69.8, 'Nov' : 66.9, 'Dic' : 65.8},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 9.1, 'Feb' : 9.1, 'Mar' : 8.6, 'Abr' : 8.7, 'May' : 9.0, 'Jun' : 8.9, 'Jul' : 10.1, 'Ago' : 10.9, 'Sep' : 11.0, 'Oct' : 11.0, 'Nov' : 10.4, 'Dic' : 9.6},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.6, 'Feb' : 3.6, 'Mar' : 3.3, 'Abr' : 3.7, 'May' : 3.6, 'Jun' : 4.1, 'Jul' : 3.6, 'Ago' : 3.6, 'Sep' : 3.8, 'Oct' : 3.7, 'Nov' : 3.4, 'Dic' : 3.4},
	'Precipitación (mm)' : {
            'Ene' : 167.2, 'Feb' : 154.9, 'Mar' : 144.1, 'Abr' : 193.8, 'May' : 138.2, 'Jun' : 139.8, 'Jul' : 103.3, 'Ago' : 93.9, 'Sep' : 145.1, 'Oct' : 226.0, 'Nov' : 181.0, 'Dic' : 179.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 10.3, 'Feb' : 9.6, 'Mar' : 9.0, 'Abr' : 10.2, 'May' : 8.3, 'Jun' : 9.4, 'Jul' : 9.0, 'Ago' : 8.3, 'Sep' : 10.9, 'Oct' : 11.3, 'Nov' : 9.5, 'Dic' : 9.4},
},
{
	'Estación' : 'TINOGASTA', 
	'Temperatura (°C)' : {
            'Ene' : 25.6, 'Feb' : 24.4, 'Mar' : 22.9, 'Abr' : 18.3, 'May' : 13.5, 'Jun' : 10.3, 'Jul' : 10.0, 'Ago' : 13.2, 'Sep' : 16.2, 'Oct' : 21.3, 'Nov' : 23.9, 'Dic' : 25.9},
	'Temperatura máxima (°C)' : {
            'Ene' : 33.5, 'Feb' : 32.4, 'Mar' : 30.9, 'Abr' : 26.9, 'May' : 22.6, 'Jun' : 19.9, 'Jul' : 19.8, 'Ago' : 23.1, 'Sep' : 25.7, 'Oct' : 30.2, 'Nov' : 32.5, 'Dic' : 33.9},
	'Temperatura mínima (°C)' : {
            'Ene' : 18.7, 'Feb' : 17.3, 'Mar' : 16.0, 'Abr' : 10.1, 'May' : 4.5, 'Jun' : 0.8, 'Jul' : 0.2, 'Ago' : 2.5, 'Sep' : 5.9, 'Oct' : 11.2, 'Nov' : 15.1, 'Dic' : 17.9},
	'Humedad relativa (%)' : {
            'Ene' : 56.9, 'Feb' : 58.3, 'Mar' : 60.8, 'Abr' : 61.6, 'May' : 63.2, 'Jun' : 60.0, 'Jul' : 55.4, 'Ago' : 47.7, 'Sep' : 47.3, 'Oct' : 46.5, 'Nov' : 48.6, 'Dic' : 51.6},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 5.9, 'Feb' : 5.2, 'Mar' : 6.6, 'Abr' : 4.2, 'May' : 4.3, 'Jun' : 4.4, 'Jul' : 4.6, 'Ago' : 5.9, 'Sep' : 5.4, 'Oct' : 6.4, 'Nov' : 6.5, 'Dic' : 6.2},
	'Nubosidad total (octavos)' : {
            'Ene' : 4.3, 'Feb' : 4.1, 'Mar' : 3.6, 'Abr' : 2.8, 'May' : 3.0, 'Jun' : 2.9, 'Jul' : 2.4, 'Ago' : 2.1, 'Sep' : 2.3, 'Oct' : 2.5, 'Nov' : 3.2, 'Dic' : 3.8},
	'Precipitación (mm)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
},
{
	'Estación' : 'LA RIOJA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 27.2, 'Feb' : 25.8, 'Mar' : 23.9, 'Abr' : 19.7, 'May' : 15.1, 'Jun' : 11.4, 'Jul' : 10.8, 'Ago' : 14.2, 'Sep' : 17.9, 'Oct' : 22.9, 'Nov' : 25.5, 'Dic' : 27.4},
	'Temperatura máxima (°C)' : {
            'Ene' : 34.7, 'Feb' : 33.0, 'Mar' : 30.7, 'Abr' : 26.7, 'May' : 22.6, 'Jun' : 19.4, 'Jul' : 19.5, 'Ago' : 23.0, 'Sep' : 26.2, 'Oct' : 30.9, 'Nov' : 33.5, 'Dic' : 35.1},
	'Temperatura mínima (°C)' : {
            'Ene' : 21.1, 'Feb' : 19.9, 'Mar' : 18.7, 'Abr' : 14.5, 'May' : 9.7, 'Jun' : 5.6, 'Jul' : 4.4, 'Ago' : 7.2, 'Sep' : 10.9, 'Oct' : 16.0, 'Nov' : 18.7, 'Dic' : 20.9},
	'Humedad relativa (%)' : {
            'Ene' : 61.8, 'Feb' : 64.6, 'Mar' : 68.6, 'Abr' : 69.7, 'May' : 69.7, 'Jun' : 69.4, 'Jul' : 62.9, 'Ago' : 52.9, 'Sep' : 48.9, 'Oct' : 48.8, 'Nov' : 51.9, 'Dic' : 55.9},
	'Velocidad del Viento (km/h)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.9, 'Feb' : 3.9, 'Mar' : 3.9, 'Abr' : 3.6, 'May' : 3.4, 'Jun' : 3.4, 'Jul' : 2.6, 'Ago' : 2.4, 'Sep' : 2.5, 'Oct' : 2.8, 'Nov' : 3.2, 'Dic' : 3.6},
	'Precipitación (mm)' : {
            'Ene' : 96.3, 'Feb' : 73.6, 'Mar' : 65.0, 'Abr' : 29.3, 'May' : 9.0, 'Jun' : 2.9, 'Jul' : 3.8, 'Ago' : 4.2, 'Sep' : 9.4, 'Oct' : 17.6, 'Nov' : 35.9, 'Dic' : 65.0},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.5, 'Feb' : 7.4, 'Mar' : 6.0, 'Abr' : 3.9, 'May' : 2.1, 'Jun' : 0.9, 'Jul' : 1.0, 'Ago' : 0.6, 'Sep' : 1.6, 'Oct' : 2.3, 'Nov' : 4.1, 'Dic' : 6.4},
},
{
	'Estación' : 'CATAMARCA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 27.3, 'Feb' : 26.0, 'Mar' : 24.4, 'Abr' : 20.4, 'May' : 16.0, 'Jun' : 12.0, 'Jul' : 11.6, 'Ago' : 15.4, 'Sep' : 19.1, 'Oct' : 23.6, 'Nov' : 25.6, 'Dic' : 27.3},
	'Temperatura máxima (°C)' : {
            'Ene' : 34.1, 'Feb' : 32.8, 'Mar' : 31.2, 'Abr' : 27.5, 'May' : 23.5, 'Jun' : 20.0, 'Jul' : 20.2, 'Ago' : 23.9, 'Sep' : 26.8, 'Oct' : 30.9, 'Nov' : 32.7, 'Dic' : 34.3},
	'Temperatura mínima (°C)' : {
            'Ene' : 21.5, 'Feb' : 20.4, 'Mar' : 19.1, 'Abr' : 14.7, 'May' : 9.8, 'Jun' : 5.3, 'Jul' : 4.4, 'Ago' : 7.7, 'Sep' : 11.8, 'Oct' : 16.8, 'Nov' : 19.3, 'Dic' : 21.2},
	'Humedad relativa (%)' : {
            'Ene' : 56.2, 'Feb' : 59.8, 'Mar' : 63.8, 'Abr' : 65.3, 'May' : 66.3, 'Jun' : 66.1, 'Jul' : 58.6, 'Ago' : 47.7, 'Sep' : 43.0, 'Oct' : 44.7, 'Nov' : 48.5, 'Dic' : 52.5},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 20.9, 'Feb' : 18.9, 'Mar' : 17.0, 'Abr' : 14.2, 'May' : 11.7, 'Jun' : 9.5, 'Jul' : 10.9, 'Ago' : 14.8, 'Sep' : 18.6, 'Oct' : 22.4, 'Nov' : 22.5, 'Dic' : 21.9},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.6, 'Feb' : 3.6, 'Mar' : 3.4, 'Abr' : 3.4, 'May' : 3.5, 'Jun' : 3.5, 'Jul' : 2.8, 'Ago' : 2.7, 'Sep' : 2.8, 'Oct' : 2.9, 'Nov' : 3.1, 'Dic' : 3.3},
	'Precipitación (mm)' : {
            'Ene' : 83.8, 'Feb' : 69.2, 'Mar' : 52.4, 'Abr' : 27.0, 'May' : 12.6, 'Jun' : 4.7, 'Jul' : 8.1, 'Ago' : 3.2, 'Sep' : 7.3, 'Oct' : 25.9, 'Nov' : 50.2, 'Dic' : 68.0},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.9, 'Feb' : 7.2, 'Mar' : 7.0, 'Abr' : 5.3, 'May' : 3.3, 'Jun' : 2.0, 'Jul' : 2.2, 'Ago' : 1.2, 'Sep' : 2.2, 'Oct' : 3.6, 'Nov' : 5.4, 'Dic' : 7.4},
},
{
	'Estación' : 'VILLA MARÍA DEL RÍO SECO', 
	'Temperatura (°C)' : {
            'Ene' : 24.0, 'Feb' : 22.4, 'Mar' : 21.0, 'Abr' : 17.3, 'May' : 14.0, 'Jun' : 11.2, 'Jul' : 10.5, 'Ago' : 12.9, 'Sep' : 15.3, 'Oct' : 19.2, 'Nov' : 21.4, 'Dic' : 23.4},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.4, 'Feb' : 29.8, 'Mar' : 28.1, 'Abr' : 24.3, 'May' : 21.3, 'Jun' : 18.7, 'Jul' : 18.7, 'Ago' : 21.6, 'Sep' : 23.6, 'Oct' : 27.1, 'Nov' : 29.1, 'Dic' : 30.9},
	'Temperatura mínima (°C)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Humedad relativa (%)' : {
            'Ene' : 74.7, 'Feb' : 79.7, 'Mar' : 81.8, 'Abr' : 82.1, 'May' : 79.0, 'Jun' : 76.7, 'Jul' : 71.8, 'Ago' : 66.3, 'Sep' : 64.7, 'Oct' : 67.5, 'Nov' : 70.4, 'Dic' : 72.5},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 6.2, 'Feb' : 5.7, 'Mar' : 5.2, 'Abr' : 5.3, 'May' : 5.2, 'Jun' : 5.3, 'Jul' : 5.7, 'Ago' : 6.8, 'Sep' : 7.6, 'Oct' : 8.8, 'Nov' : 8.6, 'Dic' : 7.1},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.9, 'Feb' : 4.1, 'Mar' : 4.1, 'Abr' : 4.4, 'May' : 4.4, 'Jun' : 4.2, 'Jul' : 3.3, 'Ago' : 3.2, 'Sep' : 3.3, 'Oct' : 3.6, 'Nov' : 3.8, 'Dic' : 4.0},
	'Precipitación (mm)' : {
            'Ene' : 130.6, 'Feb' : 119.7, 'Mar' : 134.5, 'Abr' : 70.4, 'May' : 21.3, 'Jun' : 8.4, 'Jul' : 12.5, 'Ago' : 6.7, 'Sep' : 27.1, 'Oct' : 62.6, 'Nov' : 89.0, 'Dic' : 130.2},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 9.9, 'Feb' : 9.1, 'Mar' : 9.4, 'Abr' : 7.6, 'May' : 4.4, 'Jun' : 3.3, 'Jul' : 2.7, 'Ago' : 1.6, 'Sep' : 3.6, 'Oct' : 6.6, 'Nov' : 8.7, 'Dic' : 9.6},
},
{
	'Estación' : 'CERES AERO', 
	'Temperatura (°C)' : {
            'Ene' : 25.3, 'Feb' : 24.1, 'Mar' : 22.6, 'Abr' : 18.8, 'May' : 15.2, 'Jun' : 12.3, 'Jul' : 11.5, 'Ago' : 13.7, 'Sep' : 16.0, 'Oct' : 19.8, 'Nov' : 22.2, 'Dic' : 24.3},
	'Temperatura máxima (°C)' : {
            'Ene' : 32.1, 'Feb' : 30.9, 'Mar' : 29.3, 'Abr' : 25.0, 'May' : 21.9, 'Jun' : 18.8, 'Jul' : 18.8, 'Ago' : 21.7, 'Sep' : 23.7, 'Oct' : 27.0, 'Nov' : 29.0, 'Dic' : 31.0},
	'Temperatura mínima (°C)' : {
            'Ene' : 19.2, 'Feb' : 18.5, 'Mar' : 17.3, 'Abr' : 14.0, 'May' : 10.3, 'Jun' : 7.5, 'Jul' : 6.2, 'Ago' : 7.6, 'Sep' : 9.5, 'Oct' : 13.4, 'Nov' : 15.8, 'Dic' : 17.9},
	'Humedad relativa (%)' : {
            'Ene' : 72.0, 'Feb' : 76.3, 'Mar' : 78.8, 'Abr' : 81.8, 'May' : 81.7, 'Jun' : 82.3, 'Jul' : 78.3, 'Ago' : 72.7, 'Sep' : 69.6, 'Oct' : 69.9, 'Nov' : 70.6, 'Dic' : 71.3},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 10.2, 'Feb' : 10.6, 'Mar' : 10.7, 'Abr' : 9.8, 'May' : 10.3, 'Jun' : 10.2, 'Jul' : 12.0, 'Ago' : 14.1, 'Sep' : 14.6, 'Oct' : 15.1, 'Nov' : 13.8, 'Dic' : 11.9},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.3, 'Feb' : 3.4, 'Mar' : 3.4, 'Abr' : 3.9, 'May' : 4.0, 'Jun' : 4.3, 'Jul' : 3.5, 'Ago' : 3.4, 'Sep' : 3.4, 'Oct' : 3.6, 'Nov' : 3.3, 'Dic' : 3.3},
	'Precipitación (mm)' : {
            'Ene' : 132.0, 'Feb' : 122.4, 'Mar' : 153.5, 'Abr' : 95.4, 'May' : 35.4, 'Jun' : 18.7, 'Jul' : 15.6, 'Ago' : 13.0, 'Sep' : 36.4, 'Oct' : 83.8, 'Nov' : 103.2, 'Dic' : 143.7},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 9.4, 'Feb' : 8.2, 'Mar' : 9.3, 'Abr' : 9.3, 'May' : 6.0, 'Jun' : 5.1, 'Jul' : 3.8, 'Ago' : 3.6, 'Sep' : 5.1, 'Oct' : 7.5, 'Nov' : 9.3, 'Dic' : 9.4},
},
{
	'Estación' : 'RECONQUISTA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 26.4, 'Feb' : 25.2, 'Mar' : 23.7, 'Abr' : 20.0, 'May' : 16.7, 'Jun' : 14.1, 'Jul' : 13.4, 'Ago' : 15.4, 'Sep' : 17.1, 'Oct' : 20.6, 'Nov' : 22.9, 'Dic' : 25.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 32.4, 'Feb' : 30.9, 'Mar' : 29.4, 'Abr' : 25.4, 'May' : 22.2, 'Jun' : 19.3, 'Jul' : 19.5, 'Ago' : 22.2, 'Sep' : 23.6, 'Oct' : 26.7, 'Nov' : 28.7, 'Dic' : 31.0},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.8, 'Feb' : 20.2, 'Mar' : 19.0, 'Abr' : 15.7, 'May' : 12.2, 'Jun' : 9.8, 'Jul' : 8.7, 'Ago' : 10.0, 'Sep' : 11.6, 'Oct' : 15.1, 'Nov' : 17.3, 'Dic' : 19.5},
	'Humedad relativa (%)' : {
            'Ene' : 70.3, 'Feb' : 75.6, 'Mar' : 78.0, 'Abr' : 81.5, 'May' : 81.5, 'Jun' : 83.1, 'Jul' : 78.8, 'Ago' : 73.5, 'Sep' : 71.5, 'Oct' : 71.8, 'Nov' : 71.0, 'Dic' : 70.4},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 11.5, 'Feb' : 12.0, 'Mar' : 11.7, 'Abr' : 10.6, 'May' : 10.8, 'Jun' : 10.7, 'Jul' : 12.6, 'Ago' : 14.4, 'Sep' : 15.0, 'Oct' : 15.5, 'Nov' : 14.0, 'Dic' : 12.3},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.2, 'Feb' : 3.4, 'Mar' : 3.2, 'Abr' : 3.8, 'May' : 3.6, 'Jun' : 4.3, 'Jul' : 3.5, 'Ago' : 3.4, 'Sep' : 3.5, 'Oct' : 3.5, 'Nov' : 3.2, 'Dic' : 3.1},
	'Precipitación (mm)' : {
            'Ene' : 141.4, 'Feb' : 156.6, 'Mar' : 168.3, 'Abr' : 155.6, 'May' : 58.9, 'Jun' : 49.3, 'Jul' : 31.2, 'Ago' : 26.3, 'Sep' : 53.1, 'Oct' : 114.0, 'Nov' : 159.8, 'Dic' : 136.4},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 7.8, 'Feb' : 8.1, 'Mar' : 8.4, 'Abr' : 9.2, 'May' : 5.8, 'Jun' : 5.7, 'Jul' : 4.3, 'Ago' : 3.8, 'Sep' : 6.1, 'Oct' : 8.7, 'Nov' : 9.5, 'Dic' : 8.7},
},
{
	'Estación' : 'PASO DE LOS LIBRES AERO', 
	'Temperatura (°C)' : {
            'Ene' : 26.2, 'Feb' : 25.0, 'Mar' : 23.6, 'Abr' : 19.9, 'May' : 16.3, 'Jun' : 13.9, 'Jul' : 13.4, 'Ago' : 15.3, 'Sep' : 16.7, 'Oct' : 20.1, 'Nov' : 22.5, 'Dic' : 25.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 32.6, 'Feb' : 31.0, 'Mar' : 29.6, 'Abr' : 25.6, 'May' : 21.9, 'Jun' : 19.2, 'Jul' : 19.1, 'Ago' : 21.6, 'Sep' : 22.6, 'Oct' : 25.9, 'Nov' : 28.5, 'Dic' : 31.2},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.5, 'Feb' : 20.0, 'Mar' : 18.5, 'Abr' : 15.2, 'May' : 11.7, 'Jun' : 9.7, 'Jul' : 9.0, 'Ago' : 10.3, 'Sep' : 11.7, 'Oct' : 14.7, 'Nov' : 16.8, 'Dic' : 19.0},
	'Humedad relativa (%)' : {
            'Ene' : 67.0, 'Feb' : 72.5, 'Mar' : 74.4, 'Abr' : 78.1, 'May' : 80.4, 'Jun' : 82.3, 'Jul' : 79.6, 'Ago' : 75.0, 'Sep' : 73.8, 'Oct' : 72.2, 'Nov' : 68.7, 'Dic' : 65.7},
	'Velocidad del Viento (km/h)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.8, 'Feb' : 3.9, 'Mar' : 3.5, 'Abr' : 3.9, 'May' : 3.9, 'Jun' : 4.3, 'Jul' : 3.9, 'Ago' : 3.8, 'Sep' : 4.0, 'Oct' : 3.9, 'Nov' : 3.5, 'Dic' : 3.6},
	'Precipitación (mm)' : {
            'Ene' : 128.0, 'Feb' : 154.3, 'Mar' : 166.8, 'Abr' : 205.0, 'May' : 129.8, 'Jun' : 101.4, 'Jul' : 73.7, 'Ago' : 56.8, 'Sep' : 108.7, 'Oct' : 152.6, 'Nov' : 149.9, 'Dic' : 120.6},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 7.1, 'Feb' : 8.5, 'Mar' : 7.7, 'Abr' : 8.6, 'May' : 7.4, 'Jun' : 8.0, 'Jul' : 6.7, 'Ago' : 5.9, 'Sep' : 7.7, 'Oct' : 9.1, 'Nov' : 7.7, 'Dic' : 6.9},
},
{
	'Estación' : 'SAN JUAN AERO', 
	'Temperatura (°C)' : {
            'Ene' : 27.1, 'Feb' : 25.5, 'Mar' : 22.8, 'Abr' : 17.2, 'May' : 12.2, 'Jun' : 8.3, 'Jul' : 7.7, 'Ago' : 10.6, 'Sep' : 14.4, 'Oct' : 19.8, 'Nov' : 23.4, 'Dic' : 26.3},
	'Temperatura máxima (°C)' : {
            'Ene' : 34.9, 'Feb' : 33.4, 'Mar' : 30.3, 'Abr' : 25.2, 'May' : 20.5, 'Jun' : 16.9, 'Jul' : 16.5, 'Ago' : 19.9, 'Sep' : 23.2, 'Oct' : 28.1, 'Nov' : 31.6, 'Dic' : 34.2},
	'Temperatura mínima (°C)' : {
            'Ene' : 19.5, 'Feb' : 18.2, 'Mar' : 16.2, 'Abr' : 10.7, 'May' : 5.8, 'Jun' : 1.5, 'Jul' : 0.7, 'Ago' : 2.9, 'Sep' : 6.5, 'Oct' : 11.4, 'Nov' : 14.8, 'Dic' : 18.0},
	'Humedad relativa (%)' : {
            'Ene' : 44.3, 'Feb' : 47.1, 'Mar' : 54.5, 'Abr' : 57.9, 'May' : 61.4, 'Jun' : 62.5, 'Jul' : 57.8, 'Ago' : 48.2, 'Sep' : 43.8, 'Oct' : 39.6, 'Nov' : 38.9, 'Dic' : 40.1},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 15.5, 'Feb' : 13.9, 'Mar' : 12.9, 'Abr' : 10.6, 'May' : 9.3, 'Jun' : 9.3, 'Jul' : 10.3, 'Ago' : 11.6, 'Sep' : 12.6, 'Oct' : 14.8, 'Nov' : 16.0, 'Dic' : 16.1},
	'Nubosidad total (octavos)' : {
            'Ene' : 2.8, 'Feb' : 2.7, 'Mar' : 2.8, 'Abr' : 2.5, 'May' : 2.9, 'Jun' : 2.9, 'Jul' : 2.5, 'Ago' : 2.3, 'Sep' : 2.5, 'Oct' : 2.3, 'Nov' : 2.3, 'Dic' : 2.5},
	'Precipitación (mm)' : {
            'Ene' : 15.7, 'Feb' : 18.9, 'Mar' : 11.2, 'Abr' : 4.4, 'May' : 4.4, 'Jun' : 1.6, 'Jul' : 3.5, 'Ago' : 3.2, 'Sep' : 5.6, 'Oct' : 3.6, 'Nov' : 7.0, 'Dic' : 11.6},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 3.5, 'Feb' : 2.9, 'Mar' : 2.5, 'Abr' : 1.3, 'May' : 1.2, 'Jun' : 0.5, 'Jul' : 1.1, 'Ago' : 0.9, 'Sep' : 1.8, 'Oct' : 1.1, 'Nov' : 1.6, 'Dic' : 2.3},
},
{
	'Estación' : 'CHAMICAL AERO', 
	'Temperatura (°C)' : {
            'Ene' : 26.5, 'Feb' : 25.1, 'Mar' : 23.2, 'Abr' : 19.1, 'May' : 15.2, 'Jun' : 11.9, 'Jul' : 11.3, 'Ago' : 14.4, 'Sep' : 17.7, 'Oct' : 22.2, 'Nov' : 24.6, 'Dic' : 26.4},
	'Temperatura máxima (°C)' : {
            'Ene' : 33.2, 'Feb' : 31.6, 'Mar' : 29.2, 'Abr' : 25.2, 'May' : 21.4, 'Jun' : 18.3, 'Jul' : 18.6, 'Ago' : 22.0, 'Sep' : 25.0, 'Oct' : 29.3, 'Nov' : 31.7, 'Dic' : 33.5},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.3, 'Feb' : 19.3, 'Mar' : 18.1, 'Abr' : 14.1, 'May' : 10.0, 'Jun' : 6.6, 'Jul' : 5.3, 'Ago' : 7.7, 'Sep' : 10.6, 'Oct' : 15.1, 'Nov' : 17.7, 'Dic' : 19.7},
	'Humedad relativa (%)' : {
            'Ene' : 60.0, 'Feb' : 63.3, 'Mar' : 67.4, 'Abr' : 68.6, 'May' : 68.7, 'Jun' : 67.4, 'Jul' : 60.0, 'Ago' : 50.3, 'Sep' : 46.5, 'Oct' : 47.3, 'Nov' : 50.5, 'Dic' : 54.8},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 11.7, 'Feb' : 9.8, 'Mar' : 8.2, 'Abr' : 7.1, 'May' : 6.6, 'Jun' : 6.4, 'Jul' : 7.5, 'Ago' : 9.5, 'Sep' : 11.3, 'Oct' : 13.8, 'Nov' : 14.0, 'Dic' : 13.2},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.6, 'Feb' : 3.7, 'Mar' : 3.9, 'Abr' : 3.9, 'May' : 3.8, 'Jun' : 3.9, 'Jul' : 2.9, 'Ago' : 2.6, 'Sep' : 2.8, 'Oct' : 2.9, 'Nov' : 3.2, 'Dic' : 3.4},
	'Precipitación (mm)' : {
            'Ene' : 105.0, 'Feb' : 95.1, 'Mar' : 68.2, 'Abr' : 26.6, 'May' : 9.9, 'Jun' : 2.1, 'Jul' : 4.9, 'Ago' : 1.7, 'Sep' : 9.4, 'Oct' : 30.4, 'Nov' : 42.6, 'Dic' : 83.5},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.6, 'Feb' : 6.6, 'Mar' : 6.8, 'Abr' : 4.4, 'May' : 2.7, 'Jun' : 1.5, 'Jul' : 1.4, 'Ago' : 1.0, 'Sep' : 2.2, 'Oct' : 2.9, 'Nov' : 5.4, 'Dic' : 7.2},
},
{
	'Estación' : 'VILLA DOLORES AERO', 
	'Temperatura (°C)' : {
            'Ene' : 25.1, 'Feb' : 23.7, 'Mar' : 21.8, 'Abr' : 17.7, 'May' : 13.8, 'Jun' : 10.7, 'Jul' : 10.1, 'Ago' : 12.9, 'Sep' : 15.8, 'Oct' : 20.3, 'Nov' : 22.8, 'Dic' : 24.6},
	'Temperatura máxima (°C)' : {
            'Ene' : 32.3, 'Feb' : 31.0, 'Mar' : 28.8, 'Abr' : 24.9, 'May' : 21.1, 'Jun' : 18.3, 'Jul' : 18.2, 'Ago' : 21.3, 'Sep' : 24.0, 'Oct' : 28.1, 'Nov' : 30.4, 'Dic' : 31.9},
	'Temperatura mínima (°C)' : {
            'Ene' : 18.1, 'Feb' : 17.1, 'Mar' : 16.0, 'Abr' : 12.2, 'May' : 8.7, 'Jun' : 5.6, 'Jul' : 4.5, 'Ago' : 6.6, 'Sep' : 8.8, 'Oct' : 12.8, 'Nov' : 15.2, 'Dic' : 17.3},
	'Humedad relativa (%)' : {
            'Ene' : 61.1, 'Feb' : 64.9, 'Mar' : 70.3, 'Abr' : 71.4, 'May' : 72.2, 'Jun' : 70.5, 'Jul' : 64.3, 'Ago' : 54.4, 'Sep' : 50.5, 'Oct' : 50.7, 'Nov' : 53.0, 'Dic' : 57.9},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 7.1, 'Feb' : 5.0, 'Mar' : 4.6, 'Abr' : 5.0, 'May' : 4.6, 'Jun' : 4.3, 'Jul' : 5.6, 'Ago' : 6.5, 'Sep' : 7.1, 'Oct' : 8.7, 'Nov' : 8.6, 'Dic' : 7.3},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.4, 'Feb' : 3.5, 'Mar' : 3.6, 'Abr' : 3.5, 'May' : 3.8, 'Jun' : 3.6, 'Jul' : 3.1, 'Ago' : 3.0, 'Sep' : 3.1, 'Oct' : 3.2, 'Nov' : 3.3, 'Dic' : 3.5},
	'Precipitación (mm)' : {
            'Ene' : 121.1, 'Feb' : 102.2, 'Mar' : 94.4, 'Abr' : 42.4, 'May' : 17.6, 'Jun' : 4.7, 'Jul' : 13.2, 'Ago' : 6.1, 'Sep' : 22.9, 'Oct' : 35.1, 'Nov' : 75.1, 'Dic' : 113.3},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 10.5, 'Feb' : 9.1, 'Mar' : 8.6, 'Abr' : 5.5, 'May' : 3.7, 'Jun' : 1.8, 'Jul' : 2.5, 'Ago' : 1.6, 'Sep' : 3.7, 'Oct' : 4.8, 'Nov' : 8.0, 'Dic' : 10.5},
},
{
	'Estación' : 'CÓRDOBA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 23.4, 'Feb' : 22.2, 'Mar' : 20.7, 'Abr' : 17.2, 'May' : 13.7, 'Jun' : 10.7, 'Jul' : 10.0, 'Ago' : 12.5, 'Sep' : 14.9, 'Oct' : 18.6, 'Nov' : 20.9, 'Dic' : 22.9},
	'Temperatura máxima (°C)' : {
            'Ene' : 29.4, 'Feb' : 28.3, 'Mar' : 26.9, 'Abr' : 23.6, 'May' : 20.5, 'Jun' : 18.0, 'Jul' : 17.6, 'Ago' : 20.3, 'Sep' : 22.3, 'Oct' : 25.6, 'Nov' : 27.5, 'Dic' : 29.0},
	'Temperatura mínima (°C)' : {
            'Ene' : 17.5, 'Feb' : 16.6, 'Mar' : 15.5, 'Abr' : 11.7, 'May' : 8.3, 'Jun' : 5.1, 'Jul' : 4.0, 'Ago' : 5.9, 'Sep' : 8.2, 'Oct' : 11.9, 'Nov' : 14.4, 'Dic' : 16.8},
	'Humedad relativa (%)' : {
            'Ene' : 69.9, 'Feb' : 73.2, 'Mar' : 76.0, 'Abr' : 74.4, 'May' : 72.7, 'Jun' : 70.3, 'Jul' : 65.7, 'Ago' : 58.3, 'Sep' : 56.7, 'Oct' : 60.0, 'Nov' : 62.4, 'Dic' : 65.9},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 12.6, 'Feb' : 11.3, 'Mar' : 11.4, 'Abr' : 11.5, 'May' : 11.2, 'Jun' : 10.9, 'Jul' : 12.0, 'Ago' : 13.5, 'Sep' : 14.8, 'Oct' : 15.8, 'Nov' : 15.8, 'Dic' : 13.7},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.8, 'Feb' : 3.9, 'Mar' : 3.9, 'Abr' : 4.0, 'May' : 4.2, 'Jun' : 4.0, 'Jul' : 3.5, 'Ago' : 3.3, 'Sep' : 3.5, 'Oct' : 3.7, 'Nov' : 3.7, 'Dic' : 4.0},
	'Precipitación (mm)' : {
            'Ene' : 141.0, 'Feb' : 115.9, 'Mar' : 126.9, 'Abr' : 66.3, 'May' : 21.3, 'Jun' : 4.8, 'Jul' : 13.5, 'Ago' : 9.7, 'Sep' : 35.2, 'Oct' : 71.9, 'Nov' : 118.3, 'Dic' : 156.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 11.0, 'Feb' : 9.5, 'Mar' : 9.6, 'Abr' : 6.4, 'May' : 4.3, 'Jun' : 2.0, 'Jul' : 2.7, 'Ago' : 1.7, 'Sep' : 3.7, 'Oct' : 6.7, 'Nov' : 8.9, 'Dic' : 11.1},
},
{
	'Estación' : 'CÓRDOBA OBSERVATORIO', 
	'Temperatura (°C)' : {
            'Ene' : 24.3, 'Feb' : 23.1, 'Mar' : 21.7, 'Abr' : 18.0, 'May' : 14.5, 'Jun' : 11.4, 'Jul' : 10.8, 'Ago' : 13.3, 'Sep' : 15.7, 'Oct' : 19.5, 'Nov' : 21.8, 'Dic' : 23.7},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.9, 'Feb' : 29.6, 'Mar' : 28.1, 'Abr' : 24.8, 'May' : 21.3, 'Jun' : 18.7, 'Jul' : 18.3, 'Ago' : 21.1, 'Sep' : 23.2, 'Oct' : 26.6, 'Nov' : 28.7, 'Dic' : 30.3},
	'Temperatura mínima (°C)' : {
            'Ene' : 18.5, 'Feb' : 17.5, 'Mar' : 16.4, 'Abr' : 12.8, 'May' : 9.4, 'Jun' : 6.3, 'Jul' : 5.5, 'Ago' : 7.3, 'Sep' : 9.5, 'Oct' : 13.3, 'Nov' : 15.6, 'Dic' : 17.9},
	'Humedad relativa (%)' : {
            'Ene' : 66.3, 'Feb' : 69.5, 'Mar' : 72.6, 'Abr' : 72.3, 'May' : 71.4, 'Jun' : 70.1, 'Jul' : 65.5, 'Ago' : 58.0, 'Sep' : 55.9, 'Oct' : 58.0, 'Nov' : 60.3, 'Dic' : 63.6},
	'Velocidad del Viento (km/h)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.7, 'Feb' : 3.7, 'Mar' : 3.8, 'Abr' : 3.9, 'May' : 4.1, 'Jun' : 4.0, 'Jul' : 3.4, 'Ago' : 3.4, 'Sep' : 3.5, 'Oct' : 3.6, 'Nov' : 3.6, 'Dic' : 3.8},
	'Precipitación (mm)' : {
            'Ene' : 126.3, 'Feb' : 97.0, 'Mar' : 112.1, 'Abr' : 61.3, 'May' : 18.8, 'Jun' : 4.5, 'Jul' : 13.3, 'Ago' : 8.9, 'Sep' : 35.2, 'Oct' : 69.8, 'Nov' : 112.2, 'Dic' : 154.6},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 12.0, 'Feb' : 10.3, 'Mar' : 10.3, 'Abr' : 7.1, 'May' : 5.0, 'Jun' : 2.8, 'Jul' : 3.2, 'Ago' : 2.2, 'Sep' : 4.9, 'Oct' : 7.6, 'Nov' : 10.5, 'Dic' : 12.7},
},
{
	'Estación' : 'PILAR OBS.', 
	'Temperatura (°C)' : {
            'Ene' : 23.4, 'Feb' : 22.1, 'Mar' : 20.6, 'Abr' : 17.0, 'May' : 13.6, 'Jun' : 10.5, 'Jul' : 9.7, 'Ago' : 11.9, 'Sep' : 14.3, 'Oct' : 18.3, 'Nov' : 20.8, 'Dic' : 22.9},
	'Temperatura máxima (°C)' : {
            'Ene' : 29.9, 'Feb' : 28.6, 'Mar' : 27.0, 'Abr' : 23.7, 'May' : 20.2, 'Jun' : 17.4, 'Jul' : 17.0, 'Ago' : 19.8, 'Sep' : 22.0, 'Oct' : 25.3, 'Nov' : 27.7, 'Dic' : 29.4},
	'Temperatura mínima (°C)' : {
            'Ene' : 17.9, 'Feb' : 16.9, 'Mar' : 15.7, 'Abr' : 12.1, 'May' : 8.6, 'Jun' : 5.5, 'Jul' : 4.4, 'Ago' : 5.8, 'Sep' : 8.2, 'Oct' : 12.2, 'Nov' : 14.8, 'Dic' : 17.1},
	'Humedad relativa (%)' : {
            'Ene' : 70.2, 'Feb' : 74.2, 'Mar' : 77.2, 'Abr' : 75.5, 'May' : 74.3, 'Jun' : 72.6, 'Jul' : 68.0, 'Ago' : 60.9, 'Sep' : 58.9, 'Oct' : 61.6, 'Nov' : 62.9, 'Dic' : 66.1},
	'Velocidad del Viento (km/h)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.5, 'Feb' : 3.6, 'Mar' : 3.7, 'Abr' : 3.8, 'May' : 4.1, 'Jun' : 4.0, 'Jul' : 3.5, 'Ago' : 3.3, 'Sep' : 3.4, 'Oct' : 3.6, 'Nov' : 3.6, 'Dic' : 3.7},
	'Precipitación (mm)' : {
            'Ene' : 132.2, 'Feb' : 106.1, 'Mar' : 109.6, 'Abr' : 63.4, 'May' : 23.9, 'Jun' : 4.9, 'Jul' : 13.8, 'Ago' : 9.6, 'Sep' : 33.1, 'Oct' : 66.6, 'Nov' : 103.2, 'Dic' : 130.1},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 10.7, 'Feb' : 9.1, 'Mar' : 9.5, 'Abr' : 7.0, 'May' : 4.8, 'Jun' : 2.9, 'Jul' : 2.9, 'Ago' : 2.3, 'Sep' : 4.5, 'Oct' : 7.4, 'Nov' : 9.9, 'Dic' : 11.7},
},
{
	'Estación' : 'SAUCE VIEJO AERO', 
	'Temperatura (°C)' : {
            'Ene' : 25.8, 'Feb' : 24.4, 'Mar' : 22.8, 'Abr' : 18.7, 'May' : 15.4, 'Jun' : 12.2, 'Jul' : 11.5, 'Ago' : 13.7, 'Sep' : 15.9, 'Oct' : 19.5, 'Nov' : 22.1, 'Dic' : 24.4},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.8, 'Feb' : 30.1, 'Mar' : 28.5, 'Abr' : 24.3, 'May' : 21.0, 'Jun' : 17.6, 'Jul' : 17.3, 'Ago' : 19.9, 'Sep' : 21.9, 'Oct' : 25.4, 'Nov' : 27.9, 'Dic' : 30.2},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.1, 'Feb' : 19.2, 'Mar' : 18.0, 'Abr' : 14.1, 'May' : 10.9, 'Jun' : 7.9, 'Jul' : 6.9, 'Ago' : 8.5, 'Sep' : 10.5, 'Oct' : 14.1, 'Nov' : 16.7, 'Dic' : 18.9},
	'Humedad relativa (%)' : {
            'Ene' : 70.9, 'Feb' : 75.4, 'Mar' : 78.3, 'Abr' : 81.5, 'May' : 82.5, 'Jun' : 83.6, 'Jul' : 80.4, 'Ago' : 75.7, 'Sep' : 73.0, 'Oct' : 72.7, 'Nov' : 71.1, 'Dic' : 70.5},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 9.2, 'Feb' : 8.8, 'Mar' : 9.6, 'Abr' : 8.9, 'May' : 9.8, 'Jun' : 10.1, 'Jul' : 12.1, 'Ago' : 13.8, 'Sep' : 13.9, 'Oct' : 14.3, 'Nov' : 13.4, 'Dic' : 10.9},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.0, 'Feb' : 3.2, 'Mar' : 3.1, 'Abr' : 3.5, 'May' : 3.6, 'Jun' : 4.0, 'Jul' : 3.4, 'Ago' : 3.2, 'Sep' : 3.3, 'Oct' : 3.3, 'Nov' : 3.1, 'Dic' : 3.1},
	'Precipitación (mm)' : {
            'Ene' : 95.4, 'Feb' : 112.0, 'Mar' : 146.4, 'Abr' : 116.2, 'May' : 49.4, 'Jun' : 31.5, 'Jul' : 23.9, 'Ago' : 28.4, 'Sep' : 53.2, 'Oct' : 110.5, 'Nov' : 128.9, 'Dic' : 124.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 7.0, 'Feb' : 7.0, 'Mar' : 7.9, 'Abr' : 7.8, 'May' : 4.7, 'Jun' : 3.5, 'Jul' : 3.0, 'Ago' : 3.3, 'Sep' : 4.9, 'Oct' : 7.3, 'Nov' : 7.5, 'Dic' : 8.2},
},
{
	'Estación' : 'PARANÁ AERO', 
	'Temperatura (°C)' : {
            'Ene' : 25.1, 'Feb' : 23.6, 'Mar' : 22.0, 'Abr' : 18.0, 'May' : 14.8, 'Jun' : 12.0, 'Jul' : 11.3, 'Ago' : 13.2, 'Sep' : 15.1, 'Oct' : 18.5, 'Nov' : 21.3, 'Dic' : 23.6},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.2, 'Feb' : 29.6, 'Mar' : 27.9, 'Abr' : 23.5, 'May' : 20.2, 'Jun' : 16.9, 'Jul' : 16.6, 'Ago' : 19.3, 'Sep' : 21.1, 'Oct' : 24.5, 'Nov' : 27.2, 'Dic' : 29.6},
	'Temperatura mínima (°C)' : {
            'Ene' : 19.3, 'Feb' : 18.5, 'Mar' : 17.1, 'Abr' : 13.6, 'May' : 10.6, 'Jun' : 8.0, 'Jul' : 7.1, 'Ago' : 8.4, 'Sep' : 9.9, 'Oct' : 13.1, 'Nov' : 15.6, 'Dic' : 17.8},
	'Humedad relativa (%)' : {
            'Ene' : 65.6, 'Feb' : 71.5, 'Mar' : 74.5, 'Abr' : 78.3, 'May' : 78.9, 'Jun' : 80.1, 'Jul' : 76.6, 'Ago' : 71.3, 'Sep' : 68.8, 'Oct' : 69.3, 'Nov' : 66.9, 'Dic' : 65.2},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 10.6, 'Feb' : 10.3, 'Mar' : 9.6, 'Abr' : 9.5, 'May' : 9.4, 'Jun' : 10.0, 'Jul' : 11.3, 'Ago' : 12.7, 'Sep' : 13.4, 'Oct' : 13.9, 'Nov' : 13.2, 'Dic' : 12.0},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.0, 'Feb' : 3.2, 'Mar' : 3.1, 'Abr' : 3.5, 'May' : 3.7, 'Jun' : 4.1, 'Jul' : 3.5, 'Ago' : 3.3, 'Sep' : 3.4, 'Oct' : 3.4, 'Nov' : 3.1, 'Dic' : 3.1},
	'Precipitación (mm)' : {
            'Ene' : 115.2, 'Feb' : 134.8, 'Mar' : 155.0, 'Abr' : 132.7, 'May' : 58.3, 'Jun' : 38.2, 'Jul' : 32.4, 'Ago' : 32.4, 'Sep' : 61.2, 'Oct' : 127.6, 'Nov' : 118.7, 'Dic' : 141.2},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 7.6, 'Feb' : 8.0, 'Mar' : 8.0, 'Abr' : 8.4, 'May' : 5.4, 'Jun' : 4.9, 'Jul' : 4.3, 'Ago' : 4.3, 'Sep' : 5.6, 'Oct' : 9.0, 'Nov' : 8.2, 'Dic' : 9.2},
},
{
	'Estación' : 'MONTE CASEROS AERO', 
	'Temperatura (°C)' : {
            'Ene' : 26.3, 'Feb' : 25.0, 'Mar' : 23.5, 'Abr' : 19.6, 'May' : 16.1, 'Jun' : 13.7, 'Jul' : 13.1, 'Ago' : 15.0, 'Sep' : 16.6, 'Oct' : 20.0, 'Nov' : 22.5, 'Dic' : 25.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 32.6, 'Feb' : 31.0, 'Mar' : 29.6, 'Abr' : 25.3, 'May' : 21.7, 'Jun' : 18.9, 'Jul' : 18.8, 'Ago' : 21.3, 'Sep' : 22.4, 'Oct' : 25.8, 'Nov' : 28.4, 'Dic' : 31.2},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.6, 'Feb' : 19.9, 'Mar' : 18.5, 'Abr' : 15.2, 'May' : 11.7, 'Jun' : 9.5, 'Jul' : 8.8, 'Ago' : 10.0, 'Sep' : 11.5, 'Oct' : 14.6, 'Nov' : 16.8, 'Dic' : 19.0},
	'Humedad relativa (%)' : {
            'Ene' : 66.9, 'Feb' : 72.9, 'Mar' : 74.7, 'Abr' : 79.0, 'May' : 80.4, 'Jun' : 81.9, 'Jul' : 78.9, 'Ago' : 74.5, 'Sep' : 73.1, 'Oct' : 71.9, 'Nov' : 69.1, 'Dic' : 65.8},
	'Velocidad del Viento (km/h)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.3, 'Feb' : 3.5, 'Mar' : 3.2, 'Abr' : 3.6, 'May' : 3.6, 'Jun' : 4.2, 'Jul' : 3.7, 'Ago' : 3.7, 'Sep' : 3.8, 'Oct' : 3.6, 'Nov' : 3.3, 'Dic' : 3.3},
	'Precipitación (mm)' : {
            'Ene' : 154.1, 'Feb' : 144.7, 'Mar' : 154.3, 'Abr' : 189.7, 'May' : 110.9, 'Jun' : 88.4, 'Jul' : 64.1, 'Ago' : 57.5, 'Sep' : 107.3, 'Oct' : 146.5, 'Nov' : 154.0, 'Dic' : 134.1},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.3, 'Feb' : 8.8, 'Mar' : 8.5, 'Abr' : 9.5, 'May' : 7.6, 'Jun' : 7.8, 'Jul' : 6.4, 'Ago' : 5.8, 'Sep' : 7.9, 'Oct' : 9.4, 'Nov' : 8.3, 'Dic' : 8.1},
},
{
	'Estación' : 'CONCORDIA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 25.8, 'Feb' : 24.4, 'Mar' : 22.8, 'Abr' : 18.8, 'May' : 15.3, 'Jun' : 12.7, 'Jul' : 12.2, 'Ago' : 14.1, 'Sep' : 15.7, 'Oct' : 19.1, 'Nov' : 21.7, 'Dic' : 24.2},
	'Temperatura máxima (°C)' : {
            'Ene' : 32.2, 'Feb' : 30.4, 'Mar' : 28.8, 'Abr' : 24.5, 'May' : 20.8, 'Jun' : 17.9, 'Jul' : 17.8, 'Ago' : 20.2, 'Sep' : 21.8, 'Oct' : 25.1, 'Nov' : 27.7, 'Dic' : 30.6},
	'Temperatura mínima (°C)' : {
            'Ene' : 19.4, 'Feb' : 18.8, 'Mar' : 17.3, 'Abr' : 13.8, 'May' : 10.5, 'Jun' : 8.2, 'Jul' : 7.4, 'Ago' : 8.6, 'Sep' : 10.1, 'Oct' : 13.2, 'Nov' : 15.4, 'Dic' : 17.7},
	'Humedad relativa (%)' : {
            'Ene' : 63.5, 'Feb' : 70.1, 'Mar' : 72.4, 'Abr' : 77.5, 'May' : 79.8, 'Jun' : 81.0, 'Jul' : 78.0, 'Ago' : 73.9, 'Sep' : 71.4, 'Oct' : 70.4, 'Nov' : 67.1, 'Dic' : 63.7},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 9.3, 'Feb' : 8.5, 'Mar' : 7.5, 'Abr' : 6.8, 'May' : 7.0, 'Jun' : 7.2, 'Jul' : 8.6, 'Ago' : 10.4, 'Sep' : 11.8, 'Oct' : 12.3, 'Nov' : 11.3, 'Dic' : 10.9},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.1, 'Feb' : 3.5, 'Mar' : 3.1, 'Abr' : 3.5, 'May' : 3.7, 'Jun' : 4.2, 'Jul' : 3.8, 'Ago' : 3.6, 'Sep' : 3.7, 'Oct' : 3.6, 'Nov' : 3.2, 'Dic' : 3.1},
	'Precipitación (mm)' : {
            'Ene' : 133.9, 'Feb' : 145.7, 'Mar' : 156.5, 'Abr' : 163.4, 'May' : 99.7, 'Jun' : 82.4, 'Jul' : 52.2, 'Ago' : 58.7, 'Sep' : 85.6, 'Oct' : 136.9, 'Nov' : 140.8, 'Dic' : 121.0},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.3, 'Feb' : 8.4, 'Mar' : 8.2, 'Abr' : 9.0, 'May' : 7.8, 'Jun' : 7.8, 'Jul' : 6.9, 'Ago' : 6.4, 'Sep' : 7.1, 'Oct' : 8.8, 'Nov' : 7.8, 'Dic' : 7.8},
},
{
	'Estación' : 'SAN MARTÍN (MZA)', 
	'Temperatura (°C)' : {
            'Ene' : 24.6, 'Feb' : 23.2, 'Mar' : 20.5, 'Abr' : 15.6, 'May' : 11.3, 'Jun' : 8.0, 'Jul' : 7.5, 'Ago' : 10.2, 'Sep' : 13.3, 'Oct' : 18.0, 'Nov' : 21.3, 'Dic' : 23.9},
	'Temperatura máxima (°C)' : {
            'Ene' : 32.4, 'Feb' : 31.1, 'Mar' : 28.1, 'Abr' : 23.5, 'May' : 19.1, 'Jun' : 15.7, 'Jul' : 15.4, 'Ago' : 18.6, 'Sep' : 21.5, 'Oct' : 26.0, 'Nov' : 29.2, 'Dic' : 31.7},
	'Temperatura mínima (°C)' : {
            'Ene' : 17.8, 'Feb' : 16.5, 'Mar' : 14.8, 'Abr' : 10.1, 'May' : 6.1, 'Jun' : 2.7, 'Jul' : 1.9, 'Ago' : 4.0, 'Sep' : 6.8, 'Oct' : 11.0, 'Nov' : 14.0, 'Dic' : 16.8},
	'Humedad relativa (%)' : {
            'Ene' : 55.5, 'Feb' : 59.2, 'Mar' : 66.4, 'Abr' : 69.8, 'May' : 70.6, 'Jun' : 69.9, 'Jul' : 65.0, 'Ago' : 56.7, 'Sep' : 54.7, 'Oct' : 51.3, 'Nov' : 51.1, 'Dic' : 51.5},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 7.1, 'Feb' : 6.2, 'Mar' : 6.0, 'Abr' : 5.2, 'May' : 4.7, 'Jun' : 4.5, 'Jul' : 5.1, 'Ago' : 5.9, 'Sep' : 6.9, 'Oct' : 7.7, 'Nov' : 8.4, 'Dic' : 7.5},
	'Nubosidad total (octavos)' : {
            'Ene' : 2.9, 'Feb' : 3.0, 'Mar' : 3.1, 'Abr' : 3.0, 'May' : 3.4, 'Jun' : 3.3, 'Jul' : 3.0, 'Ago' : 2.8, 'Sep' : 2.9, 'Oct' : 2.7, 'Nov' : 2.6, 'Dic' : 2.8},
	'Precipitación (mm)' : {
            'Ene' : 45.0, 'Feb' : 36.3, 'Mar' : 43.0, 'Abr' : 15.8, 'May' : 9.2, 'Jun' : 3.7, 'Jul' : 6.8, 'Ago' : 6.4, 'Sep' : 12.4, 'Oct' : 12.7, 'Nov' : 20.1, 'Dic' : 28.4},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 6.3, 'Feb' : 5.0, 'Mar' : 4.4, 'Abr' : 2.6, 'May' : 2.2, 'Jun' : 1.4, 'Jul' : 1.9, 'Ago' : 1.6, 'Sep' : 2.7, 'Oct' : 2.2, 'Nov' : 3.7, 'Dic' : 5.3},
},
{
	'Estación' : 'MENDOZA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 25.5, 'Feb' : 24.0, 'Mar' : 21.3, 'Abr' : 16.2, 'May' : 11.8, 'Jun' : 8.4, 'Jul' : 7.9, 'Ago' : 10.6, 'Sep' : 13.9, 'Oct' : 18.8, 'Nov' : 22.2, 'Dic' : 24.9},
	'Temperatura máxima (°C)' : {
            'Ene' : 32.3, 'Feb' : 30.9, 'Mar' : 27.9, 'Abr' : 23.2, 'May' : 18.7, 'Jun' : 15.7, 'Jul' : 15.0, 'Ago' : 18.3, 'Sep' : 21.1, 'Oct' : 25.9, 'Nov' : 29.2, 'Dic' : 31.8},
	'Temperatura mínima (°C)' : {
            'Ene' : 18.7, 'Feb' : 17.4, 'Mar' : 15.5, 'Abr' : 10.4, 'May' : 6.2, 'Jun' : 2.9, 'Jul' : 2.1, 'Ago' : 4.2, 'Sep' : 7.2, 'Oct' : 11.7, 'Nov' : 15.1, 'Dic' : 17.9},
	'Humedad relativa (%)' : {
            'Ene' : 49.8, 'Feb' : 53.6, 'Mar' : 61.8, 'Abr' : 65.6, 'May' : 68.3, 'Jun' : 69.4, 'Jul' : 64.4, 'Ago' : 55.1, 'Sep' : 51.3, 'Oct' : 45.7, 'Nov' : 44.5, 'Dic' : 45.8},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 8.3, 'Feb' : 6.9, 'Mar' : 6.0, 'Abr' : 4.9, 'May' : 4.5, 'Jun' : 4.3, 'Jul' : 4.9, 'Ago' : 6.0, 'Sep' : 6.7, 'Oct' : 8.1, 'Nov' : 8.9, 'Dic' : 8.8},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.3, 'Feb' : 3.4, 'Mar' : 3.4, 'Abr' : 3.2, 'May' : 3.7, 'Jun' : 3.5, 'Jul' : 3.3, 'Ago' : 3.1, 'Sep' : 3.2, 'Oct' : 3.0, 'Nov' : 3.0, 'Dic' : 3.1},
	'Precipitación (mm)' : {
            'Ene' : 50.5, 'Feb' : 33.7, 'Mar' : 34.9, 'Abr' : 16.5, 'May' : 10.5, 'Jun' : 6.3, 'Jul' : 8.0, 'Ago' : 8.0, 'Sep' : 15.1, 'Oct' : 10.4, 'Nov' : 16.4, 'Dic' : 24.3},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 6.1, 'Feb' : 5.1, 'Mar' : 4.9, 'Abr' : 3.5, 'May' : 3.2, 'Jun' : 2.1, 'Jul' : 2.7, 'Ago' : 2.4, 'Sep' : 3.8, 'Oct' : 3.0, 'Nov' : 4.0, 'Dic' : 4.3},
},
{
	'Estación' : 'MENDOZA OBSERVATORIO', 
	'Temperatura (°C)' : {
            'Ene' : 23.9, 'Feb' : 22.5, 'Mar' : 20.0, 'Abr' : 15.3, 'May' : 11.2, 'Jun' : 8.1, 'Jul' : 7.5, 'Ago' : 10.0, 'Sep' : 13.0, 'Oct' : 17.5, 'Nov' : 20.6, 'Dic' : 23.2},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.4, 'Feb' : 29.1, 'Mar' : 26.5, 'Abr' : 22.0, 'May' : 17.9, 'Jun' : 15.0, 'Jul' : 14.5, 'Ago' : 17.3, 'Sep' : 19.9, 'Oct' : 24.2, 'Nov' : 27.3, 'Dic' : 29.8},
	'Temperatura mínima (°C)' : {
            'Ene' : 18.2, 'Feb' : 16.9, 'Mar' : 15.1, 'Abr' : 10.8, 'May' : 7.0, 'Jun' : 3.9, 'Jul' : 3.1, 'Ago' : 5.1, 'Sep' : 7.4, 'Oct' : 11.5, 'Nov' : 14.5, 'Dic' : 17.3},
	'Humedad relativa (%)' : {
            'Ene' : 53.5, 'Feb' : 58.1, 'Mar' : 64.7, 'Abr' : 66.1, 'May' : 67.8, 'Jun' : 68.8, 'Jul' : 64.8, 'Ago' : 57.3, 'Sep' : 54.9, 'Oct' : 50.7, 'Nov' : 50.5, 'Dic' : 51.3},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 4.4, 'Feb' : 3.8, 'Mar' : 4.0, 'Abr' : 3.4, 'May' : 3.0, 'Jun' : 3.1, 'Jul' : 3.8, 'Ago' : 4.3, 'Sep' : 4.3, 'Oct' : 5.2, 'Nov' : 5.7, 'Dic' : 4.9},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.4, 'Feb' : 3.5, 'Mar' : 3.6, 'Abr' : 3.4, 'May' : 3.8, 'Jun' : 3.7, 'Jul' : 3.4, 'Ago' : 3.2, 'Sep' : 3.4, 'Oct' : 3.1, 'Nov' : 3.1, 'Dic' : 3.3},
	'Precipitación (mm)' : {
            'Ene' : 40.0, 'Feb' : 43.0, 'Mar' : 38.7, 'Abr' : 19.6, 'May' : 12.9, 'Jun' : 8.7, 'Jul' : 10.9, 'Ago' : 10.4, 'Sep' : 18.8, 'Oct' : 13.7, 'Nov' : 20.7, 'Dic' : 28.0},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 7.4, 'Feb' : 6.5, 'Mar' : 7.4, 'Abr' : 4.4, 'May' : 3.7, 'Jun' : 3.2, 'Jul' : 3.5, 'Ago' : 3.4, 'Sep' : 4.9, 'Oct' : 4.0, 'Nov' : 4.4, 'Dic' : 5.7},
},
{
	'Estación' : 'SAN LUIS AERO', 
	'Temperatura (°C)' : {
            'Ene' : 24.4, 'Feb' : 23.2, 'Mar' : 20.8, 'Abr' : 16.6, 'May' : 12.9, 'Jun' : 10.0, 'Jul' : 9.4, 'Ago' : 11.9, 'Sep' : 14.7, 'Oct' : 18.9, 'Nov' : 21.6, 'Dic' : 23.8},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.1, 'Feb' : 30.0, 'Mar' : 27.3, 'Abr' : 23.3, 'May' : 19.7, 'Jun' : 17.0, 'Jul' : 16.6, 'Ago' : 19.3, 'Sep' : 21.8, 'Oct' : 25.8, 'Nov' : 28.4, 'Dic' : 30.5},
	'Temperatura mínima (°C)' : {
            'Ene' : 17.9, 'Feb' : 17.0, 'Mar' : 15.3, 'Abr' : 11.3, 'May' : 7.7, 'Jun' : 4.5, 'Jul' : 3.7, 'Ago' : 5.9, 'Sep' : 8.5, 'Oct' : 12.5, 'Nov' : 15.0, 'Dic' : 17.1},
	'Humedad relativa (%)' : {
            'Ene' : 54.4, 'Feb' : 56.7, 'Mar' : 63.7, 'Abr' : 64.6, 'May' : 64.2, 'Jun' : 62.4, 'Jul' : 57.6, 'Ago' : 49.6, 'Sep' : 47.0, 'Oct' : 46.9, 'Nov' : 48.3, 'Dic' : 51.4},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 18.0, 'Feb' : 16.7, 'Mar' : 15.1, 'Abr' : 14.8, 'May' : 13.8, 'Jun' : 14.2, 'Jul' : 15.4, 'Ago' : 17.3, 'Sep' : 17.9, 'Oct' : 21.7, 'Nov' : 20.9, 'Dic' : 20.1},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.4, 'Feb' : 3.2, 'Mar' : 3.4, 'Abr' : 3.3, 'May' : 3.9, 'Jun' : 3.9, 'Jul' : 3.5, 'Ago' : 3.2, 'Sep' : 3.4, 'Oct' : 3.3, 'Nov' : 3.3, 'Dic' : 3.4},
	'Precipitación (mm)' : {
            'Ene' : 119.5, 'Feb' : 97.5, 'Mar' : 98.9, 'Abr' : 41.4, 'May' : 19.8, 'Jun' : 5.7, 'Jul' : 11.2, 'Ago' : 8.6, 'Sep' : 24.3, 'Oct' : 40.5, 'Nov' : 80.4, 'Dic' : 110.1},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 10.2, 'Feb' : 8.3, 'Mar' : 7.9, 'Abr' : 5.0, 'May' : 3.3, 'Jun' : 1.9, 'Jul' : 2.7, 'Ago' : 2.2, 'Sep' : 4.3, 'Oct' : 5.4, 'Nov' : 7.8, 'Dic' : 10.6},
},
{
	'Estación' : 'VILLA REYNOLDS AERO', 
	'Temperatura (°C)' : {
            'Ene' : 22.9, 'Feb' : 21.7, 'Mar' : 19.5, 'Abr' : 15.1, 'May' : 11.2, 'Jun' : 7.9, 'Jul' : 7.1, 'Ago' : 9.6, 'Sep' : 12.7, 'Oct' : 16.9, 'Nov' : 19.8, 'Dic' : 22.2},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.8, 'Feb' : 30.0, 'Mar' : 27.7, 'Abr' : 23.9, 'May' : 20.3, 'Jun' : 17.4, 'Jul' : 16.9, 'Ago' : 19.7, 'Sep' : 22.0, 'Oct' : 25.2, 'Nov' : 27.8, 'Dic' : 30.0},
	'Temperatura mínima (°C)' : {
            'Ene' : 15.2, 'Feb' : 14.3, 'Mar' : 12.7, 'Abr' : 8.3, 'May' : 4.4, 'Jun' : 1.0, 'Jul' : -0.1, 'Ago' : 1.6, 'Sep' : 4.4, 'Oct' : 8.9, 'Nov' : 11.8, 'Dic' : 14.3},
	'Humedad relativa (%)' : {
            'Ene' : 68.2, 'Feb' : 70.7, 'Mar' : 76.0, 'Abr' : 76.5, 'May' : 76.4, 'Jun' : 75.9, 'Jul' : 72.2, 'Ago' : 65.7, 'Sep' : 63.0, 'Oct' : 62.9, 'Nov' : 63.0, 'Dic' : 65.0},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 12.4, 'Feb' : 11.3, 'Mar' : 10.2, 'Abr' : 8.9, 'May' : 8.5, 'Jun' : 8.4, 'Jul' : 8.9, 'Ago' : 10.5, 'Sep' : 12.3, 'Oct' : 15.1, 'Nov' : 15.8, 'Dic' : 14.3},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.8, 'Feb' : 3.6, 'Mar' : 3.7, 'Abr' : 3.6, 'May' : 4.1, 'Jun' : 4.2, 'Jul' : 3.8, 'Ago' : 3.7, 'Sep' : 3.8, 'Oct' : 4.0, 'Nov' : 3.9, 'Dic' : 3.9},
	'Precipitación (mm)' : {
            'Ene' : 103.7, 'Feb' : 85.7, 'Mar' : 94.6, 'Abr' : 55.0, 'May' : 28.5, 'Jun' : 9.5, 'Jul' : 18.8, 'Ago' : 17.1, 'Sep' : 35.2, 'Oct' : 58.8, 'Nov' : 85.9, 'Dic' : 113.1},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 9.8, 'Feb' : 8.1, 'Mar' : 9.0, 'Abr' : 6.0, 'May' : 4.4, 'Jun' : 2.7, 'Jul' : 3.7, 'Ago' : 3.4, 'Sep' : 5.4, 'Oct' : 8.3, 'Nov' : 9.7, 'Dic' : 10.9},
},
{
	'Estación' : 'RÍO CUARTO AERO', 
	'Temperatura (°C)' : {
            'Ene' : 22.9, 'Feb' : 21.8, 'Mar' : 20.1, 'Abr' : 16.3, 'May' : 12.7, 'Jun' : 9.7, 'Jul' : 8.9, 'Ago' : 11.0, 'Sep' : 13.6, 'Oct' : 17.4, 'Nov' : 20.1, 'Dic' : 22.2},
	'Temperatura máxima (°C)' : {
            'Ene' : 28.9, 'Feb' : 28.0, 'Mar' : 26.3, 'Abr' : 22.7, 'May' : 19.0, 'Jun' : 15.9, 'Jul' : 15.5, 'Ago' : 18.2, 'Sep' : 20.5, 'Oct' : 24.0, 'Nov' : 26.5, 'Dic' : 28.3},
	'Temperatura mínima (°C)' : {
            'Ene' : 17.5, 'Feb' : 16.6, 'Mar' : 15.2, 'Abr' : 11.5, 'May' : 8.0, 'Jun' : 4.9, 'Jul' : 4.0, 'Ago' : 5.6, 'Sep' : 7.9, 'Oct' : 11.6, 'Nov' : 14.3, 'Dic' : 16.6},
	'Humedad relativa (%)' : {
            'Ene' : 67.8, 'Feb' : 70.2, 'Mar' : 74.0, 'Abr' : 72.9, 'May' : 72.2, 'Jun' : 70.9, 'Jul' : 66.8, 'Ago' : 60.2, 'Sep' : 58.6, 'Oct' : 60.8, 'Nov' : 61.2, 'Dic' : 63.8},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 15.9, 'Feb' : 14.3, 'Mar' : 13.7, 'Abr' : 13.8, 'May' : 12.4, 'Jun' : 13.5, 'Jul' : 15.1, 'Ago' : 16.7, 'Sep' : 18.3, 'Oct' : 19.0, 'Nov' : 18.3, 'Dic' : 16.8},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.4, 'Feb' : 3.4, 'Mar' : 3.4, 'Abr' : 3.5, 'May' : 3.9, 'Jun' : 3.9, 'Jul' : 3.5, 'Ago' : 3.3, 'Sep' : 3.5, 'Oct' : 3.7, 'Nov' : 3.6, 'Dic' : 3.6},
	'Precipitación (mm)' : {
            'Ene' : 144.5, 'Feb' : 90.6, 'Mar' : 107.8, 'Abr' : 64.7, 'May' : 31.5, 'Jun' : 8.4, 'Jul' : 14.5, 'Ago' : 13.9, 'Sep' : 40.1, 'Oct' : 75.4, 'Nov' : 128.7, 'Dic' : 138.6},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 9.5, 'Feb' : 7.5, 'Mar' : 8.2, 'Abr' : 6.0, 'May' : 3.9, 'Jun' : 2.4, 'Jul' : 3.3, 'Ago' : 2.6, 'Sep' : 4.7, 'Oct' : 7.6, 'Nov' : 9.1, 'Dic' : 10.3},
},
{
	'Estación' : 'MARCOS JUÁREZ AERO', 
	'Temperatura (°C)' : {
            'Ene' : 23.8, 'Feb' : 22.2, 'Mar' : 20.7, 'Abr' : 16.9, 'May' : 13.3, 'Jun' : 10.2, 'Jul' : 9.3, 'Ago' : 11.4, 'Sep' : 13.9, 'Oct' : 17.9, 'Nov' : 20.9, 'Dic' : 23.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.8, 'Feb' : 29.1, 'Mar' : 27.7, 'Abr' : 24.0, 'May' : 20.4, 'Jun' : 17.0, 'Jul' : 16.7, 'Ago' : 19.6, 'Sep' : 21.7, 'Oct' : 25.3, 'Nov' : 28.1, 'Dic' : 29.9},
	'Temperatura mínima (°C)' : {
            'Ene' : 17.5, 'Feb' : 16.4, 'Mar' : 15.1, 'Abr' : 11.5, 'May' : 8.1, 'Jun' : 5.0, 'Jul' : 3.8, 'Ago' : 5.1, 'Sep' : 7.2, 'Oct' : 11.3, 'Nov' : 14.2, 'Dic' : 16.5},
	'Humedad relativa (%)' : {
            'Ene' : 73.8, 'Feb' : 78.7, 'Mar' : 80.0, 'Abr' : 80.0, 'May' : 80.4, 'Jun' : 81.2, 'Jul' : 78.2, 'Ago' : 73.7, 'Sep' : 70.8, 'Oct' : 70.0, 'Nov' : 68.0, 'Dic' : 70.2},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 8.5, 'Feb' : 8.0, 'Mar' : 9.1, 'Abr' : 8.9, 'May' : 8.9, 'Jun' : 9.0, 'Jul' : 10.4, 'Ago' : 12.4, 'Sep' : 13.7, 'Oct' : 13.9, 'Nov' : 13.3, 'Dic' : 10.4},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.2, 'Feb' : 3.1, 'Mar' : 3.1, 'Abr' : 3.4, 'May' : 3.7, 'Jun' : 4.0, 'Jul' : 3.5, 'Ago' : 3.2, 'Sep' : 3.3, 'Oct' : 3.4, 'Nov' : 3.3, 'Dic' : 3.3},
	'Precipitación (mm)' : {
            'Ene' : 114.3, 'Feb' : 115.0, 'Mar' : 108.1, 'Abr' : 96.3, 'May' : 36.8, 'Jun' : 15.8, 'Jul' : 17.0, 'Ago' : 21.2, 'Sep' : 43.1, 'Oct' : 94.6, 'Nov' : 101.1, 'Dic' : 148.3},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.3, 'Feb' : 7.8, 'Mar' : 8.4, 'Abr' : 7.3, 'May' : 5.0, 'Jun' : 3.7, 'Jul' : 3.4, 'Ago' : 3.6, 'Sep' : 4.9, 'Oct' : 8.0, 'Nov' : 8.7, 'Dic' : 9.6},
},
{
	'Estación' : 'ROSARIO AERO', 
	'Temperatura (°C)' : {
            'Ene' : 24.6, 'Feb' : 23.2, 'Mar' : 21.4, 'Abr' : 17.3, 'May' : 13.8, 'Jun' : 10.7, 'Jul' : 10.0, 'Ago' : 12.1, 'Sep' : 14.5, 'Oct' : 18.1, 'Nov' : 21.0, 'Dic' : 23.4},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.8, 'Feb' : 29.2, 'Mar' : 27.4, 'Abr' : 23.5, 'May' : 19.9, 'Jun' : 16.6, 'Jul' : 16.2, 'Ago' : 18.9, 'Sep' : 20.9, 'Oct' : 24.2, 'Nov' : 27.1, 'Dic' : 29.6},
	'Temperatura mínima (°C)' : {
            'Ene' : 18.4, 'Feb' : 17.5, 'Mar' : 16.0, 'Abr' : 12.1, 'May' : 8.7, 'Jun' : 6.0, 'Jul' : 4.8, 'Ago' : 6.2, 'Sep' : 8.3, 'Oct' : 12.0, 'Nov' : 14.7, 'Dic' : 17.2},
	'Humedad relativa (%)' : {
            'Ene' : 68.2, 'Feb' : 73.7, 'Mar' : 77.2, 'Abr' : 80.0, 'May' : 81.1, 'Jun' : 82.2, 'Jul' : 79.6, 'Ago' : 74.7, 'Sep' : 70.6, 'Oct' : 70.4, 'Nov' : 67.9, 'Dic' : 67.2},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 11.1, 'Feb' : 10.0, 'Mar' : 10.1, 'Abr' : 9.3, 'May' : 9.3, 'Jun' : 10.0, 'Jul' : 11.1, 'Ago' : 12.4, 'Sep' : 13.8, 'Oct' : 14.5, 'Nov' : 13.8, 'Dic' : 11.9},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.2, 'Feb' : 3.3, 'Mar' : 3.1, 'Abr' : 3.5, 'May' : 3.8, 'Jun' : 4.3, 'Jul' : 3.7, 'Ago' : 3.5, 'Sep' : 3.5, 'Oct' : 3.6, 'Nov' : 3.4, 'Dic' : 3.3},
	'Precipitación (mm)' : {
            'Ene' : 111.8, 'Feb' : 120.6, 'Mar' : 144.8, 'Abr' : 111.8, 'May' : 59.0, 'Jun' : 27.7, 'Jul' : 24.7, 'Ago' : 32.4, 'Sep' : 47.4, 'Oct' : 108.5, 'Nov' : 112.3, 'Dic' : 120.6},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 7.9, 'Feb' : 7.6, 'Mar' : 8.1, 'Abr' : 8.2, 'May' : 5.2, 'Jun' : 4.7, 'Jul' : 4.1, 'Ago' : 4.2, 'Sep' : 5.3, 'Oct' : 8.9, 'Nov' : 8.6, 'Dic' : 9.4},
},
{
	'Estación' : 'GUALEGUAYCHÚ AERO', 
	'Temperatura (°C)' : {
            'Ene' : 25.1, 'Feb' : 23.7, 'Mar' : 22.0, 'Abr' : 17.8, 'May' : 14.2, 'Jun' : 11.3, 'Jul' : 10.7, 'Ago' : 12.8, 'Sep' : 14.7, 'Oct' : 18.0, 'Nov' : 20.9, 'Dic' : 23.4},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.6, 'Feb' : 29.8, 'Mar' : 28.2, 'Abr' : 23.9, 'May' : 20.2, 'Jun' : 17.1, 'Jul' : 16.7, 'Ago' : 19.2, 'Sep' : 20.6, 'Oct' : 24.0, 'Nov' : 27.0, 'Dic' : 29.9},
	'Temperatura mínima (°C)' : {
            'Ene' : 18.8, 'Feb' : 18.0, 'Mar' : 16.5, 'Abr' : 12.6, 'May' : 9.3, 'Jun' : 6.7, 'Jul' : 6.0, 'Ago' : 7.4, 'Sep' : 9.0, 'Oct' : 12.1, 'Nov' : 14.7, 'Dic' : 17.0},
	'Humedad relativa (%)' : {
            'Ene' : 65.1, 'Feb' : 71.6, 'Mar' : 74.3, 'Abr' : 78.8, 'May' : 80.7, 'Jun' : 82.5, 'Jul' : 80.3, 'Ago' : 75.9, 'Sep' : 72.9, 'Oct' : 71.9, 'Nov' : 68.9, 'Dic' : 65.4},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 9.2, 'Feb' : 8.1, 'Mar' : 7.9, 'Abr' : 7.6, 'May' : 8.1, 'Jun' : 8.6, 'Jul' : 9.6, 'Ago' : 10.5, 'Sep' : 11.5, 'Oct' : 11.3, 'Nov' : 11.7, 'Dic' : 10.4},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.1, 'Feb' : 3.3, 'Mar' : 3.1, 'Abr' : 3.4, 'May' : 3.7, 'Jun' : 4.1, 'Jul' : 3.7, 'Ago' : 3.6, 'Sep' : 3.5, 'Oct' : 3.5, 'Nov' : 3.3, 'Dic' : 3.2},
	'Precipitación (mm)' : {
            'Ene' : 109.6, 'Feb' : 102.5, 'Mar' : 131.6, 'Abr' : 113.9, 'May' : 82.7, 'Jun' : 56.0, 'Jul' : 50.6, 'Ago' : 54.4, 'Sep' : 71.0, 'Oct' : 110.1, 'Nov' : 119.9, 'Dic' : 116.5},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 7.6, 'Feb' : 7.6, 'Mar' : 8.1, 'Abr' : 8.7, 'May' : 6.6, 'Jun' : 6.5, 'Jul' : 6.1, 'Ago' : 5.8, 'Sep' : 6.9, 'Oct' : 9.2, 'Nov' : 8.3, 'Dic' : 8.6},
},
{
	'Estación' : 'MALARGÜE AERO', 
	'Temperatura (°C)' : {
            'Ene' : 20.0, 'Feb' : 18.7, 'Mar' : 16.2, 'Abr' : 11.3, 'May' : 7.1, 'Jun' : 4.6, 'Jul' : 3.6, 'Ago' : 5.5, 'Sep' : 8.2, 'Oct' : 12.6, 'Nov' : 16.0, 'Dic' : 19.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 28.5, 'Feb' : 27.1, 'Mar' : 24.7, 'Abr' : 19.9, 'May' : 15.0, 'Jun' : 12.1, 'Jul' : 11.4, 'Ago' : 13.7, 'Sep' : 16.3, 'Oct' : 20.6, 'Nov' : 24.3, 'Dic' : 27.2},
	'Temperatura mínima (°C)' : {
            'Ene' : 11.2, 'Feb' : 10.5, 'Mar' : 8.8, 'Abr' : 4.4, 'May' : 1.0, 'Jun' : -1.1, 'Jul' : -2.4, 'Ago' : -1.2, 'Sep' : 0.9, 'Oct' : 4.4, 'Nov' : 7.2, 'Dic' : 10.1},
	'Humedad relativa (%)' : {
            'Ene' : 46.0, 'Feb' : 51.6, 'Mar' : 58.2, 'Abr' : 62.0, 'May' : 64.2, 'Jun' : 66.3, 'Jul' : 64.2, 'Ago' : 59.0, 'Sep' : 53.5, 'Oct' : 45.8, 'Nov' : 42.8, 'Dic' : 43.1},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 8.7, 'Feb' : 7.9, 'Mar' : 6.5, 'Abr' : 6.9, 'May' : 6.9, 'Jun' : 8.1, 'Jul' : 9.6, 'Ago' : 9.4, 'Sep' : 9.4, 'Oct' : 10.8, 'Nov' : 10.7, 'Dic' : 10.1},
	'Nubosidad total (octavos)' : {
            'Ene' : 2.6, 'Feb' : 2.8, 'Mar' : 3.1, 'Abr' : 3.3, 'May' : 4.0, 'Jun' : 4.1, 'Jul' : 3.9, 'Ago' : 3.7, 'Sep' : 3.7, 'Oct' : 3.5, 'Nov' : 3.1, 'Dic' : 2.8},
	'Precipitación (mm)' : {
            'Ene' : 25.0, 'Feb' : 26.4, 'Mar' : 33.5, 'Abr' : 22.9, 'May' : 26.9, 'Jun' : 38.7, 'Jul' : 34.1, 'Ago' : 30.1, 'Sep' : 23.9, 'Oct' : 19.6, 'Nov' : 22.3, 'Dic' : 29.6},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 5.0, 'Feb' : 5.7, 'Mar' : 4.9, 'Abr' : 3.5, 'May' : 4.9, 'Jun' : 6.0, 'Jul' : 4.9, 'Ago' : 5.0, 'Sep' : 5.2, 'Oct' : 4.0, 'Nov' : 3.7, 'Dic' : 4.3},
},
{
	'Estación' : 'SAN RAFAEL AERO', 
	'Temperatura (°C)' : {
            'Ene' : 23.3, 'Feb' : 22.0, 'Mar' : 19.3, 'Abr' : 14.5, 'May' : 10.5, 'Jun' : 7.7, 'Jul' : 6.9, 'Ago' : 9.0, 'Sep' : 11.8, 'Oct' : 16.3, 'Nov' : 19.6, 'Dic' : 22.4},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.1, 'Feb' : 30.0, 'Mar' : 27.0, 'Abr' : 22.5, 'May' : 18.5, 'Jun' : 15.8, 'Jul' : 15.2, 'Ago' : 17.6, 'Sep' : 19.8, 'Oct' : 24.2, 'Nov' : 27.5, 'Dic' : 30.2},
	'Temperatura mínima (°C)' : {
            'Ene' : 15.4, 'Feb' : 14.5, 'Mar' : 12.8, 'Abr' : 8.4, 'May' : 4.8, 'Jun' : 2.0, 'Jul' : 0.9, 'Ago' : 2.4, 'Sep' : 4.7, 'Oct' : 8.3, 'Nov' : 11.2, 'Dic' : 14.0},
	'Humedad relativa (%)' : {
            'Ene' : 53.6, 'Feb' : 56.8, 'Mar' : 63.6, 'Abr' : 66.9, 'May' : 68.0, 'Jun' : 66.1, 'Jul' : 63.4, 'Ago' : 57.2, 'Sep' : 55.8, 'Oct' : 51.9, 'Nov' : 50.2, 'Dic' : 50.7},
	'Velocidad del Viento (km/h)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Nubosidad total (octavos)' : {
            'Ene' : 2.7, 'Feb' : 2.7, 'Mar' : 2.9, 'Abr' : 2.9, 'May' : 3.4, 'Jun' : 3.4, 'Jul' : 3.2, 'Ago' : 3.0, 'Sep' : 3.1, 'Oct' : 3.0, 'Nov' : 2.8, 'Dic' : 2.6},
	'Precipitación (mm)' : {
            'Ene' : 61.0, 'Feb' : 42.8, 'Mar' : 37.2, 'Abr' : 26.1, 'May' : 15.6, 'Jun' : 9.1, 'Jul' : 13.2, 'Ago' : 16.0, 'Sep' : 27.4, 'Oct' : 30.5, 'Nov' : 38.6, 'Dic' : 45.3},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 7.5, 'Feb' : 6.1, 'Mar' : 5.3, 'Abr' : 4.1, 'May' : 3.7, 'Jun' : 2.9, 'Jul' : 2.8, 'Ago' : 3.3, 'Sep' : 4.7, 'Oct' : 4.7, 'Nov' : 5.7, 'Dic' : 6.7},
},
{
	'Estación' : 'GENERAL PICO AERO', 
	'Temperatura (°C)' : {
            'Ene' : 23.8, 'Feb' : 22.5, 'Mar' : 20.2, 'Abr' : 16.0, 'May' : 12.0, 'Jun' : 8.8, 'Jul' : 8.1, 'Ago' : 10.4, 'Sep' : 13.1, 'Oct' : 16.7, 'Nov' : 20.0, 'Dic' : 22.8},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.7, 'Feb' : 29.7, 'Mar' : 27.2, 'Abr' : 22.9, 'May' : 18.7, 'Jun' : 15.2, 'Jul' : 14.8, 'Ago' : 17.7, 'Sep' : 20.2, 'Oct' : 23.6, 'Nov' : 27.0, 'Dic' : 29.7},
	'Temperatura mínima (°C)' : {
            'Ene' : 16.9, 'Feb' : 15.8, 'Mar' : 14.4, 'Abr' : 10.3, 'May' : 6.6, 'Jun' : 3.6, 'Jul' : 2.6, 'Ago' : 4.1, 'Sep' : 6.5, 'Oct' : 10.2, 'Nov' : 13.2, 'Dic' : 15.8},
	'Humedad relativa (%)' : {
            'Ene' : 64.7, 'Feb' : 67.4, 'Mar' : 72.2, 'Abr' : 73.8, 'May' : 76.5, 'Jun' : 78.2, 'Jul' : 75.1, 'Ago' : 67.2, 'Sep' : 65.2, 'Oct' : 65.1, 'Nov' : 60.1, 'Dic' : 59.7},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 12.4, 'Feb' : 10.8, 'Mar' : 10.9, 'Abr' : 9.6, 'May' : 9.8, 'Jun' : 9.5, 'Jul' : 10.7, 'Ago' : 14.1, 'Sep' : 14.4, 'Oct' : 15.6, 'Nov' : 15.5, 'Dic' : 13.6},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.2, 'Feb' : 3.0, 'Mar' : 3.4, 'Abr' : 3.4, 'May' : 3.8, 'Jun' : 4.2, 'Jul' : 3.9, 'Ago' : 3.5, 'Sep' : 3.7, 'Oct' : 3.7, 'Nov' : 3.4, 'Dic' : 3.3},
	'Precipitación (mm)' : {
            'Ene' : 111.2, 'Feb' : 102.7, 'Mar' : 143.8, 'Abr' : 70.4, 'May' : 32.8, 'Jun' : 17.4, 'Jul' : 22.0, 'Ago' : 24.9, 'Sep' : 55.2, 'Oct' : 87.2, 'Nov' : 99.8, 'Dic' : 124.4},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.5, 'Feb' : 6.7, 'Mar' : 8.9, 'Abr' : 6.2, 'May' : 4.7, 'Jun' : 3.8, 'Jul' : 4.2, 'Ago' : 3.4, 'Sep' : 5.9, 'Oct' : 8.9, 'Nov' : 8.4, 'Dic' : 8.9},
},
{
	'Estación' : 'LABOULAYE AERO', 
	'Temperatura (°C)' : {
            'Ene' : 23.1, 'Feb' : 21.9, 'Mar' : 19.9, 'Abr' : 15.8, 'May' : 12.2, 'Jun' : 8.9, 'Jul' : 8.1, 'Ago' : 10.2, 'Sep' : 12.8, 'Oct' : 16.6, 'Nov' : 19.6, 'Dic' : 22.2},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.3, 'Feb' : 29.3, 'Mar' : 27.1, 'Abr' : 23.0, 'May' : 19.3, 'Jun' : 15.9, 'Jul' : 15.5, 'Ago' : 18.3, 'Sep' : 20.7, 'Oct' : 23.8, 'Nov' : 26.9, 'Dic' : 29.3},
	'Temperatura mínima (°C)' : {
            'Ene' : 16.7, 'Feb' : 15.6, 'Mar' : 14.2, 'Abr' : 10.4, 'May' : 6.9, 'Jun' : 3.8, 'Jul' : 2.7, 'Ago' : 3.9, 'Sep' : 6.2, 'Oct' : 10.2, 'Nov' : 13.1, 'Dic' : 15.7},
	'Humedad relativa (%)' : {
            'Ene' : 70.3, 'Feb' : 72.9, 'Mar' : 77.1, 'Abr' : 77.6, 'May' : 78.1, 'Jun' : 78.3, 'Jul' : 74.7, 'Ago' : 68.8, 'Sep' : 66.7, 'Oct' : 68.2, 'Nov' : 66.5, 'Dic' : 66.7},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 10.2, 'Feb' : 8.6, 'Mar' : 9.2, 'Abr' : 8.1, 'May' : 8.0, 'Jun' : 8.0, 'Jul' : 8.9, 'Ago' : 11.5, 'Sep' : 12.9, 'Oct' : 14.8, 'Nov' : 14.5, 'Dic' : 12.6},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.4, 'Feb' : 3.2, 'Mar' : 3.4, 'Abr' : 3.6, 'May' : 4.1, 'Jun' : 4.3, 'Jul' : 3.9, 'Ago' : 3.6, 'Sep' : 3.6, 'Oct' : 3.8, 'Nov' : 3.5, 'Dic' : 3.5},
	'Precipitación (mm)' : {
            'Ene' : 120.7, 'Feb' : 105.7, 'Mar' : 138.8, 'Abr' : 83.4, 'May' : 36.0, 'Jun' : 11.7, 'Jul' : 17.6, 'Ago' : 17.2, 'Sep' : 47.3, 'Oct' : 91.0, 'Nov' : 105.0, 'Dic' : 128.7},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 9.9, 'Feb' : 8.1, 'Mar' : 9.4, 'Abr' : 7.5, 'May' : 4.9, 'Jun' : 3.9, 'Jul' : 4.1, 'Ago' : 3.6, 'Sep' : 5.7, 'Oct' : 9.3, 'Nov' : 10.3, 'Dic' : 10.9},
},
{
	'Estación' : 'PEHUAJÓ AERO', 
	'Temperatura (°C)' : {
            'Ene' : 22.5, 'Feb' : 21.3, 'Mar' : 19.2, 'Abr' : 15.3, 'May' : 11.8, 'Jun' : 8.6, 'Jul' : 8.0, 'Ago' : 9.9, 'Sep' : 12.3, 'Oct' : 15.6, 'Nov' : 18.6, 'Dic' : 21.4},
	'Temperatura máxima (°C)' : {
            'Ene' : 29.6, 'Feb' : 28.3, 'Mar' : 26.1, 'Abr' : 22.0, 'May' : 17.9, 'Jun' : 14.4, 'Jul' : 14.0, 'Ago' : 16.7, 'Sep' : 18.8, 'Oct' : 22.0, 'Nov' : 25.3, 'Dic' : 28.3},
	'Temperatura mínima (°C)' : {
            'Ene' : 16.1, 'Feb' : 14.9, 'Mar' : 13.4, 'Abr' : 9.9, 'May' : 6.7, 'Jun' : 3.9, 'Jul' : 3.0, 'Ago' : 4.2, 'Sep' : 6.3, 'Oct' : 9.9, 'Nov' : 12.5, 'Dic' : 14.9},
	'Humedad relativa (%)' : {
            'Ene' : 69.9, 'Feb' : 73.5, 'Mar' : 77.6, 'Abr' : 78.4, 'May' : 80.3, 'Jun' : 82.0, 'Jul' : 79.8, 'Ago' : 74.2, 'Sep' : 72.6, 'Oct' : 73.1, 'Nov' : 70.0, 'Dic' : 67.9},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 12.0, 'Feb' : 10.7, 'Mar' : 11.7, 'Abr' : 9.9, 'May' : 9.2, 'Jun' : 9.0, 'Jul' : 10.3, 'Ago' : 12.8, 'Sep' : 14.0, 'Oct' : 15.5, 'Nov' : 15.0, 'Dic' : 14.4},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.4, 'Feb' : 3.2, 'Mar' : 3.4, 'Abr' : 3.5, 'May' : 4.0, 'Jun' : 4.3, 'Jul' : 4.1, 'Ago' : 3.8, 'Sep' : 3.8, 'Oct' : 3.9, 'Nov' : 3.6, 'Dic' : 3.4},
	'Precipitación (mm)' : {
            'Ene' : 119.6, 'Feb' : 101.2, 'Mar' : 149.3, 'Abr' : 79.9, 'May' : 49.0, 'Jun' : 25.8, 'Jul' : 24.0, 'Ago' : 28.8, 'Sep' : 63.6, 'Oct' : 116.1, 'Nov' : 104.3, 'Dic' : 107.0},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.6, 'Feb' : 6.6, 'Mar' : 8.8, 'Abr' : 6.5, 'May' : 5.3, 'Jun' : 4.5, 'Jul' : 4.5, 'Ago' : 4.1, 'Sep' : 5.9, 'Oct' : 9.2, 'Nov' : 8.0, 'Dic' : 8.8},
},
{
	'Estación' : 'JUNÍN AERO', 
	'Temperatura (°C)' : {
            'Ene' : 23.0, 'Feb' : 21.7, 'Mar' : 19.7, 'Abr' : 15.8, 'May' : 12.4, 'Jun' : 9.3, 'Jul' : 8.6, 'Ago' : 10.7, 'Sep' : 12.9, 'Oct' : 16.3, 'Nov' : 19.4, 'Dic' : 22.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 29.8, 'Feb' : 28.4, 'Mar' : 26.6, 'Abr' : 22.6, 'May' : 19.0, 'Jun' : 15.5, 'Jul' : 15.0, 'Ago' : 17.7, 'Sep' : 19.7, 'Oct' : 22.7, 'Nov' : 26.0, 'Dic' : 28.8},
	'Temperatura mínima (°C)' : {
            'Ene' : 16.6, 'Feb' : 15.8, 'Mar' : 14.2, 'Abr' : 10.4, 'May' : 7.2, 'Jun' : 4.5, 'Jul' : 3.6, 'Ago' : 4.8, 'Sep' : 6.7, 'Oct' : 10.1, 'Nov' : 12.8, 'Dic' : 15.2},
	'Humedad relativa (%)' : {
            'Ene' : 69.6, 'Feb' : 74.4, 'Mar' : 77.2, 'Abr' : 77.8, 'May' : 78.5, 'Jun' : 79.3, 'Jul' : 77.1, 'Ago' : 72.3, 'Sep' : 70.1, 'Oct' : 71.1, 'Nov' : 67.8, 'Dic' : 65.9},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 11.6, 'Feb' : 9.9, 'Mar' : 10.6, 'Abr' : 9.7, 'May' : 10.1, 'Jun' : 10.2, 'Jul' : 11.4, 'Ago' : 13.1, 'Sep' : 14.5, 'Oct' : 15.2, 'Nov' : 15.5, 'Dic' : 13.4},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.4, 'Feb' : 3.3, 'Mar' : 3.3, 'Abr' : 3.5, 'May' : 3.9, 'Jun' : 4.3, 'Jul' : 4.0, 'Ago' : 3.7, 'Sep' : 3.7, 'Oct' : 3.8, 'Nov' : 3.6, 'Dic' : 3.5},
	'Precipitación (mm)' : {
            'Ene' : 132.3, 'Feb' : 118.8, 'Mar' : 133.2, 'Abr' : 109.1, 'May' : 61.2, 'Jun' : 26.8, 'Jul' : 31.5, 'Ago' : 32.4, 'Sep' : 55.3, 'Oct' : 122.8, 'Nov' : 110.7, 'Dic' : 110.0},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.2, 'Feb' : 7.8, 'Mar' : 9.0, 'Abr' : 7.6, 'May' : 5.3, 'Jun' : 4.4, 'Jul' : 4.8, 'Ago' : 4.5, 'Sep' : 5.9, 'Oct' : 9.9, 'Nov' : 9.2, 'Dic' : 8.6},
},
{
	'Estación' : 'NUEVE DE JULIO', 
	'Temperatura (°C)' : {
            'Ene' : 23.5, 'Feb' : 22.1, 'Mar' : 19.8, 'Abr' : 15.8, 'May' : 12.2, 'Jun' : 9.2, 'Jul' : 8.7, 'Ago' : 10.7, 'Sep' : 13.1, 'Oct' : 16.2, 'Nov' : 19.5, 'Dic' : 22.2},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.5, 'Feb' : 29.1, 'Mar' : 26.8, 'Abr' : 22.5, 'May' : 18.7, 'Jun' : 15.0, 'Jul' : 14.5, 'Ago' : 17.2, 'Sep' : 19.4, 'Oct' : 22.6, 'Nov' : 26.1, 'Dic' : 29.1},
	'Temperatura mínima (°C)' : {
            'Ene' : 16.7, 'Feb' : 15.9, 'Mar' : 14.3, 'Abr' : 10.6, 'May' : 7.5, 'Jun' : 4.8, 'Jul' : 4.0, 'Ago' : 5.3, 'Sep' : 7.0, 'Oct' : 10.3, 'Nov' : 12.9, 'Dic' : 15.3},
	'Humedad relativa (%)' : {
            'Ene' : 64.3, 'Feb' : 69.1, 'Mar' : 74.1, 'Abr' : 76.0, 'May' : 78.3, 'Jun' : 78.9, 'Jul' : 77.0, 'Ago' : 70.4, 'Sep' : 68.2, 'Oct' : 69.0, 'Nov' : 65.1, 'Dic' : 63.4},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 9.6, 'Feb' : 8.4, 'Mar' : 8.8, 'Abr' : 8.4, 'May' : 8.8, 'Jun' : 8.2, 'Jul' : 9.4, 'Ago' : 10.7, 'Sep' : 10.9, 'Oct' : 11.7, 'Nov' : 11.3, 'Dic' : 10.3},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.1, 'Feb' : 3.1, 'Mar' : 3.3, 'Abr' : 3.4, 'May' : 3.8, 'Jun' : 4.2, 'Jul' : 4.0, 'Ago' : 3.6, 'Sep' : 3.6, 'Oct' : 3.6, 'Nov' : 3.5, 'Dic' : 3.2},
	'Precipitación (mm)' : {
            'Ene' : 127.9, 'Feb' : 114.2, 'Mar' : 144.8, 'Abr' : 110.3, 'May' : 60.8, 'Jun' : 38.4, 'Jul' : 38.3, 'Ago' : 35.2, 'Sep' : 61.7, 'Oct' : 113.0, 'Nov' : 108.8, 'Dic' : 106.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.9, 'Feb' : 7.4, 'Mar' : 9.5, 'Abr' : 8.1, 'May' : 6.5, 'Jun' : 5.9, 'Jul' : 6.6, 'Ago' : 5.1, 'Sep' : 6.5, 'Oct' : 10.3, 'Nov' : 9.7, 'Dic' : 9.5},
},
{
	'Estación' : 'SAN MIGUEL', 
	'Temperatura (°C)' : {
            'Ene' : 24.2, 'Feb' : 22.7, 'Mar' : 20.9, 'Abr' : 16.9, 'May' : 13.4, 'Jun' : 10.6, 'Jul' : 10.2, 'Ago' : 12.0, 'Sep' : 14.0, 'Oct' : 17.1, 'Nov' : 20.0, 'Dic' : 22.5},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.1, 'Feb' : 28.5, 'Mar' : 26.7, 'Abr' : 22.6, 'May' : 19.0, 'Jun' : 15.7, 'Jul' : 15.2, 'Ago' : 17.6, 'Sep' : 19.3, 'Oct' : 22.6, 'Nov' : 25.5, 'Dic' : 28.4},
	'Temperatura mínima (°C)' : {
            'Ene' : 18.6, 'Feb' : 17.8, 'Mar' : 16.1, 'Abr' : 12.2, 'May' : 9.0, 'Jun' : 6.6, 'Jul' : 6.0, 'Ago' : 7.2, 'Sep' : 9.0, 'Oct' : 11.9, 'Nov' : 14.6, 'Dic' : 17.1},
	'Humedad relativa (%)' : {
            'Ene' : 69.4, 'Feb' : 74.4, 'Mar' : 77.6, 'Abr' : 80.6, 'May' : 82.7, 'Jun' : 82.8, 'Jul' : 81.0, 'Ago' : 76.9, 'Sep' : 74.2, 'Oct' : 73.1, 'Nov' : 70.9, 'Dic' : 69.5},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 8.6, 'Feb' : 7.4, 'Mar' : 6.6, 'Abr' : 6.1, 'May' : 6.1, 'Jun' : 6.6, 'Jul' : 6.5, 'Ago' : 7.8, 'Sep' : 8.8, 'Oct' : 9.2, 'Nov' : 9.1, 'Dic' : 8.7},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.9, 'Feb' : 3.7, 'Mar' : 3.7, 'Abr' : 4.0, 'May' : 4.4, 'Jun' : 4.8, 'Jul' : 4.6, 'Ago' : 4.3, 'Sep' : 4.3, 'Oct' : 4.1, 'Nov' : 4.1, 'Dic' : 3.9},
	'Precipitación (mm)' : {
            'Ene' : 116.3, 'Feb' : 128.6, 'Mar' : 118.0, 'Abr' : 110.1, 'May' : 74.1, 'Jun' : 51.4, 'Jul' : 59.7, 'Ago' : 58.6, 'Sep' : None, 'Oct' : 124.9, 'Nov' : 121.5, 'Dic' : 108.4},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.4, 'Feb' : 8.2, 'Mar' : 8.6, 'Abr' : 9.9, 'May' : 7.1, 'Jun' : 7.5, 'Jul' : 7.3, 'Ago' : 6.7, 'Sep' : None, 'Oct' : 9.9, 'Nov' : 9.9, 'Dic' : 9.2},
},
{
	'Estación' : 'EL PALOMAR AERO', 
	'Temperatura (°C)' : {
            'Ene' : 24.1, 'Feb' : 22.9, 'Mar' : 20.9, 'Abr' : 16.7, 'May' : 13.1, 'Jun' : 10.2, 'Jul' : 9.6, 'Ago' : 11.6, 'Sep' : 13.6, 'Oct' : 16.8, 'Nov' : 19.7, 'Dic' : 22.4},
	'Temperatura máxima (°C)' : {
            'Ene' : 29.9, 'Feb' : 28.5, 'Mar' : 26.5, 'Abr' : 22.5, 'May' : 18.9, 'Jun' : 15.7, 'Jul' : 15.1, 'Ago' : 17.4, 'Sep' : 19.2, 'Oct' : 22.3, 'Nov' : 25.2, 'Dic' : 28.3},
	'Temperatura mínima (°C)' : {
            'Ene' : 18.1, 'Feb' : 17.3, 'Mar' : 15.5, 'Abr' : 11.4, 'May' : 7.9, 'Jun' : 5.5, 'Jul' : 4.8, 'Ago' : 6.2, 'Sep' : 8.0, 'Oct' : 11.2, 'Nov' : 13.7, 'Dic' : 16.4},
	'Humedad relativa (%)' : {
            'Ene' : 65.8, 'Feb' : 70.8, 'Mar' : 74.9, 'Abr' : 78.9, 'May' : 80.7, 'Jun' : 81.0, 'Jul' : 79.4, 'Ago' : 75.9, 'Sep' : 72.3, 'Oct' : 71.9, 'Nov' : 68.9, 'Dic' : 65.8},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 11.4, 'Feb' : 10.9, 'Mar' : 9.6, 'Abr' : 8.7, 'May' : 8.6, 'Jun' : 9.1, 'Jul' : 9.8, 'Ago' : 11.0, 'Sep' : 12.6, 'Oct' : 11.9, 'Nov' : 12.1, 'Dic' : 11.7},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.5, 'Feb' : 3.4, 'Mar' : 3.4, 'Abr' : 3.7, 'May' : 4.0, 'Jun' : 4.4, 'Jul' : 4.2, 'Ago' : 4.0, 'Sep' : 3.9, 'Oct' : 4.0, 'Nov' : 3.8, 'Dic' : 3.5},
	'Precipitación (mm)' : {
            'Ene' : 117.5, 'Feb' : 115.0, 'Mar' : 121.9, 'Abr' : 104.3, 'May' : 78.9, 'Jun' : 49.7, 'Jul' : 50.3, 'Ago' : 54.5, 'Sep' : 57.2, 'Oct' : 117.7, 'Nov' : 106.6, 'Dic' : 105.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 7.6, 'Feb' : 7.3, 'Mar' : 7.9, 'Abr' : 8.0, 'May' : 6.0, 'Jun' : 6.0, 'Jul' : 5.9, 'Ago' : 6.0, 'Sep' : 6.6, 'Oct' : 9.0, 'Nov' : 8.5, 'Dic' : 7.9},
},
{
	'Estación' : 'EZEIZA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 23.9, 'Feb' : 22.7, 'Mar' : 20.8, 'Abr' : 16.7, 'May' : 13.2, 'Jun' : 10.3, 'Jul' : 9.6, 'Ago' : 11.5, 'Sep' : 13.4, 'Oct' : 16.7, 'Nov' : 19.6, 'Dic' : 22.3},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.2, 'Feb' : 28.5, 'Mar' : 26.7, 'Abr' : 22.5, 'May' : 18.8, 'Jun' : 15.6, 'Jul' : 14.9, 'Ago' : 17.3, 'Sep' : 19.0, 'Oct' : 22.2, 'Nov' : 25.4, 'Dic' : 28.5},
	'Temperatura mínima (°C)' : {
            'Ene' : 17.7, 'Feb' : 16.9, 'Mar' : 15.3, 'Abr' : 11.4, 'May' : 8.2, 'Jun' : 5.8, 'Jul' : 4.9, 'Ago' : 6.1, 'Sep' : 7.8, 'Oct' : 10.9, 'Nov' : 13.5, 'Dic' : 15.9},
	'Humedad relativa (%)' : {
            'Ene' : 66.3, 'Feb' : 71.6, 'Mar' : 75.3, 'Abr' : 78.6, 'May' : 79.4, 'Jun' : 79.7, 'Jul' : 78.9, 'Ago' : 75.7, 'Sep' : 72.9, 'Oct' : 72.0, 'Nov' : 69.3, 'Dic' : 66.2},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 13.3, 'Feb' : 12.5, 'Mar' : 11.2, 'Abr' : 10.5, 'May' : 10.3, 'Jun' : 10.9, 'Jul' : 11.5, 'Ago' : 12.5, 'Sep' : 14.1, 'Oct' : 13.7, 'Nov' : 13.9, 'Dic' : 13.4},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.6, 'Feb' : 3.6, 'Mar' : 3.6, 'Abr' : 3.8, 'May' : 4.3, 'Jun' : 4.7, 'Jul' : 4.5, 'Ago' : 4.3, 'Sep' : 4.2, 'Oct' : 4.1, 'Nov' : 4.0, 'Dic' : 3.7},
	'Precipitación (mm)' : {
            'Ene' : 101.7, 'Feb' : 113.1, 'Mar' : 114.4, 'Abr' : 93.2, 'May' : 76.6, 'Jun' : 47.3, 'Jul' : 47.2, 'Ago' : 55.1, 'Sep' : 59.7, 'Oct' : 110.5, 'Nov' : 103.0, 'Dic' : 98.0},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 7.6, 'Feb' : 7.6, 'Mar' : 8.3, 'Abr' : 8.3, 'May' : 6.5, 'Jun' : 6.7, 'Jul' : 6.7, 'Ago' : 6.6, 'Sep' : 7.0, 'Oct' : 9.6, 'Nov' : 9.3, 'Dic' : 8.4},
},
{
	'Estación' : 'AEROPARQUE AERO', 
	'Temperatura (°C)' : {
            'Ene' : 24.5, 'Feb' : 23.5, 'Mar' : 22.0, 'Abr' : 18.2, 'May' : 15.0, 'Jun' : 12.0, 'Jul' : 11.2, 'Ago' : 12.7, 'Sep' : 14.4, 'Oct' : 17.7, 'Nov' : 20.3, 'Dic' : 22.9},
	'Temperatura máxima (°C)' : {
            'Ene' : 28.4, 'Feb' : 27.2, 'Mar' : 25.5, 'Abr' : 21.7, 'May' : 18.3, 'Jun' : 15.1, 'Jul' : 14.3, 'Ago' : 16.3, 'Sep' : 17.9, 'Oct' : 21.2, 'Nov' : 24.2, 'Dic' : 27.0},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.8, 'Feb' : 20.0, 'Mar' : 18.6, 'Abr' : 14.9, 'May' : 11.9, 'Jun' : 9.1, 'Jul' : 8.3, 'Ago' : 9.6, 'Sep' : 11.1, 'Oct' : 14.1, 'Nov' : 16.6, 'Dic' : 19.1},
	'Humedad relativa (%)' : {
            'Ene' : 67.8, 'Feb' : 70.9, 'Mar' : 72.3, 'Abr' : 74.6, 'May' : 75.5, 'Jun' : 77.5, 'Jul' : 76.6, 'Ago' : 74.8, 'Sep' : 72.2, 'Oct' : 70.5, 'Nov' : 68.7, 'Dic' : 66.6},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 17.2, 'Feb' : 16.4, 'Mar' : 15.5, 'Abr' : 14.1, 'May' : 13.7, 'Jun' : 13.4, 'Jul' : 14.2, 'Ago' : 15.3, 'Sep' : 17.7, 'Oct' : 17.7, 'Nov' : 18.1, 'Dic' : 17.4},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.1, 'Feb' : 3.2, 'Mar' : 3.2, 'Abr' : 3.4, 'May' : 3.9, 'Jun' : 4.3, 'Jul' : 4.1, 'Ago' : 3.9, 'Sep' : 3.8, 'Oct' : 3.7, 'Nov' : 3.5, 'Dic' : 3.3},
	'Precipitación (mm)' : {
            'Ene' : 117.4, 'Feb' : 107.7, 'Mar' : 127.6, 'Abr' : 105.6, 'May' : 84.4, 'Jun' : 48.7, 'Jul' : 52.8, 'Ago' : 56.3, 'Sep' : 61.7, 'Oct' : 110.4, 'Nov' : 103.7, 'Dic' : 105.2},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.3, 'Feb' : 7.9, 'Mar' : 8.3, 'Abr' : 8.3, 'May' : 6.3, 'Jun' : 6.3, 'Jul' : 6.5, 'Ago' : 6.1, 'Sep' : 6.8, 'Oct' : 9.4, 'Nov' : 8.9, 'Dic' : 8.2},
},
{
	'Estación' : 'BUENOS AIRES', 
	'Temperatura (°C)' : {
            'Ene' : 24.9, 'Feb' : 23.6, 'Mar' : 21.9, 'Abr' : 17.9, 'May' : 14.6, 'Jun' : 11.6, 'Jul' : 11.0, 'Ago' : 12.8, 'Sep' : 14.6, 'Oct' : 17.9, 'Nov' : 20.6, 'Dic' : 23.3},
	'Temperatura máxima (°C)' : {
            'Ene' : 30.1, 'Feb' : 28.7, 'Mar' : 26.8, 'Abr' : 22.9, 'May' : 19.3, 'Jun' : 16.0, 'Jul' : 15.3, 'Ago' : 17.7, 'Sep' : 19.3, 'Oct' : 22.7, 'Nov' : 25.6, 'Dic' : 28.5},
	'Temperatura mínima (°C)' : {
            'Ene' : 20.1, 'Feb' : 19.2, 'Mar' : 17.7, 'Abr' : 13.8, 'May' : 10.7, 'Jun' : 8.1, 'Jul' : 7.4, 'Ago' : 8.8, 'Sep' : 10.3, 'Oct' : 13.3, 'Nov' : 15.9, 'Dic' : 18.4},
	'Humedad relativa (%)' : {
            'Ene' : 64.7, 'Feb' : 69.7, 'Mar' : 72.6, 'Abr' : 76.3, 'May' : 77.5, 'Jun' : 78.7, 'Jul' : 77.4, 'Ago' : 73.2, 'Sep' : 70.1, 'Oct' : 69.1, 'Nov' : 66.7, 'Dic' : 63.6},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 10.0, 'Feb' : 9.5, 'Mar' : 8.8, 'Abr' : 7.7, 'May' : 7.9, 'Jun' : 8.2, 'Jul' : 8.6, 'Ago' : 9.2, 'Sep' : 10.2, 'Oct' : 10.1, 'Nov' : 10.2, 'Dic' : 10.2},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.3, 'Feb' : 3.3, 'Mar' : 3.3, 'Abr' : 3.5, 'May' : 4.0, 'Jun' : 4.4, 'Jul' : 4.1, 'Ago' : 4.0, 'Sep' : 3.9, 'Oct' : 3.8, 'Nov' : 3.7, 'Dic' : 3.4},
	'Precipitación (mm)' : {
            'Ene' : 138.7, 'Feb' : 127.2, 'Mar' : 140.1, 'Abr' : 118.9, 'May' : 92.3, 'Jun' : 58.7, 'Jul' : 60.5, 'Ago' : 64.4, 'Sep' : 72.2, 'Oct' : 127.2, 'Nov' : 117.5, 'Dic' : 118.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 9.0, 'Feb' : 8.0, 'Mar' : 8.8, 'Abr' : 9.1, 'May' : 7.1, 'Jun' : 7.1, 'Jul' : 7.2, 'Ago' : 6.8, 'Sep' : 7.4, 'Oct' : 10.2, 'Nov' : 9.8, 'Dic' : 9.2},
},
{
	'Estación' : 'LA PLATA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 22.8, 'Feb' : 21.8, 'Mar' : 20.0, 'Abr' : 16.2, 'May' : 12.7, 'Jun' : 9.9, 'Jul' : 8.9, 'Ago' : 10.7, 'Sep' : 12.5, 'Oct' : 15.7, 'Nov' : 18.4, 'Dic' : 21.1},
	'Temperatura máxima (°C)' : {
            'Ene' : 28.9, 'Feb' : 27.6, 'Mar' : 25.7, 'Abr' : 21.8, 'May' : 18.0, 'Jun' : 14.7, 'Jul' : 14.0, 'Ago' : 16.3, 'Sep' : 17.8, 'Oct' : 21.1, 'Nov' : 24.1, 'Dic' : 27.3},
	'Temperatura mínima (°C)' : {
            'Ene' : 17.5, 'Feb' : 16.9, 'Mar' : 15.4, 'Abr' : 11.6, 'May' : 8.4, 'Jun' : 5.9, 'Jul' : 5.1, 'Ago' : 6.3, 'Sep' : 7.7, 'Oct' : 10.7, 'Nov' : 13.4, 'Dic' : 15.8},
	'Humedad relativa (%)' : {
            'Ene' : 73.6, 'Feb' : 78.1, 'Mar' : 80.6, 'Abr' : 81.9, 'May' : 83.2, 'Jun' : 84.2, 'Jul' : 83.3, 'Ago' : 81.1, 'Sep' : 79.2, 'Oct' : 79.1, 'Nov' : 76.4, 'Dic' : 72.9},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 13.6, 'Feb' : 13.5, 'Mar' : 12.3, 'Abr' : 10.5, 'May' : 10.6, 'Jun' : 10.6, 'Jul' : 11.3, 'Ago' : 12.6, 'Sep' : 14.4, 'Oct' : 13.8, 'Nov' : 13.9, 'Dic' : 14.2},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.2, 'Feb' : 3.2, 'Mar' : 3.2, 'Abr' : 3.4, 'May' : 3.8, 'Jun' : 4.2, 'Jul' : 4.1, 'Ago' : 3.9, 'Sep' : 3.8, 'Oct' : 3.8, 'Nov' : 3.5, 'Dic' : 3.3},
	'Precipitación (mm)' : {
            'Ene' : 108.8, 'Feb' : 114.3, 'Mar' : 124.5, 'Abr' : 86.8, 'May' : 79.3, 'Jun' : 52.6, 'Jul' : 61.4, 'Ago' : 61.3, 'Sep' : 69.8, 'Oct' : 110.6, 'Nov' : 103.9, 'Dic' : 95.2},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.1, 'Feb' : 7.2, 'Mar' : 8.0, 'Abr' : 7.4, 'May' : 6.0, 'Jun' : 6.2, 'Jul' : 6.3, 'Ago' : 6.4, 'Sep' : 6.9, 'Oct' : 8.8, 'Nov' : 8.4, 'Dic' : 7.6},
},
{
	'Estación' : 'PUNTA INDIO B.A.', 
	'Temperatura (°C)' : {
            'Ene' : 22.8, 'Feb' : 22.0, 'Mar' : 20.4, 'Abr' : 16.5, 'May' : 12.9, 'Jun' : 10.0, 'Jul' : 9.0, 'Ago' : 10.7, 'Sep' : 12.5, 'Oct' : 15.7, 'Nov' : 18.5, 'Dic' : 21.2},
	'Temperatura máxima (°C)' : {
            'Ene' : 28.0, 'Feb' : 26.8, 'Mar' : 25.2, 'Abr' : 21.4, 'May' : 17.9, 'Jun' : 14.6, 'Jul' : 13.8, 'Ago' : 15.7, 'Sep' : 17.2, 'Oct' : 20.6, 'Nov' : 23.3, 'Dic' : 26.3},
	'Temperatura mínima (°C)' : {
            'Ene' : 18.3, 'Feb' : 17.6, 'Mar' : 16.2, 'Abr' : 12.3, 'May' : 9.0, 'Jun' : 6.2, 'Jul' : 5.4, 'Ago' : 6.7, 'Sep' : 8.2, 'Oct' : 11.3, 'Nov' : 14.0, 'Dic' : 16.7},
	'Humedad relativa (%)' : {
            'Ene' : 76.7, 'Feb' : 79.7, 'Mar' : 81.5, 'Abr' : 83.7, 'May' : 85.2, 'Jun' : 86.2, 'Jul' : 86.0, 'Ago' : 84.4, 'Sep' : 82.1, 'Oct' : 80.9, 'Nov' : 78.9, 'Dic' : 76.1},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 18.8, 'Feb' : 17.9, 'Mar' : 16.2, 'Abr' : 14.0, 'May' : 14.3, 'Jun' : 13.8, 'Jul' : 14.4, 'Ago' : 16.3, 'Sep' : 18.5, 'Oct' : 18.1, 'Nov' : 18.3, 'Dic' : 19.2},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.7, 'Feb' : 3.6, 'Mar' : 3.5, 'Abr' : 3.6, 'May' : 4.1, 'Jun' : 4.4, 'Jul' : 4.3, 'Ago' : 4.2, 'Sep' : 4.1, 'Oct' : 4.1, 'Nov' : 4.0, 'Dic' : 3.8},
	'Precipitación (mm)' : {
            'Ene' : 84.1, 'Feb' : 112.6, 'Mar' : 109.2, 'Abr' : 95.2, 'May' : 68.5, 'Jun' : 64.7, 'Jul' : 64.7, 'Ago' : 71.1, 'Sep' : 73.3, 'Oct' : 100.2, 'Nov' : 107.9, 'Dic' : 78.7},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 6.2, 'Feb' : 7.3, 'Mar' : 7.4, 'Abr' : 7.3, 'May' : 6.0, 'Jun' : 5.3, 'Jul' : 6.4, 'Ago' : 6.5, 'Sep' : 6.3, 'Oct' : 8.4, 'Nov' : 7.4, 'Dic' : 6.6},
},
{
	'Estación' : 'SANTA ROSA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 23.6, 'Feb' : 22.1, 'Mar' : 19.5, 'Abr' : 14.9, 'May' : 11.0, 'Jun' : 7.9, 'Jul' : 7.2, 'Ago' : 9.5, 'Sep' : 12.1, 'Oct' : 15.9, 'Nov' : 19.4, 'Dic' : 22.5},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.0, 'Feb' : 29.8, 'Mar' : 26.9, 'Abr' : 22.4, 'May' : 18.0, 'Jun' : 14.7, 'Jul' : 14.2, 'Ago' : 17.2, 'Sep' : 19.7, 'Oct' : 23.1, 'Nov' : 26.7, 'Dic' : 29.8},
	'Temperatura mínima (°C)' : {
            'Ene' : 16.4, 'Feb' : 15.1, 'Mar' : 13.4, 'Abr' : 9.2, 'May' : 5.7, 'Jun' : 3.0, 'Jul' : 2.0, 'Ago' : 3.4, 'Sep' : 5.7, 'Oct' : 9.2, 'Nov' : 12.2, 'Dic' : 15.1},
	'Humedad relativa (%)' : {
            'Ene' : 58.6, 'Feb' : 62.6, 'Mar' : 69.6, 'Abr' : 72.1, 'May' : 75.4, 'Jun' : 75.9, 'Jul' : 72.7, 'Ago' : 64.8, 'Sep' : 63.0, 'Oct' : 62.1, 'Nov' : 57.6, 'Dic' : 55.4},
	'Velocidad del Viento (km/h)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.4, 'Feb' : 3.1, 'Mar' : 3.4, 'Abr' : 3.6, 'May' : 4.2, 'Jun' : 4.6, 'Jul' : 4.3, 'Ago' : 4.0, 'Sep' : 4.0, 'Oct' : 3.9, 'Nov' : 3.6, 'Dic' : 3.4},
	'Precipitación (mm)' : {
            'Ene' : 94.6, 'Feb' : 81.0, 'Mar' : 102.3, 'Abr' : 58.0, 'May' : 32.9, 'Jun' : 15.5, 'Jul' : 21.5, 'Ago' : 28.1, 'Sep' : 50.9, 'Oct' : 74.7, 'Nov' : 81.7, 'Dic' : 104.3},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 9.1, 'Feb' : 6.8, 'Mar' : 8.0, 'Abr' : 6.0, 'May' : 5.1, 'Jun' : 4.3, 'Jul' : 4.3, 'Ago' : 3.7, 'Sep' : 5.7, 'Oct' : 8.5, 'Nov' : 7.8, 'Dic' : 8.4},
},
{
	'Estación' : 'CORONEL SUÁREZ AERO', 
	'Temperatura (°C)' : {
            'Ene' : 21.0, 'Feb' : 19.8, 'Mar' : 17.5, 'Abr' : 13.3, 'May' : 9.5, 'Jun' : 6.6, 'Jul' : 5.9, 'Ago' : 7.9, 'Sep' : 10.3, 'Oct' : 13.5, 'Nov' : 16.6, 'Dic' : 20.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 28.7, 'Feb' : 27.4, 'Mar' : 24.8, 'Abr' : 20.4, 'May' : 16.1, 'Jun' : 12.7, 'Jul' : 12.3, 'Ago' : 14.9, 'Sep' : 17.1, 'Oct' : 20.3, 'Nov' : 23.9, 'Dic' : 27.4},
	'Temperatura mínima (°C)' : {
            'Ene' : 13.8, 'Feb' : 12.7, 'Mar' : 11.1, 'Abr' : 7.0, 'May' : 3.8, 'Jun' : 1.3, 'Jul' : 0.4, 'Ago' : 1.4, 'Sep' : 3.4, 'Oct' : 6.6, 'Nov' : 9.3, 'Dic' : 12.0},
	'Humedad relativa (%)' : {
            'Ene' : 64.7, 'Feb' : 69.4, 'Mar' : 74.4, 'Abr' : 76.7, 'May' : 79.7, 'Jun' : 81.1, 'Jul' : 79.1, 'Ago' : 72.8, 'Sep' : 71.3, 'Oct' : 71.7, 'Nov' : 66.9, 'Dic' : 62.1},
	'Velocidad del Viento (km/h)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.9, 'Feb' : 3.5, 'Mar' : 3.7, 'Abr' : 3.7, 'May' : 4.2, 'Jun' : 4.6, 'Jul' : 4.3, 'Ago' : 4.2, 'Sep' : 4.1, 'Oct' : 4.1, 'Nov' : 3.9, 'Dic' : 3.9},
	'Precipitación (mm)' : {
            'Ene' : 112.3, 'Feb' : 80.4, 'Mar' : 95.9, 'Abr' : 70.9, 'May' : 47.4, 'Jun' : 22.1, 'Jul' : 28.5, 'Ago' : 32.4, 'Sep' : 58.1, 'Oct' : 99.7, 'Nov' : 74.3, 'Dic' : 84.1},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 9.2, 'Feb' : 6.6, 'Mar' : 8.9, 'Abr' : 7.2, 'May' : 6.1, 'Jun' : 5.0, 'Jul' : 5.3, 'Ago' : 5.0, 'Sep' : 6.8, 'Oct' : 9.7, 'Nov' : 8.8, 'Dic' : 8.9},
},
{
	'Estación' : 'TANDIL AERO', 
	'Temperatura (°C)' : {
            'Ene' : 20.8, 'Feb' : 19.7, 'Mar' : 17.6, 'Abr' : 13.5, 'May' : 10.0, 'Jun' : 7.2, 'Jul' : 6.3, 'Ago' : 8.1, 'Sep' : 10.1, 'Oct' : 13.5, 'Nov' : 16.4, 'Dic' : 19.3},
	'Temperatura máxima (°C)' : {
            'Ene' : 28.1, 'Feb' : 26.8, 'Mar' : 24.3, 'Abr' : 20.3, 'May' : 16.4, 'Jun' : 13.0, 'Jul' : 12.4, 'Ago' : 14.7, 'Sep' : 16.6, 'Oct' : 19.8, 'Nov' : 23.0, 'Dic' : 26.4},
	'Temperatura mínima (°C)' : {
            'Ene' : 13.6, 'Feb' : 13.0, 'Mar' : 11.5, 'Abr' : 7.6, 'May' : 4.8, 'Jun' : 2.3, 'Jul' : 1.4, 'Ago' : 2.6, 'Sep' : 4.1, 'Oct' : 7.2, 'Nov' : 9.7, 'Dic' : 11.9},
	'Humedad relativa (%)' : {
            'Ene' : 68.3, 'Feb' : 73.0, 'Mar' : 76.9, 'Abr' : 78.1, 'May' : 80.7, 'Jun' : 81.0, 'Jul' : 80.7, 'Ago' : 76.2, 'Sep' : 74.6, 'Oct' : 73.5, 'Nov' : 70.7, 'Dic' : 66.5},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 13.8, 'Feb' : 12.7, 'Mar' : 12.0, 'Abr' : 11.1, 'May' : 11.4, 'Jun' : 12.1, 'Jul' : 12.5, 'Ago' : 14.0, 'Sep' : 15.4, 'Oct' : 15.5, 'Nov' : 14.9, 'Dic' : 14.4},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.5, 'Feb' : 3.4, 'Mar' : 3.6, 'Abr' : 3.6, 'May' : 4.1, 'Jun' : 4.5, 'Jul' : 4.4, 'Ago' : 4.2, 'Sep' : 4.2, 'Oct' : 4.1, 'Nov' : 3.9, 'Dic' : 3.5},
	'Precipitación (mm)' : {
            'Ene' : 108.5, 'Feb' : 90.2, 'Mar' : 98.8, 'Abr' : 71.3, 'May' : 59.7, 'Jun' : 37.2, 'Jul' : 37.6, 'Ago' : 45.2, 'Sep' : 58.6, 'Oct' : 97.7, 'Nov' : 94.6, 'Dic' : 79.2},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.7, 'Feb' : 6.9, 'Mar' : 8.3, 'Abr' : 6.7, 'May' : 5.9, 'Jun' : 5.5, 'Jul' : 6.1, 'Ago' : 5.5, 'Sep' : 6.8, 'Oct' : 9.2, 'Nov' : 8.5, 'Dic' : 7.4},
},
{
	'Estación' : 'DOLORES AERO', 
	'Temperatura (°C)' : {
            'Ene' : 21.8, 'Feb' : 20.8, 'Mar' : 19.0, 'Abr' : 15.1, 'May' : 11.6, 'Jun' : 8.7, 'Jul' : 7.8, 'Ago' : 9.8, 'Sep' : 11.7, 'Oct' : 14.9, 'Nov' : 17.6, 'Dic' : 20.3},
	'Temperatura máxima (°C)' : {
            'Ene' : 28.6, 'Feb' : 27.4, 'Mar' : 25.6, 'Abr' : 21.6, 'May' : 17.9, 'Jun' : 14.3, 'Jul' : 13.6, 'Ago' : 15.9, 'Sep' : 17.5, 'Oct' : 21.0, 'Nov' : 23.8, 'Dic' : 27.0},
	'Temperatura mínima (°C)' : {
            'Ene' : None, 'Feb' : 14.7, 'Mar' : 13.3, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Humedad relativa (%)' : {
            'Ene' : 73.5, 'Feb' : 77.2, 'Mar' : 79.8, 'Abr' : 81.5, 'May' : 83.4, 'Jun' : 84.9, 'Jul' : 84.0, 'Ago' : 81.3, 'Sep' : 79.7, 'Oct' : 77.6, 'Nov' : 75.3, 'Dic' : 72.0},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 10.0, 'Feb' : 8.4, 'Mar' : 7.6, 'Abr' : 7.9, 'May' : 7.7, 'Jun' : 8.2, 'Jul' : 9.9, 'Ago' : 10.2, 'Sep' : 11.2, 'Oct' : 11.4, 'Nov' : 12.0, 'Dic' : 10.8},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.6, 'Feb' : 3.3, 'Mar' : 3.4, 'Abr' : 3.5, 'May' : 3.9, 'Jun' : 4.3, 'Jul' : 4.2, 'Ago' : 4.0, 'Sep' : 4.0, 'Oct' : 4.0, 'Nov' : 3.8, 'Dic' : 3.6},
	'Precipitación (mm)' : {
            'Ene' : 108.4, 'Feb' : 99.8, 'Mar' : 90.4, 'Abr' : 97.4, 'May' : 58.7, 'Jun' : 59.9, 'Jul' : 59.6, 'Ago' : 59.0, 'Sep' : None, 'Oct' : 102.1, 'Nov' : 108.7, 'Dic' : 83.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.3, 'Feb' : 8.1, 'Mar' : 8.4, 'Abr' : 7.9, 'May' : 7.2, 'Jun' : 7.4, 'Jul' : 7.2, 'Ago' : 6.7, 'Sep' : None, 'Oct' : 9.7, 'Nov' : 9.4, 'Dic' : 8.3},
},
{
	'Estación' : 'PIGÜÉ AERO', 
	'Temperatura (°C)' : {
            'Ene' : 21.1, 'Feb' : 20.0, 'Mar' : 17.6, 'Abr' : 13.4, 'May' : 9.7, 'Jun' : 6.8, 'Jul' : 6.1, 'Ago' : 8.2, 'Sep' : 10.2, 'Oct' : 13.5, 'Nov' : 16.7, 'Dic' : 20.1},
	'Temperatura máxima (°C)' : {
            'Ene' : 28.8, 'Feb' : 27.4, 'Mar' : 24.5, 'Abr' : 19.8, 'May' : 15.6, 'Jun' : 12.2, 'Jul' : 11.6, 'Ago' : 14.4, 'Sep' : 16.7, 'Oct' : 20.0, 'Nov' : 23.7, 'Dic' : 27.5},
	'Temperatura mínima (°C)' : {
            'Ene' : 14.3, 'Feb' : 13.3, 'Mar' : 11.7, 'Abr' : 7.7, 'May' : 4.6, 'Jun' : 2.1, 'Jul' : 1.2, 'Ago' : 2.5, 'Sep' : 4.1, 'Oct' : 7.3, 'Nov' : 9.9, 'Dic' : 12.8},
	'Humedad relativa (%)' : {
            'Ene' : 61.0, 'Feb' : 65.6, 'Mar' : 70.9, 'Abr' : 73.8, 'May' : 77.3, 'Jun' : 78.7, 'Jul' : 76.5, 'Ago' : 69.2, 'Sep' : 69.0, 'Oct' : 68.0, 'Nov' : 63.8, 'Dic' : 58.5},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 11.9, 'Feb' : 10.8, 'Mar' : 10.2, 'Abr' : 9.1, 'May' : 8.8, 'Jun' : 9.4, 'Jul' : 10.9, 'Ago' : 12.0, 'Sep' : 12.8, 'Oct' : 12.4, 'Nov' : 12.9, 'Dic' : 12.5},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.8, 'Feb' : 3.6, 'Mar' : 3.8, 'Abr' : 3.9, 'May' : 4.5, 'Jun' : 5.0, 'Jul' : 4.6, 'Ago' : 4.5, 'Sep' : 4.3, 'Oct' : 4.2, 'Nov' : 4.1, 'Dic' : 3.9},
	'Precipitación (mm)' : {
            'Ene' : None, 'Feb' : 101.6, 'Mar' : 92.8, 'Abr' : None, 'May' : None, 'Jun' : 22.5, 'Jul' : 26.2, 'Ago' : 34.8, 'Sep' : 63.2, 'Oct' : 95.5, 'Nov' : 87.1, 'Dic' : 88.3},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : None, 'Feb' : 7.4, 'Mar' : 8.4, 'Abr' : None, 'May' : None, 'Jun' : 6.3, 'Jul' : 6.5, 'Ago' : 5.9, 'Sep' : 7.2, 'Oct' : 9.7, 'Nov' : 8.9, 'Dic' : 8.9},
},
{
	'Estación' : 'TRES ARROYOS', 
	'Temperatura (°C)' : {
            'Ene' : 21.5, 'Feb' : 20.4, 'Mar' : 18.1, 'Abr' : 14.1, 'May' : 10.6, 'Jun' : 7.8, 'Jul' : 7.1, 'Ago' : 8.8, 'Sep' : 10.6, 'Oct' : 13.8, 'Nov' : 16.9, 'Dic' : 20.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 29.3, 'Feb' : 27.7, 'Mar' : 25.1, 'Abr' : 20.6, 'May' : 16.4, 'Jun' : 13.1, 'Jul' : 12.5, 'Ago' : 14.9, 'Sep' : 17.0, 'Oct' : 20.2, 'Nov' : 23.8, 'Dic' : 27.4},
	'Temperatura mínima (°C)' : {
            'Ene' : 15.1, 'Feb' : 14.5, 'Mar' : 12.9, 'Abr' : 9.2, 'May' : 6.3, 'Jun' : 3.8, 'Jul' : 3.0, 'Ago' : 4.0, 'Sep' : 5.4, 'Oct' : 8.2, 'Nov' : 10.8, 'Dic' : 13.3},
	'Humedad relativa (%)' : {
            'Ene' : 60.0, 'Feb' : 66.5, 'Mar' : 70.6, 'Abr' : 73.0, 'May' : 76.7, 'Jun' : 77.0, 'Jul' : 76.1, 'Ago' : 70.6, 'Sep' : 70.1, 'Oct' : 68.9, 'Nov' : 64.3, 'Dic' : 59.3},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 14.9, 'Feb' : 13.4, 'Mar' : 12.7, 'Abr' : 12.9, 'May' : 12.1, 'Jun' : 13.0, 'Jul' : 13.1, 'Ago' : 13.7, 'Sep' : 13.8, 'Oct' : 15.1, 'Nov' : 15.4, 'Dic' : 16.4},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.7, 'Feb' : 3.6, 'Mar' : 3.8, 'Abr' : 3.9, 'May' : 4.6, 'Jun' : 4.9, 'Jul' : 4.8, 'Ago' : 4.6, 'Sep' : 4.6, 'Oct' : 4.3, 'Nov' : 4.1, 'Dic' : 3.7},
	'Precipitación (mm)' : {
            'Ene' : 85.1, 'Feb' : 99.5, 'Mar' : 83.5, 'Abr' : 74.5, 'May' : 59.3, 'Jun' : 34.5, 'Jul' : 43.2, 'Ago' : 42.3, 'Sep' : 63.1, 'Oct' : 82.5, 'Nov' : 88.3, 'Dic' : 80.0},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 9.2, 'Feb' : 8.2, 'Mar' : 9.5, 'Abr' : 9.3, 'May' : 8.3, 'Jun' : 7.3, 'Jul' : 9.0, 'Ago' : 7.7, 'Sep' : 8.8, 'Oct' : 10.8, 'Nov' : 9.5, 'Dic' : 9.1},
},
{
	'Estación' : 'MAR DEL PLATA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 20.4, 'Feb' : 19.8, 'Mar' : 18.2, 'Abr' : 14.5, 'May' : 11.2, 'Jun' : 8.4, 'Jul' : 7.5, 'Ago' : 8.8, 'Sep' : 10.4, 'Oct' : 13.3, 'Nov' : 15.9, 'Dic' : 18.5},
	'Temperatura máxima (°C)' : {
            'Ene' : 26.5, 'Feb' : 25.6, 'Mar' : 23.9, 'Abr' : 20.4, 'May' : 16.8, 'Jun' : 13.6, 'Jul' : 12.7, 'Ago' : 14.5, 'Sep' : 15.9, 'Oct' : 18.9, 'Nov' : 21.7, 'Dic' : 24.5},
	'Temperatura mínima (°C)' : {
            'Ene' : 14.6, 'Feb' : 14.3, 'Mar' : 13.0, 'Abr' : 9.2, 'May' : 6.3, 'Jun' : 3.8, 'Jul' : 3.1, 'Ago' : 4.1, 'Sep' : 5.3, 'Oct' : 7.8, 'Nov' : 10.2, 'Dic' : 12.6},
	'Humedad relativa (%)' : {
            'Ene' : 74.4, 'Feb' : 76.9, 'Mar' : 79.3, 'Abr' : 80.5, 'May' : 82.4, 'Jun' : 82.7, 'Jul' : 82.5, 'Ago' : 80.8, 'Sep' : 79.6, 'Oct' : 78.4, 'Nov' : 76.5, 'Dic' : 74.6},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 16.0, 'Feb' : 14.8, 'Mar' : 13.7, 'Abr' : 12.3, 'May' : 12.2, 'Jun' : 12.8, 'Jul' : 12.6, 'Ago' : 13.6, 'Sep' : 14.0, 'Oct' : 15.4, 'Nov' : 15.8, 'Dic' : 16.2},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.7, 'Feb' : 3.7, 'Mar' : 3.8, 'Abr' : 4.0, 'May' : 4.3, 'Jun' : 4.7, 'Jul' : 4.6, 'Ago' : 4.5, 'Sep' : 4.5, 'Oct' : 4.2, 'Nov' : 4.1, 'Dic' : 3.8},
	'Precipitación (mm)' : {
            'Ene' : 94.9, 'Feb' : 93.9, 'Mar' : 95.7, 'Abr' : 85.5, 'May' : 66.4, 'Jun' : 57.4, 'Jul' : 55.7, 'Ago' : 55.9, 'Sep' : 57.3, 'Oct' : 89.3, 'Nov' : 81.3, 'Dic' : 92.8},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 8.3, 'Feb' : 7.9, 'Mar' : 9.0, 'Abr' : 9.1, 'May' : 8.6, 'Jun' : 8.5, 'Jul' : 8.8, 'Ago' : 7.9, 'Sep' : 7.9, 'Oct' : 9.8, 'Nov' : 9.6, 'Dic' : 8.8},
},
{
	'Estación' : 'NEUQUÉN AERO', 
	'Temperatura (°C)' : {
            'Ene' : 23.7, 'Feb' : 22.3, 'Mar' : 18.9, 'Abr' : 13.4, 'May' : 9.2, 'Jun' : 6.6, 'Jul' : 5.8, 'Ago' : 8.1, 'Sep' : 11.4, 'Oct' : 15.6, 'Nov' : 19.4, 'Dic' : 22.4},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.9, 'Feb' : 30.6, 'Mar' : 27.0, 'Abr' : 21.6, 'May' : 16.5, 'Jun' : 12.9, 'Jul' : 12.9, 'Ago' : 15.9, 'Sep' : 18.9, 'Oct' : 23.2, 'Nov' : 27.1, 'Dic' : 30.2},
	'Temperatura mínima (°C)' : {
            'Ene' : 15.5, 'Feb' : 14.2, 'Mar' : 11.6, 'Abr' : 6.8, 'May' : 3.5, 'Jun' : 1.5, 'Jul' : 0.2, 'Ago' : 1.6, 'Sep' : 4.4, 'Oct' : 8.2, 'Nov' : 11.6, 'Dic' : 14.5},
	'Humedad relativa (%)' : {
            'Ene' : 36.7, 'Feb' : 44.0, 'Mar' : 53.4, 'Abr' : 62.2, 'May' : 67.7, 'Jun' : 71.7, 'Jul' : 68.5, 'Ago' : 58.7, 'Sep' : 51.1, 'Oct' : 44.3, 'Nov' : 38.3, 'Dic' : 36.1},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 12.8, 'Feb' : 11.3, 'Mar' : 9.9, 'Abr' : 8.8, 'May' : 8.3, 'Jun' : 9.3, 'Jul' : 9.5, 'Ago' : 9.7, 'Sep' : 10.3, 'Oct' : 12.8, 'Nov' : 13.9, 'Dic' : 13.8},
	'Nubosidad total (octavos)' : {
            'Ene' : 2.6, 'Feb' : 2.6, 'Mar' : 3.1, 'Abr' : 3.5, 'May' : 4.3, 'Jun' : 4.8, 'Jul' : 4.4, 'Ago' : 4.3, 'Sep' : 4.0, 'Oct' : 3.8, 'Nov' : 3.4, 'Dic' : 3.1},
	'Precipitación (mm)' : {
            'Ene' : 12.9, 'Feb' : 11.9, 'Mar' : 23.6, 'Abr' : 15.3, 'May' : 21.1, 'Jun' : 23.5, 'Jul' : 15.9, 'Ago' : 11.4, 'Sep' : 19.3, 'Oct' : 20.3, 'Nov' : 14.5, 'Dic' : 11.2},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 2.7, 'Feb' : 2.6, 'Mar' : 3.5, 'Abr' : 4.9, 'May' : 5.5, 'Jun' : 7.1, 'Jul' : 4.9, 'Ago' : 3.9, 'Sep' : 4.6, 'Oct' : 4.1, 'Nov' : 2.9, 'Dic' : 3.0},
},
{
	'Estación' : 'BAHÍA BLANCA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 23.6, 'Feb' : 22.1, 'Mar' : 19.4, 'Abr' : 14.9, 'May' : 11.1, 'Jun' : 8.1, 'Jul' : 7.5, 'Ago' : 9.4, 'Sep' : 11.6, 'Oct' : 15.1, 'Nov' : 18.7, 'Dic' : 22.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 31.1, 'Feb' : 29.6, 'Mar' : 26.6, 'Abr' : 21.8, 'May' : 17.5, 'Jun' : 14.1, 'Jul' : 13.7, 'Ago' : 16.3, 'Sep' : 18.5, 'Oct' : 22.2, 'Nov' : 25.9, 'Dic' : 29.3},
	'Temperatura mínima (°C)' : {
            'Ene' : 16.3, 'Feb' : 15.2, 'Mar' : 13.4, 'Abr' : 9.2, 'May' : 6.0, 'Jun' : 3.3, 'Jul' : 2.4, 'Ago' : 3.9, 'Sep' : 5.6, 'Oct' : 8.5, 'Nov' : 11.4, 'Dic' : 14.4},
	'Humedad relativa (%)' : {
            'Ene' : 54.1, 'Feb' : 60.5, 'Mar' : 66.5, 'Abr' : 70.5, 'May' : 74.5, 'Jun' : 75.1, 'Jul' : 73.8, 'Ago' : 68.9, 'Sep' : 67.2, 'Oct' : 64.8, 'Nov' : 58.5, 'Dic' : 53.3},
	'Velocidad del Viento (km/h)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.3, 'Feb' : 3.0, 'Mar' : 3.3, 'Abr' : 3.5, 'May' : 4.0, 'Jun' : 4.3, 'Jul' : 4.1, 'Ago' : 4.1, 'Sep' : 4.0, 'Oct' : 3.9, 'Nov' : 3.6, 'Dic' : 3.4},
	'Precipitación (mm)' : {
            'Ene' : 67.1, 'Feb' : 67.1, 'Mar' : 75.2, 'Abr' : 54.5, 'May' : 41.2, 'Jun' : 31.5, 'Jul' : 31.1, 'Ago' : 34.5, 'Sep' : 51.6, 'Oct' : 73.3, 'Nov' : 56.8, 'Dic' : 67.3},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 7.6, 'Feb' : 6.4, 'Mar' : 8.1, 'Abr' : 7.0, 'May' : 5.5, 'Jun' : 5.9, 'Jul' : 5.9, 'Ago' : 5.1, 'Sep' : 6.7, 'Oct' : 8.9, 'Nov' : 7.0, 'Dic' : 7.0},
},
{
	'Estación' : 'BARILOCHE AERO', 
	'Temperatura (°C)' : {
            'Ene' : 15.0, 'Feb' : 14.8, 'Mar' : 11.9, 'Abr' : 7.9, 'May' : 4.9, 'Jun' : 2.9, 'Jul' : 2.1, 'Ago' : 3.0, 'Sep' : 5.1, 'Oct' : 8.0, 'Nov' : 10.8, 'Dic' : 13.5},
	'Temperatura máxima (°C)' : {
            'Ene' : 22.6, 'Feb' : 23.0, 'Mar' : 19.7, 'Abr' : 14.6, 'May' : 10.2, 'Jun' : 6.9, 'Jul' : 6.7, 'Ago' : 8.3, 'Sep' : 11.5, 'Oct' : 14.8, 'Nov' : 17.9, 'Dic' : 20.5},
	'Temperatura mínima (°C)' : {
            'Ene' : 6.6, 'Feb' : 6.3, 'Mar' : 4.7, 'Abr' : 2.3, 'May' : 0.6, 'Jun' : -0.6, 'Jul' : -1.6, 'Ago' : -1.1, 'Sep' : -0.2, 'Oct' : 1.8, 'Nov' : 3.7, 'Dic' : 5.9},
	'Humedad relativa (%)' : {
            'Ene' : 54.1, 'Feb' : 54.8, 'Mar' : 62.4, 'Abr' : 69.8, 'May' : 76.4, 'Jun' : 80.2, 'Jul' : 78.9, 'Ago' : 75.9, 'Sep' : 68.2, 'Oct' : 62.5, 'Nov' : 57.7, 'Dic' : 54.9},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 22.9, 'Feb' : 19.8, 'Mar' : 18.3, 'Abr' : 19.1, 'May' : 15.9, 'Jun' : 17.9, 'Jul' : 16.6, 'Ago' : 16.8, 'Sep' : 17.1, 'Oct' : 23.4, 'Nov' : 25.4, 'Dic' : 25.2},
	'Nubosidad total (octavos)' : {
            'Ene' : 2.9, 'Feb' : 2.7, 'Mar' : 3.4, 'Abr' : 4.0, 'May' : 4.9, 'Jun' : 5.5, 'Jul' : 5.0, 'Ago' : 4.8, 'Sep' : 4.2, 'Oct' : 4.0, 'Nov' : 3.6, 'Dic' : 3.3},
	'Precipitación (mm)' : {
            'Ene' : 20.0, 'Feb' : 15.3, 'Mar' : 35.2, 'Abr' : 58.9, 'May' : 130.1, 'Jun' : 170.1, 'Jul' : 122.1, 'Ago' : 101.4, 'Sep' : 56.5, 'Oct' : 49.4, 'Nov' : 29.3, 'Dic' : 23.4},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 3.7, 'Feb' : 3.4, 'Mar' : 6.7, 'Abr' : 8.2, 'May' : 13.6, 'Jun' : 16.1, 'Jul' : 14.0, 'Ago' : 13.0, 'Sep' : 9.1, 'Oct' : 8.3, 'Nov' : 5.4, 'Dic' : 4.6},
},
{
	'Estación' : 'MAQUINCHAO', 
	'Temperatura (°C)' : {
            'Ene' : 18.0, 'Feb' : 17.5, 'Mar' : 14.1, 'Abr' : 8.9, 'May' : 4.4, 'Jun' : 1.4, 'Jul' : 0.5, 'Ago' : 2.7, 'Sep' : 5.7, 'Oct' : 9.8, 'Nov' : 13.5, 'Dic' : 16.6},
	'Temperatura máxima (°C)' : {
            'Ene' : 26.4, 'Feb' : 25.7, 'Mar' : 21.9, 'Abr' : 16.3, 'May' : 10.9, 'Jun' : 6.6, 'Jul' : 6.2, 'Ago' : 9.2, 'Sep' : 12.9, 'Oct' : 16.9, 'Nov' : 20.9, 'Dic' : 24.2},
	'Temperatura mínima (°C)' : {
            'Ene' : 9.3, 'Feb' : 9.1, 'Mar' : 6.6, 'Abr' : 2.3, 'May' : -0.6, 'Jun' : -2.9, 'Jul' : -4.6, 'Ago' : -3.1, 'Sep' : -1.1, 'Oct' : 2.3, 'Nov' : 5.4, 'Dic' : 7.9},
	'Humedad relativa (%)' : {
            'Ene' : 42.8, 'Feb' : 46.9, 'Mar' : 52.7, 'Abr' : 59.6, 'May' : 67.1, 'Jun' : 72.0, 'Jul' : 69.5, 'Ago' : 64.5, 'Sep' : 58.1, 'Oct' : 52.3, 'Nov' : 47.6, 'Dic' : 44.8},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 11.6, 'Feb' : 9.1, 'Mar' : 8.4, 'Abr' : 8.0, 'May' : 6.1, 'Jun' : 7.5, 'Jul' : 6.9, 'Ago' : 8.3, 'Sep' : 8.3, 'Oct' : 12.6, 'Nov' : 13.7, 'Dic' : 12.7},
	'Nubosidad total (octavos)' : {
            'Ene' : 2.8, 'Feb' : 2.7, 'Mar' : 3.3, 'Abr' : 3.5, 'May' : 4.0, 'Jun' : 4.4, 'Jul' : 3.9, 'Ago' : 3.9, 'Sep' : 3.7, 'Oct' : 3.7, 'Nov' : 3.5, 'Dic' : 3.2},
	'Precipitación (mm)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : 26.2, 'Abr' : 20.7, 'May' : 23.3, 'Jun' : 28.1, 'Jul' : None, 'Ago' : 11.5, 'Sep' : 14.9, 'Oct' : 18.6, 'Nov' : None, 'Dic' : None},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : None, 'Feb' : None, 'Mar' : 3.2, 'Abr' : 3.6, 'May' : 5.1, 'Jun' : 6.9, 'Jul' : None, 'Ago' : 3.4, 'Sep' : 3.5, 'Oct' : 3.2, 'Nov' : None, 'Dic' : None},
},
{
	'Estación' : 'VIEDMA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 22.1, 'Feb' : 20.8, 'Mar' : 18.3, 'Abr' : 13.8, 'May' : 9.9, 'Jun' : 7.2, 'Jul' : 6.6, 'Ago' : 8.2, 'Sep' : 10.5, 'Oct' : 14.3, 'Nov' : 17.7, 'Dic' : 20.6},
	'Temperatura máxima (°C)' : {
            'Ene' : 29.4, 'Feb' : 28.3, 'Mar' : 25.3, 'Abr' : 20.9, 'May' : 16.3, 'Jun' : 13.1, 'Jul' : 12.8, 'Ago' : 15.1, 'Sep' : 17.5, 'Oct' : 21.4, 'Nov' : 25.0, 'Dic' : 27.9},
	'Temperatura mínima (°C)' : {
            'Ene' : 14.7, 'Feb' : 14.1, 'Mar' : 12.0, 'Abr' : 7.8, 'May' : 4.7, 'Jun' : 2.4, 'Jul' : 1.5, 'Ago' : 2.3, 'Sep' : 4.0, 'Oct' : 7.1, 'Nov' : 10.1, 'Dic' : 12.9},
	'Humedad relativa (%)' : {
            'Ene' : 50.2, 'Feb' : 56.1, 'Mar' : 62.8, 'Abr' : 67.3, 'May' : 73.4, 'Jun' : 75.0, 'Jul' : 72.1, 'Ago' : 66.9, 'Sep' : 64.0, 'Oct' : 57.8, 'Nov' : 51.0, 'Dic' : 48.2},
	'Velocidad del Viento (km/h)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Nubosidad total (octavos)' : {
            'Ene' : 2.9, 'Feb' : 2.8, 'Mar' : 3.1, 'Abr' : 3.3, 'May' : 3.9, 'Jun' : 4.2, 'Jul' : 4.0, 'Ago' : 3.9, 'Sep' : 3.8, 'Oct' : 3.6, 'Nov' : 3.4, 'Dic' : 3.1},
	'Precipitación (mm)' : {
            'Ene' : 31.4, 'Feb' : 43.0, 'Mar' : 54.1, 'Abr' : 41.8, 'May' : 28.8, 'Jun' : 25.6, 'Jul' : 26.0, 'Ago' : 22.3, 'Sep' : 25.2, 'Oct' : 30.3, 'Nov' : 23.6, 'Dic' : 21.3},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 5.2, 'Feb' : 5.6, 'Mar' : 6.0, 'Abr' : 6.4, 'May' : 7.1, 'Jun' : 8.0, 'Jul' : 7.2, 'Ago' : 5.8, 'Sep' : 5.5, 'Oct' : 6.1, 'Nov' : 5.1, 'Dic' : 5.0},
},
{
	'Estación' : 'ESQUEL AERO', 
	'Temperatura (°C)' : {
            'Ene' : 15.1, 'Feb' : 15.0, 'Mar' : 12.3, 'Abr' : 8.2, 'May' : 4.9, 'Jun' : 2.4, 'Jul' : 1.5, 'Ago' : 3.2, 'Sep' : 5.5, 'Oct' : 8.4, 'Nov' : 11.2, 'Dic' : 13.6},
	'Temperatura máxima (°C)' : {
            'Ene' : 21.7, 'Feb' : 22.2, 'Mar' : 19.1, 'Abr' : 14.4, 'May' : 10.1, 'Jun' : 6.7, 'Jul' : 6.1, 'Ago' : 8.5, 'Sep' : 11.8, 'Oct' : 14.7, 'Nov' : 17.6, 'Dic' : 19.9},
	'Temperatura mínima (°C)' : {
            'Ene' : 8.2, 'Feb' : 7.7, 'Mar' : 5.5, 'Abr' : 2.7, 'May' : 0.5, 'Jun' : -1.8, 'Jul' : -2.8, 'Ago' : -1.4, 'Sep' : 0.0, 'Oct' : 2.3, 'Nov' : 4.7, 'Dic' : 7.0},
	'Humedad relativa (%)' : {
            'Ene' : 48.0, 'Feb' : 50.1, 'Mar' : 56.5, 'Abr' : 63.5, 'May' : 72.2, 'Jun' : 76.6, 'Jul' : 75.5, 'Ago' : 70.9, 'Sep' : 62.9, 'Oct' : 55.2, 'Nov' : 50.0, 'Dic' : 48.1},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 23.4, 'Feb' : 20.0, 'Mar' : 17.2, 'Abr' : 17.4, 'May' : 14.5, 'Jun' : 15.4, 'Jul' : 14.6, 'Ago' : 14.7, 'Sep' : 15.8, 'Oct' : 20.6, 'Nov' : 23.5, 'Dic' : 23.8},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.3, 'Feb' : 3.0, 'Mar' : 3.5, 'Abr' : 3.8, 'May' : 4.4, 'Jun' : 4.7, 'Jul' : 4.5, 'Ago' : 4.3, 'Sep' : 4.1, 'Oct' : 3.9, 'Nov' : 3.7, 'Dic' : 3.6},
	'Precipitación (mm)' : {
            'Ene' : 18.8, 'Feb' : 18.4, 'Mar' : 24.5, 'Abr' : 43.1, 'May' : 65.0, 'Jun' : 79.4, 'Jul' : 60.2, 'Ago' : 47.0, 'Sep' : 35.7, 'Oct' : 28.3, 'Nov' : 20.8, 'Dic' : 20.8},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 3.8, 'Feb' : 3.7, 'Mar' : 5.6, 'Abr' : 7.0, 'May' : 9.7, 'Jun' : 11.0, 'Jul' : 9.4, 'Ago' : 9.6, 'Sep' : 7.3, 'Oct' : 6.1, 'Nov' : 4.4, 'Dic' : 4.1},
},
{
	'Estación' : 'TRELEW AERO', 
	'Temperatura (°C)' : {
            'Ene' : 21.5, 'Feb' : 20.3, 'Mar' : 17.6, 'Abr' : 13.3, 'May' : 9.2, 'Jun' : 6.2, 'Jul' : 5.8, 'Ago' : 7.7, 'Sep' : 10.4, 'Oct' : 14.1, 'Nov' : 17.4, 'Dic' : 20.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 29.2, 'Feb' : 28.1, 'Mar' : 25.0, 'Abr' : 20.7, 'May' : 15.7, 'Jun' : 12.2, 'Jul' : 12.3, 'Ago' : 14.8, 'Sep' : 17.5, 'Oct' : 21.2, 'Nov' : 24.9, 'Dic' : 27.5},
	'Temperatura mínima (°C)' : {
            'Ene' : 13.6, 'Feb' : 12.6, 'Mar' : 10.5, 'Abr' : 6.7, 'May' : 3.4, 'Jun' : 0.8, 'Jul' : 0.2, 'Ago' : 1.4, 'Sep' : 3.6, 'Oct' : 6.5, 'Nov' : 9.5, 'Dic' : 11.9},
	'Humedad relativa (%)' : {
            'Ene' : 41.7, 'Feb' : 49.0, 'Mar' : 53.6, 'Abr' : 57.0, 'May' : 65.7, 'Jun' : 69.6, 'Jul' : 66.9, 'Ago' : 61.2, 'Sep' : 56.6, 'Oct' : 49.6, 'Nov' : 44.1, 'Dic' : 41.7},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 24.2, 'Feb' : 23.0, 'Mar' : 20.2, 'Abr' : 19.1, 'May' : 16.6, 'Jun' : 17.7, 'Jul' : 17.9, 'Ago' : 18.4, 'Sep' : 18.3, 'Oct' : 22.5, 'Nov' : 23.7, 'Dic' : 23.9},
	'Nubosidad total (octavos)' : {
            'Ene' : 3.6, 'Feb' : 3.5, 'Mar' : 3.7, 'Abr' : 3.8, 'May' : 4.3, 'Jun' : 4.3, 'Jul' : 4.2, 'Ago' : 4.2, 'Sep' : 4.2, 'Oct' : 4.2, 'Nov' : 3.9, 'Dic' : 3.9},
	'Precipitación (mm)' : {
            'Ene' : 13.6, 'Feb' : 18.9, 'Mar' : 23.3, 'Abr' : 24.8, 'May' : 26.3, 'Jun' : 22.2, 'Jul' : 17.8, 'Ago' : 13.9, 'Sep' : 14.6, 'Oct' : 19.2, 'Nov' : 13.7, 'Dic' : 13.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 3.8, 'Feb' : 4.1, 'Mar' : 5.4, 'Abr' : 4.6, 'May' : 7.1, 'Jun' : 8.0, 'Jul' : 6.0, 'Ago' : 6.3, 'Sep' : 6.1, 'Oct' : 6.0, 'Nov' : 4.7, 'Dic' : 3.9},
},
{
	'Estación' : 'COMODORO RIVADAVIA AERO', 
	'Temperatura (°C)' : {
            'Ene' : 19.7, 'Feb' : 18.8, 'Mar' : 16.3, 'Abr' : 13.1, 'May' : 9.6, 'Jun' : 6.9, 'Jul' : 6.6, 'Ago' : 7.9, 'Sep' : 10.1, 'Oct' : 13.0, 'Nov' : 15.9, 'Dic' : 18.2},
	'Temperatura máxima (°C)' : {
            'Ene' : 26.1, 'Feb' : 25.0, 'Mar' : 22.4, 'Abr' : 18.6, 'May' : 14.2, 'Jun' : 10.9, 'Jul' : 10.8, 'Ago' : 12.8, 'Sep' : 15.4, 'Oct' : 18.8, 'Nov' : 22.1, 'Dic' : 24.5},
	'Temperatura mínima (°C)' : {
            'Ene' : 13.6, 'Feb' : 12.9, 'Mar' : 10.9, 'Abr' : 8.3, 'May' : 5.5, 'Jun' : 3.1, 'Jul' : 2.7, 'Ago' : 3.6, 'Sep' : 5.1, 'Oct' : 7.5, 'Nov' : 10.0, 'Dic' : 12.1},
	'Humedad relativa (%)' : {
            'Ene' : 37.9, 'Feb' : 42.7, 'Mar' : 47.2, 'Abr' : 49.4, 'May' : 57.3, 'Jun' : 60.1, 'Jul' : 57.2, 'Ago' : 54.2, 'Sep' : 51.5, 'Oct' : 45.9, 'Nov' : 40.8, 'Dic' : 38.9},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 25.9, 'Feb' : 21.2, 'Mar' : 20.7, 'Abr' : 22.8, 'May' : 19.4, 'Jun' : 22.4, 'Jul' : 19.5, 'Ago' : 19.2, 'Sep' : 19.5, 'Oct' : 23.3, 'Nov' : 25.1, 'Dic' : 25.6},
	'Nubosidad total (octavos)' : {
            'Ene' : 4.3, 'Feb' : 4.1, 'Mar' : 4.1, 'Abr' : 4.2, 'May' : 4.5, 'Jun' : 4.5, 'Jul' : 4.5, 'Ago' : 4.4, 'Sep' : 4.5, 'Oct' : 4.6, 'Nov' : 4.5, 'Dic' : 4.5},
	'Precipitación (mm)' : {
            'Ene' : 11.6, 'Feb' : 14.4, 'Mar' : 18.2, 'Abr' : 25.4, 'May' : 37.4, 'Jun' : 35.9, 'Jul' : 23.4, 'Ago' : 20.1, 'Sep' : 20.1, 'Oct' : 16.4, 'Nov' : 14.5, 'Dic' : 10.1},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 2.9, 'Feb' : 3.5, 'Mar' : 4.7, 'Abr' : 5.0, 'May' : 6.9, 'Jun' : 6.7, 'Jul' : 5.8, 'Ago' : 6.1, 'Sep' : 6.3, 'Oct' : 5.4, 'Nov' : 4.6, 'Dic' : 3.9},
},
{
	'Estación' : 'SAN JULIÁN AERO', 
	'Temperatura (°C)' : {
            'Ene' : 16.3, 'Feb' : 15.6, 'Mar' : 13.2, 'Abr' : 9.8, 'May' : 6.2, 'Jun' : 3.4, 'Jul' : 3.2, 'Ago' : 4.8, 'Sep' : 7.4, 'Oct' : 10.4, 'Nov' : 13.2, 'Dic' : 15.1},
	'Temperatura máxima (°C)' : {
            'Ene' : 23.1, 'Feb' : 22.2, 'Mar' : 19.7, 'Abr' : 15.7, 'May' : 10.7, 'Jun' : 7.1, 'Jul' : 7.3, 'Ago' : 9.9, 'Sep' : 13.3, 'Oct' : 16.6, 'Nov' : 19.6, 'Dic' : 21.5},
	'Temperatura mínima (°C)' : {
            'Ene' : 9.7, 'Feb' : 9.2, 'Mar' : 7.4, 'Abr' : 4.9, 'May' : 2.0, 'Jun' : -0.1, 'Jul' : -0.4, 'Ago' : 0.6, 'Sep' : 2.2, 'Oct' : 4.4, 'Nov' : 6.7, 'Dic' : 8.6},
	'Humedad relativa (%)' : {
            'Ene' : 50.9, 'Feb' : 55.3, 'Mar' : 58.0, 'Abr' : 62.5, 'May' : 69.9, 'Jun' : 74.4, 'Jul' : 72.4, 'Ago' : 68.1, 'Sep' : 62.3, 'Oct' : 56.4, 'Nov' : 51.6, 'Dic' : 51.4},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 30.2, 'Feb' : 28.8, 'Mar' : 26.8, 'Abr' : 26.8, 'May' : 25.5, 'Jun' : 26.2, 'Jul' : 25.2, 'Ago' : 24.9, 'Sep' : 25.6, 'Oct' : 28.7, 'Nov' : 29.6, 'Dic' : 30.8},
	'Nubosidad total (octavos)' : {
            'Ene' : 4.6, 'Feb' : 4.3, 'Mar' : 4.0, 'Abr' : 4.0, 'May' : 3.9, 'Jun' : 3.9, 'Jul' : 3.8, 'Ago' : 3.9, 'Sep' : 4.1, 'Oct' : 4.3, 'Nov' : 4.6, 'Dic' : 4.7},
	'Precipitación (mm)' : {
            'Ene' : 14.3, 'Feb' : 22.5, 'Mar' : 23.4, 'Abr' : 19.1, 'May' : 31.1, 'Jun' : 33.7, 'Jul' : 22.5, 'Ago' : 18.3, 'Sep' : 14.3, 'Oct' : 17.3, 'Nov' : 14.9, 'Dic' : 20.2},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 6.4, 'Feb' : 6.3, 'Mar' : 6.7, 'Abr' : 7.4, 'May' : 8.6, 'Jun' : 8.4, 'Jul' : 6.5, 'Ago' : 6.8, 'Sep' : 5.9, 'Oct' : 6.4, 'Nov' : 6.6, 'Dic' : 7.5},
},
{
	'Estación' : 'RÍO GALLEGOS AERO', 
	'Temperatura (°C)' : {
            'Ene' : 13.8, 'Feb' : 13.2, 'Mar' : 10.8, 'Abr' : 7.6, 'May' : 4.2, 'Jun' : 1.4, 'Jul' : 1.2, 'Ago' : 3.1, 'Sep' : 5.7, 'Oct' : 8.4, 'Nov' : 11.1, 'Dic' : 12.8},
	'Temperatura máxima (°C)' : {
            'Ene' : 20.0, 'Feb' : 19.6, 'Mar' : 17.0, 'Abr' : 13.2, 'May' : 8.4, 'Jun' : 4.9, 'Jul' : 4.8, 'Ago' : 7.4, 'Sep' : 11.3, 'Oct' : 14.8, 'Nov' : 17.2, 'Dic' : 18.8},
	'Temperatura mínima (°C)' : {
            'Ene' : 7.6, 'Feb' : 7.1, 'Mar' : 5.3, 'Abr' : 2.9, 'May' : 0.2, 'Jun' : -2.0, 'Jul' : -2.4, 'Ago' : -0.6, 'Sep' : 0.9, 'Oct' : 2.4, 'Nov' : 4.8, 'Dic' : 6.6},
	'Humedad relativa (%)' : {
            'Ene' : 52.4, 'Feb' : 56.8, 'Mar' : 62.3, 'Abr' : 68.9, 'May' : 76.2, 'Jun' : 80.2, 'Jul' : 78.4, 'Ago' : 73.7, 'Sep' : 66.4, 'Oct' : 58.0, 'Nov' : 52.8, 'Dic' : 52.0},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 27.1, 'Feb' : 25.6, 'Mar' : 22.8, 'Abr' : 22.5, 'May' : 19.4, 'Jun' : 19.0, 'Jul' : 18.6, 'Ago' : 19.7, 'Sep' : 20.3, 'Oct' : 24.1, 'Nov' : 26.7, 'Dic' : 27.4},
	'Nubosidad total (octavos)' : {
            'Ene' : 5.6, 'Feb' : 5.2, 'Mar' : 4.9, 'Abr' : 4.8, 'May' : 4.5, 'Jun' : 4.3, 'Jul' : 4.3, 'Ago' : 4.4, 'Sep' : 4.7, 'Oct' : 4.8, 'Nov' : 5.2, 'Dic' : 5.6},
	'Precipitación (mm)' : {
            'Ene' : 27.7, 'Feb' : 27.1, 'Mar' : 26.7, 'Abr' : 26.7, 'May' : 26.9, 'Jun' : 18.3, 'Jul' : 19.2, 'Ago' : 16.9, 'Sep' : 13.3, 'Oct' : 16.9, 'Nov' : 22.7, 'Dic' : 25.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 10.1, 'Feb' : 7.9, 'Mar' : 8.7, 'Abr' : 8.6, 'May' : 8.3, 'Jun' : 7.3, 'Jul' : 7.4, 'Ago' : 6.4, 'Sep' : 6.2, 'Oct' : 6.0, 'Nov' : 8.0, 'Dic' : 9.6},
},
{
	'Estación' : 'RÍO GRANDE B.A.', 
	'Temperatura (°C)' : {
            'Ene' : 10.9, 'Feb' : 10.3, 'Mar' : 8.1, 'Abr' : 5.5, 'May' : 2.6, 'Jun' : -0.1, 'Jul' : -0.2, 'Ago' : 1.4, 'Sep' : 3.5, 'Oct' : 6.2, 'Nov' : 8.4, 'Dic' : 10.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 16.1, 'Feb' : 15.7, 'Mar' : 13.5, 'Abr' : 10.5, 'May' : 6.5, 'Jun' : 3.1, 'Jul' : 3.0, 'Ago' : 5.2, 'Sep' : 8.3, 'Oct' : 11.4, 'Nov' : 13.4, 'Dic' : 15.1},
	'Temperatura mínima (°C)' : {
            'Ene' : 5.7, 'Feb' : 5.4, 'Mar' : 3.5, 'Abr' : 1.6, 'May' : -0.8, 'Jun' : -3.2, 'Jul' : -3.1, 'Ago' : -1.7, 'Sep' : -0.2, 'Oct' : 1.6, 'Nov' : 3.3, 'Dic' : 4.8},
	'Humedad relativa (%)' : {
            'Ene' : 72.7, 'Feb' : 74.6, 'Mar' : 77.8, 'Abr' : 82.4, 'May' : 86.0, 'Jun' : 87.7, 'Jul' : 86.5, 'Ago' : 84.5, 'Sep' : 79.5, 'Oct' : 73.8, 'Nov' : 70.0, 'Dic' : 70.6},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 29.1, 'Feb' : 27.2, 'Mar' : 25.3, 'Abr' : 23.4, 'May' : 19.8, 'Jun' : 17.4, 'Jul' : 18.0, 'Ago' : 20.6, 'Sep' : 21.9, 'Oct' : 26.6, 'Nov' : 28.1, 'Dic' : 29.6},
	'Nubosidad total (octavos)' : {
            'Ene' : 5.5, 'Feb' : 5.2, 'Mar' : 4.9, 'Abr' : 4.7, 'May' : 4.4, 'Jun' : 4.1, 'Jul' : 4.1, 'Ago' : 4.2, 'Sep' : 4.5, 'Oct' : 4.8, 'Nov' : 5.2, 'Dic' : 5.5},
	'Precipitación (mm)' : {
            'Ene' : 36.0, 'Feb' : 29.7, 'Mar' : 27.2, 'Abr' : 28.8, 'May' : 29.4, 'Jun' : 26.7, 'Jul' : 23.9, 'Ago' : 20.7, 'Sep' : 17.1, 'Oct' : 18.5, 'Nov' : 27.0, 'Dic' : 36.0},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 12.4, 'Feb' : 10.9, 'Mar' : 9.9, 'Abr' : 9.8, 'May' : 9.9, 'Jun' : 8.0, 'Jul' : 7.6, 'Ago' : 7.6, 'Sep' : 7.9, 'Oct' : 7.8, 'Nov' : 9.2, 'Dic' : 11.3},
},
{
	'Estación' : 'BASE ESPERANZA', 
	'Temperatura (°C)' : {
            'Ene' : 1.4, 'Feb' : 0.7, 'Mar' : -2.3, 'Abr' : -6.1, 'May' : -8.2, 'Jun' : -10.4, 'Jul' : -10.5, 'Ago' : -9.0, 'Sep' : -6.5, 'Oct' : -4.3, 'Nov' : -1.1, 'Dic' : 0.8},
	'Temperatura máxima (°C)' : {
            'Ene' : 4.3, 'Feb' : 3.7, 'Mar' : 1.2, 'Abr' : -2.1, 'May' : -4.0, 'Jun' : -6.2, 'Jul' : -6.3, 'Ago' : -4.6, 'Sep' : -2.3, 'Oct' : -0.4, 'Nov' : 2.1, 'Dic' : 3.8},
	'Temperatura mínima (°C)' : {
            'Ene' : -1.2, 'Feb' : -2.0, 'Mar' : -5.6, 'Abr' : -9.7, 'May' : -12.1, 'Jun' : -14.3, 'Jul' : -14.8, 'Ago' : -13.2, 'Sep' : -10.4, 'Oct' : -8.0, 'Nov' : -4.2, 'Dic' : -1.9},
	'Humedad relativa (%)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 19.4, 'Feb' : 23.7, 'Mar' : 25.6, 'Abr' : 27.1, 'May' : 25.7, 'Jun' : 27.9, 'Jul' : 30.4, 'Ago' : 28.5, 'Sep' : 28.1, 'Oct' : 29.7, 'Nov' : 24.8, 'Dic' : 24.1},
	'Nubosidad total (octavos)' : {
            'Ene' : 6.3, 'Feb' : 6.1, 'Mar' : 5.9, 'Abr' : 5.7, 'May' : 5.2, 'Jun' : 5.1, 'Jul' : 5.0, 'Ago' : 5.1, 'Sep' : 5.4, 'Oct' : 5.7, 'Nov' : 5.9, 'Dic' : 6.1},
	'Precipitación (mm)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
},
{
	'Estación' : 'BASE ORCADAS', 
	'Temperatura (°C)' : {
            'Ene' : 1.4, 'Feb' : 1.4, 'Mar' : 0.4, 'Abr' : -1.8, 'May' : -4.6, 'Jun' : -7.9, 'Jul' : -9.3, 'Ago' : -7.8, 'Sep' : -5.4, 'Oct' : -2.8, 'Nov' : -0.7, 'Dic' : 0.6},
	'Temperatura máxima (°C)' : {
            'Ene' : 3.4, 'Feb' : 3.4, 'Mar' : 2.3, 'Abr' : 0.4, 'May' : -1.8, 'Jun' : -4.4, 'Jul' : -5.3, 'Ago' : -4.0, 'Sep' : -1.9, 'Oct' : 0.4, 'Nov' : 2.3, 'Dic' : 3.0},
	'Temperatura mínima (°C)' : {
            'Ene' : -0.5, 'Feb' : -0.3, 'Mar' : -1.5, 'Abr' : -4.1, 'May' : -7.5, 'Jun' : -11.7, 'Jul' : -13.9, 'Ago' : -12.0, 'Sep' : -9.3, 'Oct' : -5.9, 'Nov' : -3.2, 'Dic' : -1.4},
	'Humedad relativa (%)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 19.9, 'Feb' : 23.7, 'Mar' : 23.9, 'Abr' : 24.9, 'May' : 24.0, 'Jun' : 23.7, 'Jul' : 24.2, 'Ago' : 25.6, 'Sep' : 24.7, 'Oct' : 26.5, 'Nov' : 23.6, 'Dic' : 23.3},
	'Nubosidad total (octavos)' : {
            'Ene' : 7.5, 'Feb' : 7.4, 'Mar' : 7.3, 'Abr' : 7.2, 'May' : 6.9, 'Jun' : 6.4, 'Jul' : 6.1, 'Ago' : 6.2, 'Sep' : 6.6, 'Oct' : 7.0, 'Nov' : 7.3, 'Dic' : 7.3},
	'Precipitación (mm)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
},
{
	'Estación' : 'BASE BELGRANO II', 
	'Temperatura (°C)' : {
            'Ene' : -2.4, 'Feb' : -7.0, 'Mar' : -12.0, 'Abr' : -16.7, 'May' : -18.1, 'Jun' : -19.1, 'Jul' : -20.4, 'Ago' : -20.2, 'Sep' : -18.4, 'Oct' : -14.8, 'Nov' : -8.0, 'Dic' : -3.0},
	'Temperatura máxima (°C)' : {
            'Ene' : 0.7, 'Feb' : -3.7, 'Mar' : -8.8, 'Abr' : -13.5, 'May' : -14.6, 'Jun' : -15.7, 'Jul' : -17.1, 'Ago' : -16.6, 'Sep' : -14.9, 'Oct' : -11.0, 'Nov' : -4.1, 'Dic' : 0.4},
	'Temperatura mínima (°C)' : {
            'Ene' : -5.9, 'Feb' : -10.9, 'Mar' : -16.1, 'Abr' : -20.7, 'May' : -22.0, 'Jun' : -23.1, 'Jul' : -24.5, 'Ago' : -24.4, 'Sep' : -23.0, 'Oct' : -19.4, 'Nov' : -12.3, 'Dic' : -6.9},
	'Humedad relativa (%)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Velocidad del Viento (km/h)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Nubosidad total (octavos)' : {
            'Ene' : 5.4, 'Feb' : 5.0, 'Mar' : 4.7, 'Abr' : 4.4, 'May' : 4.1, 'Jun' : 3.9, 'Jul' : 4.2, 'Ago' : 4.6, 'Sep' : 4.7, 'Oct' : 4.8, 'Nov' : 5.0, 'Dic' : 5.0},
	'Precipitación (mm)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
},
{
	'Estación' : 'BASE MARAMBIO', 
	'Temperatura (°C)' : {
            'Ene' : -0.8, 'Feb' : -2.0, 'Mar' : -6.1, 'Abr' : -10.8, 'May' : -12.8, 'Jun' : -14.7, 'Jul' : -14.7, 'Ago' : -13.1, 'Sep' : -10.1, 'Oct' : -7.6, 'Nov' : -3.6, 'Dic' : -1.2},
	'Temperatura máxima (°C)' : {
            'Ene' : 1.6, 'Feb' : 0.7, 'Mar' : -2.8, 'Abr' : -6.6, 'May' : -8.5, 'Jun' : -10.5, 'Jul' : -10.3, 'Ago' : -8.9, 'Sep' : -5.8, 'Oct' : -3.8, 'Nov' : -0.5, 'Dic' : 1.3},
	'Temperatura mínima (°C)' : {
            'Ene' : -2.9, 'Feb' : -4.3, 'Mar' : -9.1, 'Abr' : -14.2, 'May' : -16.6, 'Jun' : -18.3, 'Jul' : -18.7, 'Ago' : -17.3, 'Sep' : -14.1, 'Oct' : -11.0, 'Nov' : -6.5, 'Dic' : -3.5},
	'Humedad relativa (%)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 23.7, 'Feb' : 25.5, 'Mar' : 28.5, 'Abr' : 31.1, 'May' : 30.5, 'Jun' : 34.8, 'Jul' : 34.5, 'Ago' : 31.5, 'Sep' : 31.9, 'Oct' : 33.6, 'Nov' : 28.9, 'Dic' : 26.7},
	'Nubosidad total (octavos)' : {
            'Ene' : 6.7, 'Feb' : 6.5, 'Mar' : 6.1, 'Abr' : 5.6, 'May' : 4.9, 'Jun' : 4.9, 'Jul' : 4.8, 'Ago' : 4.8, 'Sep' : 5.2, 'Oct' : 5.7, 'Nov' : 6.2, 'Dic' : 6.4},
	'Precipitación (mm)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
},
{
	'Estación' : 'BASE SAN MARTÍN', 
	'Temperatura (°C)' : {
            'Ene' : 2.0, 'Feb' : 0.9, 'Mar' : -1.2, 'Abr' : -3.3, 'May' : -5.3, 'Jun' : -9.3, 'Jul' : -11.6, 'Ago' : -11.5, 'Sep' : -8.9, 'Oct' : -5.9, 'Nov' : -2.0, 'Dic' : 0.8},
	'Temperatura máxima (°C)' : {
            'Ene' : 4.5, 'Feb' : 3.3, 'Mar' : 1.3, 'Abr' : -0.9, 'May' : -2.3, 'Jun' : -5.8, 'Jul' : -7.3, 'Ago' : -6.9, 'Sep' : -4.6, 'Oct' : -2.1, 'Nov' : 1.2, 'Dic' : 3.4},
	'Temperatura mínima (°C)' : {
            'Ene' : -0.3, 'Feb' : -1.3, 'Mar' : -3.6, 'Abr' : -5.8, 'May' : -8.4, 'Jun' : -13.5, 'Jul' : -16.3, 'Ago' : -16.8, 'Sep' : -13.9, 'Oct' : -10.2, 'Nov' : -5.5, 'Dic' : -1.8},
	'Humedad relativa (%)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 14.6, 'Feb' : 17.7, 'Mar' : 22.3, 'Abr' : 20.4, 'May' : 19.3, 'Jun' : 18.0, 'Jul' : 17.3, 'Ago' : 18.9, 'Sep' : 17.5, 'Oct' : 20.3, 'Nov' : 19.2, 'Dic' : 18.3},
	'Nubosidad total (octavos)' : {
            'Ene' : 6.2, 'Feb' : 6.5, 'Mar' : 6.3, 'Abr' : 6.0, 'May' : 5.8, 'Jun' : 5.2, 'Jul' : 5.5, 'Ago' : 5.9, 'Sep' : 6.3, 'Oct' : 6.4, 'Nov' : 6.4, 'Dic' : 6.2},
	'Precipitación (mm)' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : None, 'Feb' : None, 'Mar' : None, 'Abr' : None, 'May' : None, 'Jun' : None, 'Jul' : None, 'Ago' : None, 'Sep' : None, 'Oct' : None, 'Nov' : None, 'Dic' : None},
}
]
"""
def obtener_valor_maximo(promedios):
    maximo = max(promedios)
    return maximo
	
        


def calcular_promedio(diccionarios):
    promedios = []
    for diccionario in diccionarios:
        valores = [valor for valor in diccionario.values() if valor is not None]
        if valores:
            promedio = sum(valores) / len(valores)
            promedios.append(promedio)
    return promedios
        

"""  
def get_sum_of_values(condition):
    total_values = {}
    for estacion in estadisticas: # Access station
        for key in estacion: # Access type of value
            sum_values = 0
            for month in estacion[condition]: # Access individual values then Sum every value from that type on the station
                value = (estacion[condition][month])
                if value == None: sum_values += 0
                else: sum_values += value
            sum_values = round(sum_values,2)
        total_values[estacion['Estación']]=sum_values # make a separate dictionary to hold the sum of values based on station 
    return total_values

def get_sorted_values(total_values):
    sorted_values = sorted(total_values.values(),reverse=True) # make an array that holds the sorted values of the sums
    
    amount_null = 0 # Search null data in sorted values
    for item in sorted_values:
        if item == 0: amount_null+=1

    for i in range(amount_null): # remove from the sorted value null data
        sorted_values.remove(0)
    # Saco todas las estaciones que le faltan algun dato porque me molestan para tomar mediciones
    return sorted_values # De este modo tambien cumplo con la ultima consigna desde el principio

def get_max_value(type_medition):
    total_values = get_sum_of_values(type_medition)
    sorted_values = get_sorted_values(total_values)
    for item in total_values: # get Max value of station
        if total_values[item] == sorted_values[0]:
            print(item)
    print(type_medition,' Average: ',end='')
    print(round(sorted_values[0]/12,2)) # print max value

def get_min_value(type_medition):
    valores_totales = get_sum_of_values(type_medition)
    valores_ordenados = get_sorted_values(valores_totales)
    for item in valores_totales:
        if valores_totales[item] == valores_ordenados[-1]:
            print(item)
    print(type_medition,' Avarage: ',end='')
    print(round(valores_ordenados[-1]/12, 2))



def get_less_windy_station():
    print('Less Windy Station: ',end='')
    get_min_value('Velocidad del Viento (km/h)')

get_less_windy_station()                    

def get_most_windy_station():
    print('Most Windy Station: ',end='')
    get_max_value('Velocidad del Viento (km/h)')

get_most_windy_station()
	
			