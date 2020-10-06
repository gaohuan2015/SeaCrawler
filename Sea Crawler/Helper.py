import requests
import logging
import threading

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')


def ConstructURL(north, south, east, west, time):
    url = 'http://ncss.hycom.org/thredds/ncss/GLBu0.08/reanalysis/3hrly?var=surf_el&var=salinity&var=water_temp&var=water_u&var=water_v&north={north}&west={west}&east={east}&south={south}&horizStride=1&time={time}T21%3A00%3A00Z&vertCoord=&accept=netcdf'.format(
        north=north, west=west, east=east, south=south, time=time)
    logger.info("{name} Download URL is {url}".format(
        url=url, name=threading.current_thread().name))
    return url


def SendRequestToServer(url):
    response = requests.get(url, stream=True)
    logger.info("{name} Response status code is {statusCode}".format(
        statusCode=response.status_code, name=threading.current_thread().name))
    logger.info("{name} Response header {header}".format(
        header=response.headers, name=threading.current_thread().name))
    return response


def DownLoadFile(file, response):
    logger.info("{name} Download file name {fileName}".format(
        fileName=file, name=threading.current_thread().name))
    try:
        fileName = "Sea Crawler/Data/{fileName}.nc".format(fileName=file)
        f = open(fileName, "wb")
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
        logger.error("{name} Successfully writing file!!".format(
            name=threading.current_thread().name))
        return True
    except IOError:
        logger.error("{name} Error writing file!!".format(
            name=threading.current_thread().name))
        return False
