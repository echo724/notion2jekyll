#!/usr/bin/env zsh


read commit

#git push
git pull
git add .
git commit -m commit
git push

#build
rm -rf build dist
python setup.py bdist_wheel
twine upload dist/*
