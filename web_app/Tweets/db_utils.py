from cloudant.client import CouchDB
from cloudant.design_document import DesignDocument


def connect_database(username, password, url, database_name):
    client = CouchDB(username, password, url=url, connect=True)
    return client[database_name]

def acess_view(database, ddoc_id, view_id, group):
    view = database.get_design_document(ddoc_id).get_view(view_id)
    result = view.custom_result(group = group)
    return result

