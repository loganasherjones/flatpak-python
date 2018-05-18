# Hello Google Python

This manifest installs python, the requests library and a simple script.

## Build the application

Run the following:

```
flatpak-builder build-dir org.flatpak.HelloGoogle.json --force-clean
```

## Run the application

Run the following:

```
flatpak-builder --run build-dir org.flatpak.HelloGoogle.json runner.sh
```
