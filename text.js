
let n = 20;

// for (let i = 0; i < n; i++) {
//     for (let j = 0; j < i; j++) {
//         let square = i ** 2 + j ** 2;
//         c = parseInt(Math.sqrt(square));
//         if (square - c ** 2 == 0) {
//             console.log(j, i, c);
//         }
//     }
// }

const myPattern = (n) => {
    let space = 2 * n - 2;
    for (let i = 0; i < n; i++) {
        for (j = 0; j < space; j++) {
            console.log(" ");
        }
        space = space - 1;
        for (j = 0; j <= i + 1; j++) {
            console.log("* " + "");
        }
        console.log("\r");
    }
};

myPattern(5);