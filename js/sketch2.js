let sketch = function(p) {
let model;
  p.setup = function(){
    p.createCanvas(p.windowWidth, 400,p.WEBGL);
    p.background(0);
	model = p.loadModel("js/a.obj");
  }
  
  p.draw = function(){
  
      var scrollTop = window.pageYOffset || (document.documentElement || document.body.parentNode || document.body).scrollTop;
      
      p.background(scrollTop);
      p.rotateY(p.PI);
      p.rotateX(-p.HALF_PI);
      p.rotateX(0.01 * scrollTop);
      
      p.rotateZ(p.cos(p.frameCount*0.03)*0.1);
      p.rotateY(p.sin(p.frameCount*0.02)*0.1);
      
      p.noFill();
      p.stroke(255);
      p.strokeWeight(0.5);
      p.scale(100 - scrollTop*0.1);
	p.model(model);
  }
  


  // dynamically adjust the canvas to the window
  p.windowResized = function() {
      p.resizeCanvas(p.windowWidth, 400);

  }
};
new p5(sketch, 'container1');
