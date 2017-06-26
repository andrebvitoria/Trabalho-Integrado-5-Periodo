from splinter.browser import Browser


def before_all(context):
    context.browser = Browser('chrome')
    context.server_url = 'http://localhost:8000'


def after_all(context):
    context.browser.pause()
    context.browser = None