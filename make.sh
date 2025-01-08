#!/bin/bash

cd mkdocs/ && mkdocs build &&  cp site/* ../docs -adpR && cd ..
