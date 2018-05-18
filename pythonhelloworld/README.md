# Hello World Python

This manifest installs python and a simple script.

## Build the application

Run the following:

```
flatpak-builder build-dir org.flatpak.HelloPy.json --force-clean
```

## Run the application

Run the following:

```
flatpak-builder --run build-dir org.flatpak.HelloPy.json runner.sh
```
