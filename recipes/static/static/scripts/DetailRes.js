let dailyEnergyIntake = 2000.0 // kcal

let dailyTotalFatIntake = 70.0 // per 100 grams
let maxDailyFat = 17.5
let minDailyFat = 3.0

let dailySaturatedFatIntake = 20.0 // grams
let maxDailySaturatedFat = 5.0
let minDailySaturatedFat = 1.5

let dailyCarbsIntake = 260 // grams


let dailySugarsInatke = 90.0 // grams
let maxDailySugars = 22.5
let minDailySugars = 5.0
let dailyProteinIntake = 50 // grams
let dailySaltIntake = 6.0 // grams
let maxDailySalt = 1.5
let minDailySalt = 0.3

var fatColor = "low"
var satsColor = "low"
var saltColor = "low"
var sugarColor = "low"

var s = document.getElementsByClassName("ing")
console.log(s);
var query
var tmpArray = []
for (i = 0; i < s.length; i++) {
tmpArray.push(s[i].innerHTML)
}
query = tmpArray.join(', ')
console.log(query)

var nf_saturates = 0.0
var nf_salt = 0.0
var nf_sugar = 0.0
var nf_totalfats = 0.0
var nf_calories = 0.0
var serving_qty = 0
let endpoint = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
$.ajax({
url : endpoint,
type : 'post',
data : {
    query : query
},
headers : {
    'x-app-id' : '6d3a9ca1',
    'x-app-key': 'a5facf6d43ddb75f5ae1f14c4091e45a'
},
dataType : 'json',
success : function (data) {

}
}).then(function (result) {
resArray = result
foodarray = resArray["foods"]
console.log(foodarray)

for (var i = 0; i < foodarray.length; i++) {
    var tmpObj = foodarray[i]
    nf_calories = nf_calories + tmpObj['nf_calories']
    nf_totalfats = nf_totalfats + tmpObj['nf_total_fat']
    nf_saturates = nf_saturates + tmpObj['nf_saturated_fat']
    nf_salt = nf_salt + tmpObj['nf_sodium']*2.5 // Multiply sodium by 2.5 to get salt content
    nf_sugar = nf_sugar + tmpObj['nf_sugars']
    serving_qty = serving_qty + tmpObj['serving_qty']
}
nf_salt /= Math.pow(100, 1); // Salt in mg so have to move the decimal place
console.log(nf_calories.toFixed(2))
console.log(nf_saturates.toFixed(2))
nf_salt /= 1000
console.log(nf_totalfats.toFixed(2))
console.log(nf_salt.toFixed(2))
console.log(nf_sugar.toFixed(2))
workoutColors()
injectValues()
});


function workoutColors() {
if (nf_totalfats <= minDailyFat) {
        fatColor = "low"
    } else if (nf_totalfats >= maxDailyFat) {
        fatColor = "high"
    } else {
        fatColor = "medium"
}

if (nf_saturates <= minDailySaturatedFat) {
        satsColor = "low"
    } else if (nf_saturates >= maxDailySaturatedFat) {
        satsColor = "high"
    } else {
    satsColor = "medium"
}

if (nf_salt <= minDailySalt) {
        saltColor = "low"
    } else if (nf_salt >= maxDailySalt) {
        saltColor = "high"
    } else {
        saltColor = "medium"
}

if (nf_sugar <= minDailySugars) {
        sugarColor = "low"
    } else if (nf_sugar >= maxDailySugars) {
        sugarColor = "high"
    } else {
        sugarColor = "medium"
    }
}

function injectValues() {
document.getElementById('energy').innerHTML = (nf_calories * 4.184).toFixed(2) + 'kJ' + ' ' +  nf_calories.toFixed(2) + 'kCal'
document.getElementById('energyper').innerHTML = ((nf_calories / dailyEnergyIntake) * 100).toFixed(2) + '%'


document.getElementById('total_fats').innerHTML = nf_totalfats.toFixed(2) + 'g'
document.getElementById('fatper').innerHTML = ((nf_totalfats / dailyTotalFatIntake) * 100).toFixed(2) + '%'
document.getElementById('topfat').className = "top " + fatColor;
document.getElementById('bottomfat').className = "bottom " + fatColor


document.getElementById('saturates').innerHTML = nf_saturates.toFixed(2) + 'g'
document.getElementById('satsper').innerHTML = ((nf_saturates / dailySaturatedFatIntake) * 100).toFixed(2) + '%'
document.getElementById('topsats').className = "top " + satsColor
document.getElementById('bottomsats').className = "bottom " + satsColor

document.getElementById('salt').innerHTML = nf_salt.toFixed(2) + 'g'
document.getElementById('saltper').innerHTML = ((nf_salt / dailySaltIntake) * 100).toFixed(2) + '%'
document.getElementById('topsalt').className = "top " + saltColor
document.getElementById('bottomsalt').className = "bottom " + saltColor

document.getElementById('sugar').innerHTML = nf_sugar.toFixed(2) + 'g'
document.getElementById('sugarper').innerHTML = ((nf_sugar / dailySugarsInatke) * 100).toFixed(2) + '%'
document.getElementById('topsugars').className = "top " + sugarColor
document.getElementById('bottomsugars').className = "bottom " + sugarColor
}

