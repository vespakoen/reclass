#
# -*- coding: utf-8 -*-
#
# This file is part of reclass (http://github.com/madduck/reclass)
#
# Copyright © 2007–13 martin f. krafft <madduck@madduck.net>
# Released under the terms of the Artistic Licence 2.0
#

from output import OutputLoader
from storage import StorageBackendLoader
from config import path_mangler

def get_storage(storage_type, nodes_uri, classes_uri, file_extension, class_mappings):
    storage_class = StorageBackendLoader(storage_type).load()
    return storage_class(nodes_uri, classes_uri, file_extension, class_mappings)


def get_nodeinfo(storage_type, inventory_base_uri, nodes_uri, classes_uri, file_extension,
                 nodename, class_mappings):
    nodes_uri, classes_uri = path_mangler(inventory_base_uri, nodes_uri,
                                          classes_uri)
    storage = get_storage(storage_type, nodes_uri, classes_uri, file_extension,
                          class_mappings)
    # TODO: template interpolation
    return storage.nodeinfo(nodename)


def get_inventory(storage_type, inventory_base_uri, nodes_uri, classes_uri, file_extension,
                  class_mappings):
    nodes_uri, classes_uri = path_mangler(inventory_base_uri, nodes_uri,
                                          classes_uri)
    storage = get_storage(storage_type, nodes_uri, classes_uri, file_extension,
                          class_mappings)
    return storage.inventory()


def output(data, fmt, pretty_print=False):
    output_class = OutputLoader(fmt).load()
    outputter = output_class()
    return outputter.dump(data, pretty_print=pretty_print)
