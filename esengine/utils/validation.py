# coding: utf-8

from esengine.exceptions import ClientError


def validate_client(es):
    """
    A valid ES client is a interface which must implements at least
    "index" and "search" public methods.
    preferably an elasticsearch.ElasticSearch() instance
    :param es:
    :return: None
    """

    if not es:
        raise ClientError("ES client cannot be Nonetype")

    try:
        if not callable(es.index) or not callable(es.search) or \
                not callable(es.get):
            raise ClientError(
                "index or search or get Interface is not callable"
            )
    except AttributeError as e:
        raise ClientError(str(e))