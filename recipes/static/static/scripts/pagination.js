var page = 0;
var elementCount = $('.recipe-tile-outer').length
var countArray = []

window.onload = load()

function load() {
    for (var i = 1; i <= elementCount; i++) {
        countArray.push(i)
        $(`#recipe-tile-outer-${i}`).hide();
    }

    for (var i = 1; i <= 3; i++) {
        $('.all-grid .recipe-tile-outer#recipe-tile-outer-' + countArray[0]).show();
        $('.all-grid .recipe-tile-outer#recipe-tile-outer-' + countArray[0]).onclick = ;
            console.log(`Before : ${countArray}`)
            countArray.splice(0, 1)
            console.log(`After : ${countArray}`)
            elementCount = $('.recipe-tile-outer').length
            page++;
        }

        $('html,body').animate({
            scrollTop: $('.all-grid .recipe-tile-outer#recipe-tile-outer-' + (1)).offset().top
        },
        'slow');

    $('#more').click(nextPage);
}
function showPage(page) {
    for (var i = 1; i <= 3; i++) {
    $('.all-grid .recipe-tile-outer#recipe-tile-outer-' + countArray[0]).show();
        console.log(`Before : ${countArray}`)
        countArray.splice(0, 1)
        console.log(`After : ${countArray}`)
        elementCount = $('.recipe-tile-outer').length
        page++;
    }

    $('html,body').animate({
            scrollTop: $('.all-grid .recipe-tile-outer#recipe-tile-outer-' + (page)).offset().top
        },
        'slow');
}


function nextPage() {

    showPage(page);
}


