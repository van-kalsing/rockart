import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("rockart").version
except pkg_resources.DistributionNotFound:
    pass
