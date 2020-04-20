import qbittorrentapi
import sys
import os
import time
import traceback


SEEDING_RATIO_THRESHOLD = 2.0
LOG_FILE_NAME = 'qbitman_log.txt'
LOG_FILE_PATH = os.path.join(os.path.split(__file__)[0], LOG_FILE_NAME)


# redirect prints and exceptions
sys.stdout = open(LOG_FILE_PATH, 'w')
sys.stderr = open(LOG_FILE_PATH, 'w')


def main():
    print("Starting at %s" % time.ctime())
    qbt_client = qbittorrentapi.Client(host='localhost:8080')
    qbt_client.auth_log_in() # using empty password

    print("Connected")

    # stop any torrent that passes the seeding ratio threshold
    for torrent in qbt_client.torrents_info():
        if torrent.ratio >= SEEDING_RATIO_THRESHOLD:
            print("Pausing %s (seeding ratio = %.02f)" % (torrent.name, torrent.ratio))
            qbt_client.torrents_pause(torrent.hash)
 
    # close the program if everything stopped or there are no torrents
    for torrent in qbt_client.torrents_info():
        if torrent.state != 'pausedUP':
            print("Still active: %s" % torrent.name)
            break
    else:
        # no break, i.e. empty list or everything passed 2.0 seeding ratio
        print("Shutting down")
        qbt_client.app.shutdown

    print("Finished at %s" % time.ctime())


if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()
