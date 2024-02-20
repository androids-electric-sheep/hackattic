var readline = require("readline");
var rl = readline.createInterface(process.stdin);

rl.on("line", function (line) {
  let stack = [];
  for (let i = 0; i < line.length; ++i) {
    if (line[i] === ")") {
      if (stack.length === 0 || stack[stack.length - 1] !== "(") {
        console.log("no");
        return;
      }
      stack.pop();
    } else {
      stack.push("(");
    }
  }
  if (stack.length !== 0) {
    console.log("no");
    return;
  }
  console.log("yes");
});
