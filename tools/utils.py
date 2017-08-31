import sys
import time
import hashlib
from six.moves import urllib


def download(filename, url):
    def reporthook(count, block_size, total_size):
        """
        From http://blog.moleculea.com/2012/10/04/urlretrieve-progres-indicator/
        """
        global start_time
        if count == 0:
            start_time = time.time()
            return
        duration = (time.time() - start_time) or 0.01
        progress_size = int(count * block_size)
        speed = int(progress_size / (1024 * duration))
        percent = int(count * block_size * 100 / total_size)
        sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                         (percent, progress_size / (1024 * 1024), speed, duration))
        sys.stdout.flush()
    urllib.request.urlretrieve(url, filename, reporthook)
    print()


def check(filename, sha1):
    with open(filename, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest() == sha1
