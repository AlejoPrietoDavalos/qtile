### Quickstart
Clonar el repo en `~/.config`.
```bash
cd ~/.config
git clone https://github.com/AlejoPrietoDavalos/qtile
cd qtile
```

```bash
git clone https://github.com/elParaguayo/qtile-extras
cd qtile-extras
pip install . --break-system-packages
```

#sudo pacman -Syu discord # Para actualizar discord

### Archivo .log de qtile
Si se rompe algo, podés ver acá el error.
```bash
cat ~/.local/share/qtile/qtile.log
```


### TODO
- `betterlockscreen`, pantalla de lockeo?
- TODO: CONFIGURAR ROFI.
- TODO: VER EJECUCIÓN DE SCRIPTS, Y COMANDOS.
- TODO: FICHEROS DE ESTADO DEL SISTEMA CON LECTURA EN PYTHON.
- TODO: Se puede dejar corriendo un proceso en 2do plano que quede dormido hasta que sea llamado? no quiero que cargue y procese todo python de cero cada vez, para que sea bien dinámico.

### Instalar los repos AUR.
```bash
git clone https://aur.archlinux.org/paru-bin.git
cd paru-bin
makepkg -si
cd ..
# borrar
```
sudo mount /dev/sdb1 /mnt/disco_externo/
