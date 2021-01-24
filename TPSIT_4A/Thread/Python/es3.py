import threading
import logging
import time

def fn_thread(val):
    
    l.acquire()
    logging.info("Thread %s: inizio", val)
    time.sleep(2)
    logging.info("Thread %s: fine", val)
    l.relase()


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level = logging.INFO, datefmt = "%H:%M:%S")

    l = threading.Lock()

    logging.info("PADRE: creo un thread")

    threads = list()
    for i in range(5):
        logging.info("PADRE: creo ed avvio il thread %d", i)
        x = threading.Thread(target= fn_thread, args=(i,))
        threads.append(x)
        x.start()
    
    for i, t in enumerate(threads):
        logging.info("PADRE: prima dell'attesa del thread %s.", i)
        t.join()
        logging.info("PADRE: thread %d terminato", i)


    logging.info("PADRE: fine")
    


if __name__ == "__main__":
    main()