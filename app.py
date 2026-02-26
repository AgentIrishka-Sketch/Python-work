import streamlit as st
import streamlit.components.v1 as components

st.title("Интерактивные частицы, реагирующие на мышь 🖱️✨")

html_code = """
<!DOCTYPE html>
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>
</head>
<body style="margin:0; overflow:hidden; background:black;">
<script>

let particles = [];

class Particle {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.vx = random(-1, 1);
    this.vy = random(-1, 1);
  }

  update() {

    let dx = mouseX - this.x;
    let dy = mouseY - this.y;
    let dist = sqrt(dx*dx + dy*dy);

    if (dist < 150) {
      this.vx += dx * 0.0005;
      this.vy += dy * 0.0005;
    }

    this.x += this.vx;
    this.y += this.vy;

    this.vx *= 0.98;
    this.vy *= 0.98;
  }

  draw() {
    noStroke();
    fill(0, 200, 255);
    circle(this.x, this.y, 4);
  }
}

function setup() {
  let canvas = createCanvas(window.innerWidth, 500);
  canvas.parent(document.body);

  for (let i = 0; i < 300; i++) {
    particles.push(new Particle(random(width), random(height)));
  }
}

function draw() {
  background(0, 40);

  for (let p of particles) {
    p.update();
    p.draw();
  }
}

</script>
</body>
</html>
"""

components.html(html_code, height=500)
