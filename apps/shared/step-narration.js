/* Optional, reusable step narration. No microphone or API key required. */
(function(global){
'use strict';
function mount(container){
 if(!container)return {update:function(){},stop:function(){}};
 var supported=!!(global.speechSynthesis&&global.SpeechSynthesisUtterance);
 var enabled=false,current='',key='',synth=global.speechSynthesis;
 var row=document.createElement('div');row.style.cssText='display:flex;align-items:center;flex-wrap:wrap;gap:6px;margin:8px 0;font-size:.9rem';
 row.setAttribute('role','group');row.setAttribute('aria-label','Step narration');
 function button(label){var b=document.createElement('button');b.type='button';b.textContent=label;row.appendChild(b);return b}
 var toggle=button('Audio off'), replay=button('Replay'), stopBtn=button('Stop');
 var rate=document.createElement('select');rate.setAttribute('aria-label','Narration speed');
 [['0.8','Slow'],['1','Normal'],['1.2','Fast']].forEach(function(v){var opt=document.createElement('option');opt.value=v[0];opt.textContent=v[1];rate.appendChild(opt)});rate.value='1';row.appendChild(rate);
 var message=document.createElement('span');message.setAttribute('role','status');row.appendChild(message);container.prepend(row);
 function stop(){if(supported)synth.cancel()}
 function speak(){
  if(!supported||!current)return;stop();
  try{var u=new SpeechSynthesisUtterance(current),vs=synth.getVoices();
   var voice=vs.find(function(v){return /^en-IE$/i.test(v.lang)&&v.localService})||vs.find(function(v){return /^en-IE$/i.test(v.lang)})||vs.find(function(v){return /^en-GB$/i.test(v.lang)&&v.localService})||vs.find(function(v){return /^en-GB$/i.test(v.lang)});
   u.lang=voice?voice.lang:'en-GB';if(voice)u.voice=voice;u.rate=Number(rate.value);
   u.onerror=function(e){if(e.error!=='canceled'&&e.error!=='interrupted')message.textContent='Audio unavailable on this device.'};
   message.textContent='';synth.speak(u);
  }catch(e){message.textContent='Audio unavailable on this device.'}
 }
 toggle.setAttribute('aria-pressed','false');
 toggle.onclick=function(){enabled=!enabled;toggle.textContent=enabled?'Audio on':'Audio off';toggle.setAttribute('aria-pressed',String(enabled));if(enabled)speak();else stop()};
 replay.onclick=speak;stopBtn.onclick=stop;
 function refresh(){row.hidden=!current;row.style.display=current?'flex':'none';replay.disabled=!supported||!current;toggle.disabled=!supported;stopBtn.disabled=!supported;rate.disabled=!supported}
 function update(text,id){
  var next=String(text||''),nextKey=String(id||next);
  if(nextKey===key&&next===current)return;
  stop();current=next;key=nextKey;refresh();if(enabled&&current)speak();
 }
 if(!supported)message.textContent='This browser has no speech synthesis.';
 refresh();global.addEventListener('pagehide',stop);
 return {update:update,stop:stop};
}
global.WCMStepNarration={mount:mount};
})(window);
