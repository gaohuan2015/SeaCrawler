from Helper import ConstructURL
from Helper import SendRequestToServer
from Helper import DownLoadFile
from concurrent.futures import ThreadPoolExecutor
import json
import threading
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')


def SeaCrawler(config):
    north = config['north']
    south = config['south']
    west = config['west']
    east = config['east']
    time = config['time']
    fileName = "{north}_{south}_{west}_{east}_{time}".format(
        north=north, south=south, east=east, west=west, time=time)
    logger.info("{name} threading is running".format(
        name=threading.current_thread().name))
    url = ConstructURL(north, south, east, west, time)
    response = SendRequestToServer(url)
    DownLoadFile(fileName, response)


if __name__ == "__main__":
    threadPool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="test_")
    with open('Sea Crawler\Config.json', 'r') as f:
        config = json.load(f)
    for i in config['downloadFiles']:
        future = threadPool.submit(SeaCrawler, i)
    threadPool.shutdown(wait=True)

logging.debug('End of program')
