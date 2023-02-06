

class Config:
    def __init__(self, browser, server):
        self.browser = {
            'chrome': 'chrome',
            'firefox': 'firefox',
        }[browser]
        self.server = {
            'prod': 'https://prod',
            'qa': 'https://super_test.awide.local'
        }[server]

