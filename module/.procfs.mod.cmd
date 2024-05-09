cmd_/home/pix/projetcs/legal/now/module/procfs.mod := printf '%s\n'   procfs.o | awk '!x[$$0]++ { print("/home/pix/projetcs/legal/now/module/"$$0) }' > /home/pix/projetcs/legal/now/module/procfs.mod
