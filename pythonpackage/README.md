# Hello Google Python Package

This manifest installs a python package and allows us to perform a GET on 
Google's homepage.

## Build the application

Run the following:

```
flatpak-builder build-dir org.flatpak.HelloPackage.json --force-clean
```

## Run the application

Run the following:

```
flatpak-builder --run build-dir org.flatpak.HelloPackage.json runner.sh
```