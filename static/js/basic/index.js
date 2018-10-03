jQuery(document).ready(function($) {
  var container = document.getElementById("content");

  var width = $(container).width();
  var height = window.innerHeight;

  container.style.perspective = "900px";
  document.body.style.overflow = "hidden";

  for (var i = 0; i < 50; i++) {

    var left = Math.random() * ((width - 50)-50)+50;
    var top = Math.random() * ((height - 50)-50)+50;

    var circle = document.createElement("DIV");
    circle.className = "circle";
    circle.style.position = "fixed";
    circle.style.opacity = 0;
    circle.style.zIndex = -1000000;
    circle.style.borderRadius = "25px";
    circle.style.backgroundColor = "#ffff99";
    circle.style.left = left + "px";
    circle.style.top = top + "px";
    circle.style.width = "50px";
    circle.style.height = "50px";

    var r = Math.random();
    var nd = Math.floor(r * (150 - 25) + 25);

    //circles have different initial positions on z-Axis:
    $(circle).velocity({ translateZ: [nd, nd] });

    //circles that are more distant are more blurry
    $(circle).velocity({ blur: (1 - r) * 5 });

    container.appendChild(circle);

    //cp = (velocitys) current position
    //background: if we want the animation of the circle start from screen position (left, top)...
    //... then we have to give velocity the initial values (0,0) for x- and y-Translation (see lines 100-101)
    //Test case: https://codepen.io/blaustern_fotografie/pen/QBwKZx
    //explanation: the zero-point for the animation of one circle lies on the initial screen position of the circle (left, top)
    circle.cp_x = 0;
    circle.cp_y = 0;

    //actual position on screen is always cp+offset
    circle.offset_x = left;
    circle.offset_y = top;

    //opacity (blur) decreases (increases) when the distance on the z-Axis grows (nd)
    $(circle).velocity({ opacity: r, blur: (1 - r) * 5 }, { duration: 3000 });
  }

  animateAll();

  function animateAll() {
    //found here: http://jsfiddle.net/Xw29r/

    $(".circle").each(function(index, element) {
      my_animate(element);
    });
  }

  function my_animate(circle) {

    //x- and y-movement as random distances:

    //y-distance between -250 and 250
    var move_y = Math.floor(Math.random() * (250 + 250) - 250);

    //x-distance between -500 and 500
    var move_x = Math.floor(Math.random() * (500 + 500) - 500);

    //circles must not pass the edges of the screen:

    //actual position on screen is always cp+offset
    //if position+move exceeds an edge, it is limited to the distance to the edge
    if (circle.cp_x + circle.offset_x + move_x > width) {
      move_x = width - (circle.cp_x + circle.offset_x) - 50;
    } else if (circle.cp_x + circle.offset_x + move_x < 0) {
      move_x = -(circle.cp_x + circle.offset_x) + 50;
    }

    if (circle.cp_y + circle.offset_y + move_y > height) {
      move_y = height - (circle.cp_y + circle.offset_y) - 50;
    } else if (circle.cp_y + circle.offset_y + move_y < 0) {
      move_y = -(circle.cp_y + circle.offset_y) + 50;
    }
    //note: due to the z-Transformation the circles will nevertheless exceed the edges to a certain extend, zoom out the webpage to see the boundary of the circles

    var r = Math.random();

    //slight movement along z-Axis
    var nd = Math.floor(r * (50 - 25) + 25);

    $(circle).velocity(
      {
        //velocity.js forcefeeding: [target_value, initial_value]
        translateX: [circle.cp_x + move_x, circle.cp_x],
        translateY: [circle.cp_y + move_y, circle.cp_y],
        translateZ: nd,
        opacity: r, //opacity (blur) decreases (increases) when the distance on the z-Axis grows (nd)
        blur: Math.round((1 - r) * 5)
      },
      {
        duration: Math.round(Math.random() * (100000 - 60000) + 60000),
        complete: function() {
          //update current position of circle
          circle.cp_x = circle.cp_x + move_x;
          circle.cp_y = circle.cp_y + move_y;
          my_animate(circle);
        }
      }
    );
  }
});