function preventcopy(){
	document.oncontextmenu=function(e){
		e.preventDefault();
	}
	document.onselectstart=function(e){
		e.preventDefault();
	}
	document.oncopy=function(e){
		e.preventDefault();
	}
}
function allowcopy(){
	document.oncontextmenu=new Function("event.returnValue=true"); 
	document.onselectstart=new Function("event.returnValue=true"); 
	document.oncopy=new Function("event.returnValue=true"); 
}