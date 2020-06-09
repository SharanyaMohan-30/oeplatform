from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from rdflib import Graph, RDFS
from oeplatform.settings import ONTOLOGY_FOLDER
from collections import OrderedDict

import os
import re


def collect_modules(path):
    modules = dict()
    for file in os.listdir(path):
        if not os.path.isdir(os.path.join(path,file)):
            match = re.match("^(?P<filename>.*)\.(?P<extension>\w+)$", file)
            filename, extension = match.groups()
            if filename not in modules:
                modules[filename] = dict(extensions=[], comment="No description found")
            if extension == "owl":
                g = Graph()
                g.parse(os.path.join(path, file))
                root = dict(g.namespaces())['']
                comment = next(g.objects(root, RDFS.comment))
                modules[filename]["comment"] = comment
            modules[filename]["extensions"].append(extension)
    return modules

class OntologyOverview(View):
    def get(self, request, version=None):
        ontology = "oeo"
        versions = os.listdir(f"{ONTOLOGY_FOLDER}/{ontology}")
        if not version:
            version = max((d for d in versions), key=lambda d:[int(x) for x in d.split(".")])
        if request.headers.get("Accept") == "application/rdf+xml":
            return redirect(f"/ontology/releases/oeo/{version}/oeo.owl")
        else:

            main_module = collect_modules(f"{ONTOLOGY_FOLDER}/{ontology}/{version}")
            main_module_name = list(main_module.keys())[0]
            main_module = main_module[main_module_name]
            main_module["name"] = main_module_name
            submodules = collect_modules(f"{ONTOLOGY_FOLDER}/{ontology}/{version}/modules")
            # Collect all file names


            return render(request, "ontology/oeo.html", dict(
                ontology=ontology,
                version=version,
                main_module=main_module,
                submodules=submodules.items()
            ))


class OntologyStatics(View):
    def get(self, request, ontology, file, version=None, extension=None):
        """
        Returns the requested file `{file}.{extension}` of version `version`
        of ontology `ontology`

        :param version: default: highest version in folder
        :param extension: default: `.owl`
        :return:
        """

        if not extension:
            extension = "owl"
        if not version:
            version = max((d for d in os.listdir(f"{ONTOLOGY_FOLDER}/{ontology}")), key=lambda d:[int(x) for x in d.split(".")])
        file_path = f"{ONTOLOGY_FOLDER}/{ontology}/{version}/{file}.{extension}"
        if os.path.exists(file_path):
            with open(file_path) as f:
                response = HttpResponse(f, content_type="application/rdf+xml")
                response["Content-Disposition"] = f'attachment; filename="{file}.{extension}"'
                return response
        else:
            file_path = f"{ONTOLOGY_FOLDER}/{ontology}/{version}/modules/{file}.{extension}"
            with open(file_path) as f:
                response = HttpResponse(f, content_type="application/rdf+xml")
                response["Content-Disposition"] = f'attachment; filename="{file}.{extension}"'
                return response