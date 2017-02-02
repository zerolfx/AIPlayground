// this file should be pure javascript

function randomWord(min, max) {
  var str = "", range = min;
  var arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
   'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
   'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
   'W', 'X', 'Y', 'Z'];
  if (max != min)
    range = Math.round(Math.random() * (max-min)) + min;
  for(var i=0; i<range; i++){
    pos = Math.round(Math.random() * (arr.length-1));
    str += arr[pos];
  }
  return str;
}

function randomString() {
  return randomWord(32, 32);
}

function writeJavascript(href) {
  document.write('<script src="' + href + '?v=' + randomString() + '"\><\/script>');
}

function writeCss(href) {
  document.write('<link href="' + href + '?v=' + randomString() + '" rel="stylesheet">');
}
