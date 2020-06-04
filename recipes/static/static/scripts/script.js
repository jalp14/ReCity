
        var searchres = []
        var query = ""
        var i = 1;

        $(document).ready(function(e) {
                    let h = '<p /><div> <label class="control-label  requiredField">Quantity:</label> <input type="text" name="qty" required id="qty"/> <label class="control-label  requiredField">Ingredient:</label> <input type="text" name="ing" required id="ing" oninput="getIngredients()" class="ui-autocomplete-input"/> <a href="#" id="remove">x</a></div>'
                    var maxRows = 20;

                    $("[name=ingredient_field_count]").val(i);
                    $("#add").click(function (e) {
                        if (i <= maxRows) {
                            $("#container").append(h)
                            document.getElementById("ing").setAttribute("name", `ing${i}`)
                            document.getElementById("ing").id = `ing${i}`
                            document.getElementById("qty").setAttribute("name", `qty${i}`)
                            document.getElementById("qty").id = `qty${i}`
                            i++;
                            $(`#ing${i-1}`).devbridgeAutocomplete({
                    lookup: searchres,
                    onSelect: function (suggestion) {
                        console.log(suggestion)
                    }
                });
                            $("[name=ingredient_field_count]").val(i);
                        }
                    });

                    $("#container").on('click', '#remove', function(e) {
                        $(this).parent('div').remove();
                        i--;
                        document.getElementById(`ing${i}`).setAttribute("name", `ing${i - 1}`)
                        document.getElementById(`ing${i}`).id = `ing${i - 1}`
                        document.getElementById(`qty${i}`).setAttribute("name", `qty${i - 1}`)
                        document.getElementById(`qty${i}`).id = `qty${i - 1}`
                        $("[name=ingredient_field_count]").val(i);
                    });

                    $("#container").on('dblclick', '#ing', function(e) {
                        console.log('function called')
                        $(this).val($('#ing').val());
                    });

                });


            function createPair(name, image) {
                var jsonObj = {value: name, image: image}
                return jsonObj
            }

            function getData(query) {

            let endpoint = 'https://trackapi.nutritionix.com/v2/search/instant?branded_region=2&branded=false&query='

                fetch(endpoint+query, {headers : {"x-app-id": "6d3a9ca1", "x-app-key": "a5facf6d43ddb75f5ae1f14c4091e45a"}})
                .then(function (response) {
                    return response.json();
                })
                .then(function (result) {
                    resArray = result
                    foodarray = resArray["common"]
                    console.log(foodarray)

                    console.log(foodarray.length)
                    searchres.length = 0
                    for (var i = 0; i <foodarray.length; i++) {
                        var tmpObj = foodarray[''+i]
                        tmpName = tmpObj['food_name']
                        tmpimagepath = tmpObj['photo']
                        tmpimage = tmpimagepath['thumb']
                        var s = createPair(tmpName,tmpimage)
                        searchres.push(s)
                    }
                    console.log(searchres)
                })
                };


                function addEvent(obj, evType, fn) {
                    if (obj.addEventListener) {
                    obj.addEventListener(evType, fn, false);
                return true;
                    } else if (obj.attachEvent) {
                    var r = obj.attachEvent("on" + evType, fn);
                    return r;
                } else {
                    alert("Handler could not be attached");
                    }
                }


                function getIngredients() {
                    var input = document.getElementById(`ing${i - 1}`).value
                    console.log(input)
                    if (input.length > 2) {
                        getData(input)
                    }
                };


                $(`#ing${i-1}`).devbridgeAutocomplete({
                    lookup: searchres,
                    onSelect: function (suggestion) {
                        console.log(suggestion)
                    },
                    onSearchComplete: function(query, suggestion){
                        suggestion = $('.autocomplete-suggestion').each(function(index){

                                $(this).prepend("<img width='30%' src=" + suggestion[index].image + "> ")

                        })
                    }
                });


