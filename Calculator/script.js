const num = document.querySelectorAll("#keyboard>div");
const dis = document.querySelector("#input");

for (i = 0; i < num.length; i++) {
  num[i].addEventListener("click", cal);
}

function cal() {
  let tar = event.target.innerText;
  let a = dis.innerText;
  let b = a.slice(0, -1);

  switch (tar) {
    case "C":
      dis.innerText = "";
      break;

    case "=":
      if (a[0] == "/" || a[0] == "*") {
        dis.innerText = "Please check the input";
      } else if (dis.innerText != "") {
        dis.innerText = eval(dis.innerText);
      }
      break;
    case "Back":
      dis.innerText = b;

      break;
    default:
      dis.innerText += tar;
  }
}
