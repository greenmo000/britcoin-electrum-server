from setuptools import setup

setup(
    name="electrum-britcoin-server",
    version="0.9",
    scripts=['run_electrum_britcoin_server','electrum-britcoin-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumbritcoinserver':'src'
        },
    py_modules=[
        'electrumbritcoinserver.__init__',
        'electrumbritcoinserver.utils',
        'electrumbritcoinserver.storage',
        'electrumbritcoinserver.deserialize',
        'electrumbritcoinserver.networks',
        'electrumbritcoinserver.blockchain_processor',
        'electrumbritcoinserver.server_processor',
        'electrumbritcoinserver.processor',
        'electrumbritcoinserver.version',
        'electrumbritcoinserver.ircthread',
        'electrumbritcoinserver.stratum_tcp',
        'electrumbritcoinserver.stratum_http'
    ],
    description="britcoin Electrum Server",
    author="Thomas Voegtlin & Soopy452000 & greenmo000",
    author_email="britcoin3@gmail.com",
    license="GNU Affero GPLv3",
    url="https://github.com/britcoin3/electrum-britcoin-server/",
    long_description="""Server for the Electrum Lightweight Britcoin Wallet"""
)


