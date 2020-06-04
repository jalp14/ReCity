// const text = document.querySelector(".banner-text");
// const str = text.textContent;
// const splitText = str.split("");
// text.textContent = "";
// for (let i = 0; i <splitText.length; i++) {
//     text.innerHTML += "<span>" + splitText[i] + "</span>";
// }

// let char = 0;
// let timer = setInterval(onTick, 50);

// function onTick(){
//     const span = text.querySelectorAll('span')[char];
//     span.classList.add('faded');
//     char++

//     if (char == splitText.length) {
//         complete();
//         return;
//     }

//     function complete() {
//         clearInterval(timer);
//         timer = null;
//     }
// }

const logo = document.querySelectorAll('#logo path');


for (let i = 0; i < logo.length; i++) {
    console.log(`letter ${i} is ${logo[i].getTotalLength()}`);
}

var controller = new ScrollMagic.Controller()
new ScrollMagic.Scene({
        triggerElement: "#banner",
        triggerHook: "onEnter",
    })
    .duration('300%')
    .setTween("#banner", {
        backgroundPosition: "50% 100%",
        ease: Linear.ease
    })
    //.addIndicators() // for debugging purposes
    .addTo(controller);




// Image Dictionary
var imageDict = {
    1 : "url(https://www.sheknows.com/wp-content/uploads/2018/08/mqv7jwdv18tolcgdiegm.jpeg)",
    2 : "url(https://images.ctfassets.net/wy4h2xf1swlt/asset_65797/ed725f994827f1a9806ecf4d910ed2db/171124_StoveBakedEggsBoiledEgg_01.jpg)",
    3 : "url(https://lh3.googleusercontent.com/proxy/O6cZgx6d2eQgMSv_m66hrcw-QtO9E-IN37mZZaDJmO3wmzjkP4uEzGeylDxkXu1-kxN6BiX6m1h8WZWNPqyZ80lps7kfTip4A0gCCBRgTCuP4BVK9HPnHJYTScI-Uy3ZzFuoE1yACu2jVSat_pmfyOlkugebWeilELjw4bOdb2mnVCo1fWtJFrdMxrQ)",
    4 : "url(https://media1.s-nbcnews.com/i/newscms/2017_44/1292809/bibimbap-today-110117-tease_d2d79d2744f9f98184a589f0bc920058.jpg)",
    5 : "url(https://www.bitemybun.com/wp-content/uploads/2019/06/korean-food-3908819_1920.jpg)",
    6 : "url(https://technext.github.io/food-funday/images/blog_bg.jpg)",
    7 : "url(https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/v1555352211/shape/mentalfloss/homemadehed.png?itok=XMF9U17Q)",
    8 : "url(https://scstylecaster.files.wordpress.com/2018/01/lentil-chili-recipe.jpg)",
    9 : "url(https://images.squarespace-cdn.com/content/v1/5b4e0e6a5b409b5848de216a/1536382993388-YJ6HC0RY1XHMX1EH88FD/ke17ZwdGBToddI8pDm48kAiQauKMq5t3zNDTFOhTnlJ7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0tb-hnCqoepq4X8c1traqO-_NrqY7vRbriOxzaFgT6Y6dynDdRL5TMOOSto-dGo7jQ/smart-food-banner.jpg?format=2500w)",
    10 : "url(https://www.sheknows.com/wp-content/uploads/2018/08/ti8wzfbbvdspxo8dg1ci.jpeg)",
    11 : "url(https://images.wallpaperscraft.com/image/fish_sauce_sesame_japanese_cuisine_lemon_laying_20751_1920x1080.jpg)",
    12 : "url(https://www.raymondblanc.com/wp-content/uploads/2019/04/RB_Spring1941727-e1554897698371-1920x1080.jpg)",
    13 : "url(https://headbangerskitchen.com/wp-content/uploads/2017/12/ALMONDFLOURCHOCOLATECAKE.jpg)",
    14 : "url(https://www.theslimmingfoodie.com/wp-content/uploads/2015/09/BRAZILIAN_PORK_STEW.jpg)",
    15 : "url(https://proximity.co.uk/wp-content/uploads/food-erp-software-infor-ab-world-foods.png)",
    16 : "url(https://theoxfordmagazine.com/wp-content/uploads/raymond-blanc-apple-tart-maman-blanc-recipe-1920x1080.jpg)",
}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


randImage = getRandomInt(1, Object.keys(imageDict).length)


// Change image
document.getElementById("banner").style.backgroundImage = imageDict[randImage]
