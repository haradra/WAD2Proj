function selectButton(element) {
    $(element).parent().find("button").removeClass("active");
    $(element).addClass("active");
}

function selectPaws(paws) {
    images=$("#div-rating").find("img");
    for(i=0; i<images.length; i++) {
        if(i<=paws-1) {
            images[i].src="/static/images/paw-filled.png";
        }
        else {
            images[i].src="/static/images/paw-empty.png";
        }
    }
}

function unselectPaws() {
    images=$("#div-rating").find("img");
    for(i=0; i<images.length; i++) {
        if($(images[i]).hasClass("images-rating-empty")) {
            images[i].src="/static/images/paw-empty.png";
        }
        else {
            images[i].src="/static/images/paw-filled.png";
        }
    }
}

function userFunction() {
    $("#user_form").show();
    $("#pet_form").hide();
}

function petFunction() {
    $("#user_form").hide();
    $("#pet_form").show();
}