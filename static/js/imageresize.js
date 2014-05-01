function lanczosCreate(lobes){
	return function(x){
		if(x>lobes){
			return 0;
		}
		x*=Math.PI;
		if (Math.abs(x) < 1e-16){
			return 1;
		}
		var xx=x/lobes;
		return Math.sin(x) * Math.sin(xx) / x / xx;
	};
}

function thumbnailer(elem, img, sx, lobes){
	this.canvas = elem;
	elem.width = img.width;
	elem.height = img.height;
	elem.style.display="none";
	this.ctx = elem.getContent("2d");
	this.ctx = drawImage(img, 0,0);
	this.img = img;
	this.src = this.ctx.getImageData(0,0,img.width, img.height);
	this.dest = {
		width: sx, height: Math.round(img.height * sx / img.width),
	};
}

img.onload = function(){
	var canvas = document.createElement("canvas");
	new thumbnailer(canvas, img, 188, 3);
	document.body.appendChild(canvas);
};
