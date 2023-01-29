import os
import math
from pyproj import Transformer
promt = ("1.ECEF->BLH\n\
2.BLH->ECEF\n\
3.BLH->MER\n\
4.MER->BLH\n")
choose = input(promt)


def ecef2blh(x, y, z):
    trans = Transformer.from_crs(
        crs_from={"proj": 'geocent', "ellps": 'WGS84', "datum": 'WGS84'}, crs_to='EPSG:4326', always_xy=True)
    lon, lat, alt = trans.transform(x, y, z, radians=False)
    return lon, lat, lat


def blh2ecef(lon, lat, alt):
    trans = Transformer.from_crs(
        crs_from='EPSG:4326', crs_to={"proj": 'geocent', "ellps": 'WGS84', "datum": 'WGS84'},  always_xy=True)
    x, y, z = trans.transform(lon, lat, alt, radians=False)
    return x, y, z


def blh2mer(lon, lat):
    trans = Transformer.from_crs(
        crs_from='EPSG:4326', crs_to='EPSG:3857', always_xy=True)
    x, y = trans.transform(lon, lat, radians=False)
    return x, y


def mer2blh(x, y):
    trans = Transformer.from_crs(
        crs_to='EPSG:4326', crs_from='EPSG:3857', always_xy=True)
    lon, lat = trans.transform(x, y, radians=False)
    return lon, lat


match int(choose):
    case 1:
        x, y, z = input("please input ecef(x,y,z):").split(',')
        lon, lat, alt = ecef2blh(x, y, z)
        print(lon, lat, alt)
    case 2:
        lon, lat, alt = input("please input blh(lon,lat,alt):").split(',')
        x, y, z = blh2ecef(lon, lat, alt)
        print(x, y, z)
    case 3:
        lon, lat = input("please input blh(lon,lat):").split(',')
        x, y = blh2mer(lon, lat)
        print(x, y)
        pass
    case 4:
        x, y = input("please input blh(lon,lat):").split(',')
        lon, lat = mer2blh(x, y)
        print(lon, lat)
    case _:
        print("default")
