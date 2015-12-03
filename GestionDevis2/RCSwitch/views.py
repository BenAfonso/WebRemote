from django.shortcuts import render
import os
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
# Create your views here.

@login_required(login_url='/')
def home(request):
    return render_to_response('base.html', context_instance=RequestContext(request))


def switch_on(request,channel,plugNumber):
    
    # PlugNumber 0->2 [1-3]
    # channel 0->3 [A-D]
    cmd = "sudo pilight-send -p  kaku_switch_old -i "+str(plugNumber)+" -u "+str(channel)+" -t"
    # Lancement de la commande
    os.system(cmd)
    return redirect('/switchs/')
    
    
def switch_off(request,channel,plugNumber):
    cmd = "sudo pilight-send -p  kaku_switch_old -i "+str(plugNumber)+" -u "+str(channel)+" -f"
    # Lancement de la commande
    os.system(cmd)
    return redirect('/switchs/')

    
    