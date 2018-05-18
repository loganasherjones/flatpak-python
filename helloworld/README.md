# Hello World

This is the most basic example. 

## Build the application

Run the following:

```
flatpak-builder build-dir org.flatpak.Hello.json --force-clean
```

## Run the application

Run the following:

```
flatpak-builder --run build-dir org.flatpak.Hello.json hello.sh
```
