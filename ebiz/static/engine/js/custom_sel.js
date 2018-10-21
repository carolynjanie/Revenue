"color:black">"color:red"> "color:mediumblue">var x, i, j, selElmnt, a, b, c;
"color:green">/*look for any elements with the class "custom-select":*/
x = document."color:black">getElementsByClassName("color:brown">"custom-select");
"color:red"> "color:mediumblue">for (i = "color:red">0; i < x."color:black">length; i++) {
  selElmnt = x[i]."color:black">getElementsByTagName("color:brown">"select")["color:red">0];
  "color:green">/*for each element, create a new DIV that will act as the selected item:*/
  "color:red"> a = document."color:black">createElement("color:brown">"DIV");
  a."color:black">setAttribute("color:brown">"class", "color:red"> "color:brown">"select-selected");
  a."color:black">innerHTML = selElmnt."color:black">options[selElmnt."color:black">selectedIndex]."color:black">innerHTML;
  "color:red"> x[i]."color:black">appendChild(a);
  "color:green">/*for each element, create a new DIV that will contain the option list:*/
  b = document."color:black">createElement("color:brown">"DIV");
  "color:red"> b."color:black">setAttribute("color:brown">"class", "color:brown">"select-items select-hide");
  "color:mediumblue">for (j = "color:red"> "color:red">1; j < selElmnt."color:black">length; j++) {
    "color:green">/*for each option in the original select element,
    create a new DIV that will act as an option item:*/
    c = document."color:black">createElement("color:brown">"DIV");
    "color:red"> c."color:black">innerHTML = selElmnt."color:black">options[j]."color:black">innerHTML;
    "color:red"> c."color:black">addEventListener("color:brown">"click", "color:mediumblue">function(e) {
        "color:red"> "color:green">/*when an item is clicked, update the original select box,
        and the selected item:*/
        "color:mediumblue">var y, "color:red"> i, k, s, h;
        s = "color:red"> "color:mediumblue">this."color:black">parentNode."color:black">parentNode."color:black">getElementsByTagName("color:brown">"select")["color:red">0];
        "color:red"> h = "color:mediumblue">this."color:black">parentNode."color:black">previousSibling;
        "color:red"> "color:mediumblue">for (i = "color:red">0; i < s."color:black">length; i++) {
          "color:red"> "color:mediumblue">if (s."color:black">options[i]."color:black">innerHTML == "color:mediumblue">this."color:black">innerHTML) {
            "color:red"> s."color:black">selectedIndex = i;
            "color:red"> h."color:black">innerHTML = "color:mediumblue">this."color:black">innerHTML;
            "color:red"> y = "color:mediumblue">this."color:black">parentNode."color:black">getElementsByClassName("color:brown">"same-as-selected");
            "color:red"> "color:mediumblue">for (k = "color:red">0; k < y."color:black">length; k++) {
              "color:red"> y[k]."color:black">removeAttribute("color:brown">"class");
            "color:red"> }
            "color:red"> "color:mediumblue">this."color:black">setAttribute("color:brown">"class", "color:brown">"same-as-selected");
            "color:red"> "color:mediumblue">break;
          }
        "color:red"> }
        h."color:black">click();
    "color:red"> });
    b."color:black">appendChild(c);
  }
  x[i]."color:black">appendChild(b);
  "color:red"> a."color:black">addEventListener("color:brown">"click", "color:mediumblue">function(e) {
      "color:red"> "color:green">/*when the select box is clicked, close any other select boxes,
      and open/close the current select box:*/
      "color:red"> e."color:black">stopPropagation();
      closeAllSelect("color:mediumblue">this);
      "color:red"> "color:mediumblue">this."color:black">nextSibling."color:black">classList."color:black">toggle("color:brown">"select-hide");
      "color:red"> "color:mediumblue">this."color:black">classList."color:black">toggle("color:brown">"select-arrow-active");
  });
}
"color:mediumblue">function closeAllSelect(elmnt) {
  "color:green">/*a function that will close all select boxes in the document,
  except the current select box:*/
  "color:mediumblue">var x, y, i, arrNo = [];
  x = "color:red"> document."color:black">getElementsByClassName("color:brown">"select-items");
  y = "color:red"> document."color:black">getElementsByClassName("color:brown">"select-selected");
  "color:mediumblue">for (i = "color:red">0; i < "color:red"> y."color:black">length; i++) {
    "color:mediumblue">if (elmnt == y[i]) {
      "color:red"> arrNo."color:black">push(i)
    } "color:mediumblue">else {
      "color:red"> y[i]."color:black">classList."color:black">remove("color:brown">"select-arrow-active");
    }
  "color:red"> }
  "color:mediumblue">for (i = "color:red">0; i < x."color:black">length; i++) {
    "color:mediumblue">if (arrNo."color:black">indexOf(i)) "color:red"> {
      x[i]."color:black">classList."color:black">add("color:brown">"select-hide");
    "color:red"> }
  }
}
"color:green">/*if the user clicks anywhere outside the select box,
then close all select boxes:*/
document."color:black">addEventListener("color:brown">"click", closeAllSelect); 