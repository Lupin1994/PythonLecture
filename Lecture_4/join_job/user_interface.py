import data_provider as prov
import logger as log

def temperature_view(senser):
    data = prov.get_temperature(senser)
    log.temperature_logger(data)
    return data

def preassure_view(senser):
    data = prov.get_preassure(senser)
    log.preassure_logger(data)
    return data

def wind_speed_view(senser):
    data = prov.get_wind_speed(senser)
    log.wind_speed_logger(data)
    return data