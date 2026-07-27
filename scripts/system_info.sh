SYSTEM INFORMATION

echo Fecha actual: $(date)
echo Usuario actual: $(whoami)
echo Directorio actual:$PWD
echo Sistema operativo: $(uname -o)
echo Versión del kernel: $(uname -r)
echo Tiempo desde el último arranque:$(uptime -s) 
echo Espacio libre en disco: $(df -h)
 