$('.reply-btn').click(function () {
$(this).parent().parent().next('.replied-comments').fadeToggle()
})

$(document).on('submit', '.comment-form', function(event){
event.preventDefault();
$.ajax({
type: 'POST',
url: $(this).attr('action'),
data: $(this).serialize(),
dataType: 'json',
success: function (response) {
$('.main-comment-section').html(response['form']);
$('.textarea').val('')
$('.reply-btn').click(function () {
$(this).parent().parent().next('.replied-comments').fadeToggle()
$('textarea').val('')
})
},
error: function (rs, e) {
console.log(rs.responseText);
}
});
});

$(document).on('submit', '.reply-form', function(event){
event.preventDefault();
$.ajax({
type: 'POST',
url: $(this).attr('action'),
data: $(this).serialize(),
dataType: 'json',
success: function (response) {
$('.main-comment-section').html(response['form']);
$('textarea').val('')
$('.reply-btn').click(function () {
$(this).parent().parent().next('.replied-comments').fadeToggle()
$('textarea').val('')
})
},
error: function (rs, e) {
console.log(rs.responseText);
}
});
});


/*                  MODAL DISPLAY                   */
function updateIngredientsTable(id, ingredient_title){
// Get the modal
var ingredientsModal = document.getElementById("updateIngredientModal");

// Get the <span> element that closes the modal
var span = document.getElementById("closeUpdateIngredient");

//Get Input Field
var inputIngredient = document.getElementById("updateInputIngredient");
inputIngredient.defaultValue = ingredient_title; // Default value for input

var submitBtn = document.getElementById("updateSubmitIngredient");

// When the user clicks on the button, open the modal
ingredientsModal.style.display = "block";

// When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        ingredientsModal.style.display = "none";
}

// Submit Update
submitBtn.onclick = function(event)
{
    updateIngredient(id, inputIngredient.value)
    ingredientsModal.style.display = "none";
}
};

function addIngredientsTable(recipe_id){
// Get the modal
var ingredientsModal = document.getElementById("addIngredientModal");

// Get the <span> element that closes the modal
var span = document.getElementById("closeAddIngredient");

//Get Input Field
var inputIngredient = document.getElementById("addInputIngredient");

var submitBtn = document.getElementById("addSubmitIngredient");

// When the user clicks on the button, open the modal
ingredientsModal.style.display = "block";

// When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        ingredientsModal.style.display = "none";
}

// Submit Update
submitBtn.onclick = function(event)
{
    addIngredient(inputIngredient.value, recipe_id)
    inputIngredient.value = ""
    ingredientsModal.style.display = "none";
}
};

function instructionsTable(recipe_id){
    // Get the modal
    var instructionsModal = document.getElementById("instructionsModal");

    // Get the <span> element that closes the modal
    var span = document.getElementById("closeInstructions");

    //Get Input Field
    var inputInstructions = document.getElementById("inputInstructions");

    var submitBtn = document.getElementById("submitInstructions");

    inputInstructions.defaultValue = document.getElementById("recipeInstructions").textContent;

    // When the user clicks on the button, open the modal
    instructionsModal.style.display = "block";

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        instructionsModal.style.display = "none";
    }

    // Submit Update
    submitBtn.onclick = function(event)
    {
        editInstructions(recipe_id, inputInstructions.value)
        instructionsModal.style.display = "none";
    }
};

function editTable(recipe_id, recipe_title, description){

// Get the modal
var editModal = document.getElementById("editModal");

// Get the <span> element that closes the modal
var span = document.getElementById("closeEdit");

//Get Input Field
var inputedit = document.getElementById("inputEdit");

var submitBtn = document.getElementById("submitEdit");


// When the user clicks on the button, open the modal
editModal.style.display = "block";

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    editModal.style.display = "none";
}

// Submit Update
submitBtn.onclick = function(event)
{
    //editRecipe(recipe_id, recipe_title, description, categories);
    editModal.style.display = "none";
}
};

/*                          AJAX                    */

