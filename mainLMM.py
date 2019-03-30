import logging
import logging.config
logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('mainLMM')


logging.info ("__________START______")
from goodreads import client
gc = client.GoodreadsClient('gOCk7w1mOcYTs97j9BmCkw', 'JlcnVqvmuoyznIO06huEbreIcT9mNw4qyFAbjVu3WI')
logging.debug ("apres gc =")

book = gc.book(1)
logging.debug ("apres gc.book")
msg = "BOKK TITLE : "+book.title
logging.info (msg)
logging.debug ("apres book.title")

gc.authenticate()
logging.debug ("apres authenticate")
