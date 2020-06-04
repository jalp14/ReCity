        var area_photo = document.createElement('div')
        area_photo.id = "image_area_photo"
        document.getElementById('id_photo').parentNode.insertBefore(area_photo, document.getElementById('id_photo').nextSibling)
        document.getElementById('id_photo').addEventListener('input', handleFileSelect, false);

        var area_thumbnail = document.createElement('div')
        area_thumbnail.id = "image_area_thumbnail"
        document.getElementById('id_thumbnail').parentNode.insertBefore(area_thumbnail, document.getElementById('id_thumbnail').nextSibling)
        document.getElementById('id_thumbnail').addEventListener('input', handleFileThumbnailSelect, false);
    
        function handleFileSelect(evt) {
            var image_holder_photo = document.getElementById("image_holder_photo");
            if (image_holder_photo != null) {
                console.log("removing image_holder_photo")
                image_holder_photo.parentElement.removeChild(document.getElementById("image_holder_photo"));
            }
            console.log("creating image_holder_thumbnail...")
            image_holder_photo = document.createElement("div");
            image_holder_photo.id = "image_holder_photo";
            document.getElementById("image_area_photo").append(image_holder_photo);
    
    
            var files = evt.target.files;
            console.log(files);
    
            var count = 0;
            for (i = 0; i < files.length; i++) {
                var reader = new FileReader();
                reader.addEventListener("load", function (event) {
    
                    var picFile = event.target;
                    var img = document.createElement("img")
                    img.style.paddingRight = "10px";
                    img.id = "img_" + count;
                    img.src = picFile.result;
                    img.height = 150;
                    img.width = 150;
                    document.getElementById('image_holder_photo').append(img);

                });
                reader.readAsDataURL(files[i]);
                console.log(files[i])
            }
    
        }

        function handleFileThumbnailSelect(evt) {
            var image_holder_thumbnail = document.getElementById("image_holder_thumbnail");
            if (image_holder_thumbnail != null) {
                console.log("removing image_holder_thumbnail")
                image_holder_thumbnail.parentElement.removeChild(document.getElementById("image_holder_thumbnail"));
            }
            console.log("creating image_holder_thumbnail...")
            image_holder_thumbnail = document.createElement("div");
            image_holder_thumbnail.id = "image_holder_thumbnail";
            document.getElementById("image_area_thumbnail").append(image_holder_thumbnail);
    
    
            var files = evt.target.files;
            console.log(files);
    
            var count = 0;
            for (i = 0; i < files.length; i++) {
                var reader = new FileReader();
                reader.addEventListener("load", function (event) {
    
                    var picFile = event.target;
                    var img = document.createElement("img")
                    img.style.paddingRight = "10px";
                    img.id = "img_" + count;
                    img.src = picFile.result;
                    img.height = 150;
                    img.width = 150;
                    document.getElementById('image_holder_thumbnail').append(img);

                });
                reader.readAsDataURL(files[i]);
                console.log(files[i])
            }
    
        }