function updateIngredient(id, ingredient_title)
{
$.ajax({
        type: 'PUT',
        url: '/recipes/recipe/update-ingredient-ajax/',
        data:JSON.stringify({"ingredient_id":id, "ingredient_title":ingredient_title}),
        contentType: 'application/json;charset=UTF-8',
        async: false,
        dataType: 'json',
        success: function (response) {
            if (!response.success)
            {
                alert(response.error_msg);
            }else
            {
                $('.main-ingredients-table').html(response.recipe)
                recalculateCalories();
            }
        }
    });
};

function deleteIngredient(id)
{
$.ajax({
        type: 'DELETE',
        url: '/recipes/recipe/delete-ingredient-ajax/',
        data:JSON.stringify({"ingredient_id":id}),
        contentType: 'application/json;charset=UTF-8',
        async: false,
        dataType: 'json',
        success: function (response) {
            if (!response.success)
            {
                alert(response.error_msg);
            }else
            {
                $('.main-ingredients-table').html(response.recipe)
                recalculateCalories();
            }
        }
    });
};

function addIngredient(ingredient_title, recipe_id)
{
$.ajax({
        type: 'POST',
        url: '/recipes/recipe/add-ingredient-ajax/',
        data:JSON.stringify({"ingredient_title":ingredient_title, "recipe_id":recipe_id}),
        contentType: 'application/json;charset=UTF-8',
        async: false,
        dataType: 'json',
        success: function (response) {
            if (!response.success)
            {
                alert(response.error_msg);
            }else
            {
                $('.main-ingredients-table').html(response.recipe)
                recalculateCalories();
            }
        }
    });
};

function editInstructions(recipe_id, instructions)
{
$.ajax({
        type: 'PUT',
        url: '/recipes/recipe/update-instructions-ajax/',
        data:JSON.stringify({"recipe_id":recipe_id, "instructions":instructions}),
        contentType: 'application/json;charset=UTF-8',
        async: false,
        dataType: 'json',
        success: function (response) {
            if (!response.success)
            {
                alert(response.error_msg);
            }else
            {
                $('.main-instructions-body').html(response.recipe);
            }
        }
    });
};

function editRecipe(recipe_id, recipe_title, description, categories)
{
$.ajax({
        type: 'PUT',
        url: '/recipes/recipe/edit-recipe-ajax/',
        data:JSON.stringify({"recipe_id":recipe_id, "instructions":instructions}),
        contentType: 'application/json;charset=UTF-8',
        async: false,
        dataType: 'json',
        success: function (response) {
            if (!response.success)
            {
                alert(response.error_msg);
            }else
            {
                $('.main-instructions-body').html(response.recipe);
            }
        }
    });
};

/*                  AJAX CSRF                   */

function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
}
});

function recalculateCalories() {
s = document.getElementsByClassName("ing")
tmpArray = [];
for (i = 0; i < s.length; i++) {
    tmpArray.push(s[i].innerHTML)
}
query = tmpArray.join(', ')

nf_saturates = 0.0
nf_salt = 0.0
nf_sugar = 0.0
nf_totalfats = 0.0
nf_calories = 0.0
serving_qty = 0
$.ajax({
        url : endpoint,
        type : 'post',
        data : {
            query : query
        },
        headers : {
            'x-app-id' : '6d3a9ca1',
            'x-app-key': 'a5facf6d43ddb75f5ae1f14c4091e45a'
        },
        dataType : 'json',
        success : function (data) {

        }
    }).then(function (result) {
        resArray = result
        console.log(resArray)
        foodarray = resArray["foods"]
        console.log(foodarray)

        for (var i = 0; i < foodarray.length; i++) {
            var tmpObj = foodarray[i]
            nf_calories = nf_calories + tmpObj['nf_calories']
            nf_totalfats = nf_totalfats + tmpObj['nf_total_fat']
            nf_saturates = nf_saturates + tmpObj['nf_saturated_fat']
            nf_salt = nf_salt + tmpObj['nf_sodium']*2.5 // Multiply sodium by 2.5 to get salt content
            nf_sugar = nf_sugar + tmpObj['nf_sugars']
            serving_qty = serving_qty + tmpObj['serving_qty']
        }
        nf_salt /= Math.pow(100, 1); // Salt in mg so have to move the decimal place
        console.log(nf_calories.toFixed(2))
        console.log(nf_saturates.toFixed(2))
        nf_salt /= 1000
        console.log(nf_totalfats.toFixed(2))
        console.log(nf_salt.toFixed(2))
        console.log(nf_sugar.toFixed(2))
        workoutColors();
        injectValues();
    });
}   