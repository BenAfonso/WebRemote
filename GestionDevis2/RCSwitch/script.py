import os
os.seteuid(0)
os.system("pilight-send -p kaku_switch_old -u 0 -i -f")
