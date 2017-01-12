from pyo import *
import random
s=Server().boot()
s.amp=.1

notes=[midiToHz(m) for m in [57,59,62,64,67,69,71]]
notRand=Choice(choice=notes,freq=[5,7,6,4])

soloFad=Fader(6,6,0)
solo=FastSine(freq=notRand,mul=soloFad).mix(2).out()

basseFad=Fader(6,6,0)
basse=FM(carrier=[Randh(min=98.,max=99.,freq=.5) for n in range(4)],mul=basseFad).mix(2).out()

atmoFad=Fader(6,6,0,mul=[random.uniform(.05,.1) for i in range(10)])
atmo=SumOsc(freq=[Randi(min=100.,max=1000,freq=.2) for o in range(70)],mul=atmoFad).mix(2).out()

atmoFadR=Fader(6,6,0,mul=[random.uniform(.05,.1) for i in range(10)])
atmoR=SumOsc(freq=[Randi(min=100.,max=1000,freq=.2) for o in range(70)],mul=atmoFadR).mix(1).out(1)

atmoFadL=Fader(6,6,0,mul=[random.uniform(.05,.1) for i in range(10)])
atmoL=SumOsc(freq=[Randi(min=100.,max=1000,freq=.2) for o in range(70)],mul=atmoFadL).mix(1).out(0)

solo1=FastSine(freq=notRand).mix(2)

shiftFadL=Fader(6,6,0)
shiftL=FreqShift(solo1,shift=800,mul=shiftFadL*.6).mix(1).out(0) 

shiftFadR=Fader(6,6,0)
shiftR=FreqShift(solo1,shift=800,mul=shiftFadR*.6).mix(1).out(1)

atmo1=SumOsc(freq=[Randi(min=100.,max=1000,freq=.2) for o in range(70)]).mix(2)

lowpFad=Fader(6,6,0)
lowp=ButLP(atmo1,freq=300,mul=lowpFad).mix(2).out()

def jouer_solo(state=1):
    if state==1:
        soloFad.play()
    else:
        soloFad.stop()
        
def jouer_basse(state=1):
    if state==1:
        basseFad.play()
    else:
        basseFad.stop()
        
def jouer_atmo(state=1):
    if state==1:
        atmoFad.play()
    else:
        atmoFad.stop()
        
def jouer_atmoR(state=1):
    if state==1:
        atmoFadR.play()
    else:
        atmoFadR.stop()
        
def jouer_atmoL(state=1):
    if state==1:
        atmoFadL.play()
    else:
        atmoFadL.stop()
        
def jouer_shiftL(state=1):
    if state==1:
        shiftFadL.play()
    else:
        shiftFadL.stop()
         
def jouer_shiftR(state=1):
    if state==1:
        shiftFadR.play()
    else:
         shiftFadR.stop()      
        
def jouer_lowp(state=1):
    if state==1:
        lowpFad.play()
    else:
        lowpFad.stop()


def event_0():
    jouer_lowp()
    
def event_1():
    jouer_lowp(0)
    
def event_2():
    jouer_atmoL()

def event_3():
    jouer_atmoR()

def event_4():
    pass

def event_5():
    jouer_shiftL()
    
def event_6():
    jouer_atmoL(0)
        
def event_7():
    pass
            
def event_8():
    jouer_shiftR()

def event_9():
    jouer_atmoR(0)
    
def event_10():
    jouer_shiftL(0)

def event_11():
    jouer_shiftR(0)
    jouer_solo() 
    jouer_basse()         
  
def event_12():
    pass
    
def event_13():
    pass
    
def event_14():
    jouer_basse(0)
    jouer_atmo()
    
def event_15():
    jouer_lowp()
    jouer_atmo(0)
    
def event_16():
    pass
    
def event_17():
    jouer_atmo(0)
    
def event_18():
    jouer_solo(0)
    
def event_19():
    jouer_lowp(0)
    met.stop()

    
met=Metro(time=5).play()
count=Counter(met,max=20)
score=Score(count,fname='event_')
        

s.gui(locals())